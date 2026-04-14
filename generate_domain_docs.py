#!/usr/bin/env python3
"""Generate domain-layer documentation pages.

Reads the OpenAPI spec, unwraps RPC-style response/request bodies to their
inner domain entities, and emits one markdown page per domain concept under
docs/domain/. Hub pages are generated for polymorphic unions (Transaction),
multi-view entities (Stakeholder), and subsystems (Compensation Benchmarks).

Run: python generate_domain_docs.py
"""
from __future__ import annotations

import json
import posixpath
import re
import urllib.error
import urllib.request
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

try:
    import yaml  # type: ignore
except ImportError:  # pragma: no cover
    yaml = None  # type: ignore

ROOT = Path(__file__).parent
SPEC_PATH = ROOT / "carta-issuer-api.openapi.json"
DOCS_DIR = ROOT / "docs"
DOMAIN_DIR = DOCS_DIR / "domain"
OBJECTS_DIR = DOCS_DIR / "objects"
TYPES_DIR = DOCS_DIR / "types"
OCF_MAPPING_PATH = ROOT / "ocf_mapping.yaml"
OCF_CACHE_DIR = ROOT / "build" / "ocf-schemas"
OCF_DOCS_BASE = "https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF"
OCF_RAW_BASE = (
    "https://raw.githubusercontent.com/"
    "Open-Cap-Table-Coalition/Open-Cap-Format-OCF/main/docs/schema_markdown/schema"
)

REF_RE = re.compile(r"^#/components/schemas/(.+)$")
METHODS = ("get", "post", "put", "patch", "delete")


# ---------------------------------------------------------------------------
# Domain categorization (hand-curated — the spec has no "category" field)
# ---------------------------------------------------------------------------

CATEGORIES: list[tuple[str, list[str]]] = [
    (
        "Organization",
        ["v1alpha1Corporation", "v1alpha1Issuer", "__stakeholder_hub__"],
    ),
    (
        "Cap Table",
        [
            "v1alpha1CapitalizationTable",
            "v1alpha1StakeholderCapitalizationTable",
            "v1alpha1ShareClass",
        ],
    ),
    (
        "Securities",
        [
            "v1alpha1Certificate",
            "v1alpha1ConvertibleNote",
            "v1alpha1OptionGrant",
            "v1alpha1RestrictedStockAward",
            "v1alpha1RestrictedStockUnit",
            "v1alpha1DraftOptionGrant",
        ],
    ),
    (
        "Securities Activity",
        ["v1alpha1OptionExercise", "__transaction_hub__"],
    ),
    (
        "Reference Data",
        [
            "v1alpha1Interest",
            "v1alpha1FairMarketValue",
            "v1alpha1PointOfContact",
            "v1alpha1VestingScheduleTemplate",
        ],
    ),
    (
        "Compensation Benchmarks",
        ["__compensation_benchmarks_hub__"],
    ),
]

# Schemas backing the three hub pages
TRANSACTION_VARIANTS: list[tuple[str, str]] = [
    ("v1alpha1OptionTransactionItem", "Option grants"),
    ("v1alpha1RsuTransactionItem", "Restricted stock units"),
    ("v1alpha1RsaTransactionItem", "Restricted stock awards"),
    ("v1alpha1CertificateTransactionItem", "Certificates"),
    ("v1alpha1WarrantTransactionItem", "Warrants"),
    ("v1alpha1ConvertibleTransactionItem", "Convertible notes"),
    ("v1alpha1PiuTransactionItem", "Profits interest units"),
    ("v1alpha1SarTransactionItem", "Stock appreciation rights"),
]

STAKEHOLDER_VIEWS: list[tuple[str, str]] = [
    (
        "publicapiissuersv1alpha1Stakeholder",
        "Returned by the public `GET /issuers/{id}/stakeholders` endpoints.",
    ),
    (
        "issuerscapitalizationv1alpha1Stakeholder",
        "Embedded in capitalization table rows.",
    ),
    (
        "issuersdraftsecuritiesv1alpha1Stakeholder",
        "Embedded in draft option grant bodies.",
    ),
    (
        "publicapiissuersv1alpha1StakeholderRelationship",
        "Relationship metadata for public stakeholders.",
    ),
    (
        "issuersdraftsecuritiesv1alpha1StakeholderRelationship",
        "Relationship metadata for draft-securities stakeholders.",
    ),
]

BENCHMARKS_MEMBERS: list[tuple[str, str]] = [
    ("v1alpha1Benchmarks", "The benchmark dataset itself."),
    ("v1alpha1BenchmarkJob", "A job role within the benchmark dataset."),
    ("v1alpha1BenchmarksMetadata", "Metadata describing the benchmark dataset."),
    ("v1alpha1Access", "Access/entitlement information for benchmarks."),
]


# ---------------------------------------------------------------------------
# Name sanitization (mirrors schema_composer.py so cross-links resolve)
# ---------------------------------------------------------------------------


def sanitize(schema_name: str) -> str:
    parts = schema_name.split("v1alpha1")
    if len(parts) == 2 and parts[0]:
        ns = re.sub(r"(?<!^)(?=[A-Z])", "_", parts[0]).lower()
        sn = re.sub(r"(?<!^)(?=[A-Z])", "_", parts[1]).lstrip("_").lower()
        return f"{ns}_{sn}"
    name = parts[-1] if parts else schema_name
    sn = re.sub(r"(?<!^)(?=[A-Z])", "_", name).lstrip("_").lower()
    return sn or schema_name.lower()


def title_case(sanitized: str) -> str:
    return " ".join(w.capitalize() for w in sanitized.split("_"))


# ---------------------------------------------------------------------------
# Spec traversal helpers
# ---------------------------------------------------------------------------


def collect_refs(node: Any) -> list[str]:
    out: list[str] = []

    def walk(n: Any) -> None:
        if isinstance(n, dict):
            for k, v in n.items():
                if k == "$ref" and isinstance(v, str):
                    m = REF_RE.match(v)
                    if m:
                        out.append(m.group(1))
                else:
                    walk(v)
        elif isinstance(n, list):
            for item in n:
                walk(item)

    walk(node)
    return out


@dataclass
class EndpointHit:
    method: str
    path: str
    role: str  # "request", "resp 200", etc.
    cardinality: str  # "single" | "list"
    wrapper: str
    property_name: str


@dataclass
class DomainEntity:
    schema_name: str  # e.g. "v1alpha1OptionGrant"
    sanitized: str  # e.g. "option_grant"
    endpoints: list[EndpointHit] = field(default_factory=list)
    referenced_by: list[tuple[str, str]] = field(default_factory=list)
    # list of (parent_schema_name, property_name)


def find_wrapper_endpoints(spec: dict) -> dict[str, list[tuple[str, str, str]]]:
    """wrapper_schema_name -> [(path, METHOD, role)]"""
    out: dict[str, list[tuple[str, str, str]]] = defaultdict(list)
    for path, ops in spec["paths"].items():
        for method, op in ops.items():
            if method not in METHODS:
                continue
            for ref in collect_refs(op.get("requestBody", {})):
                out[ref].append((path, method.upper(), "request"))
            for code, resp in (op.get("responses") or {}).items():
                if code.startswith("2"):
                    for ref in collect_refs(resp):
                        out[ref].append((path, method.upper(), f"resp {code}"))
    return out


def unwrap(wrapper_schema: dict) -> list[tuple[str, str, str]]:
    """Return [(property_name, target_schema, "single"|"list")] for one-hop
    $refs inside the wrapper's top-level properties."""
    out: list[tuple[str, str, str]] = []
    for prop_name, prop_def in (wrapper_schema.get("properties") or {}).items():
        if not isinstance(prop_def, dict):
            continue
        if "$ref" in prop_def:
            m = REF_RE.match(prop_def["$ref"])
            if m:
                out.append((prop_name, m.group(1), "single"))
        elif prop_def.get("type") == "array":
            items = prop_def.get("items") or {}
            if "$ref" in items:
                m = REF_RE.match(items["$ref"])
                if m:
                    out.append((prop_name, m.group(1), "list"))
    return out


# ---------------------------------------------------------------------------
# Property rendering — cross-links into docs/objects or docs/types
# ---------------------------------------------------------------------------


def cross_link(schema_name: str) -> str:
    """Return a markdown link string for a referenced schema, probing
    docs/objects and docs/types (in that order) for an existing page."""
    sn = sanitize(schema_name)
    if (OBJECTS_DIR / f"{sn}.md").exists():
        return f"[`{schema_name}`](../objects/{sn}.md)"
    if (TYPES_DIR / f"{sn}.md").exists():
        return f"[`{schema_name}`](../types/{sn}.md)"
    return f"`{schema_name}`"


def type_string(prop_def: dict) -> str:
    """Render an OpenAPI property definition as a compact type string."""
    if not isinstance(prop_def, dict):
        return "?"
    if "$ref" in prop_def:
        m = REF_RE.match(prop_def["$ref"])
        return cross_link(m.group(1)) if m else "?"
    if prop_def.get("type") == "array":
        items = prop_def.get("items") or {}
        return f"{type_string(items)}[]"
    fmt = prop_def.get("format")
    t = prop_def.get("type", "object")
    if t == "string" and fmt:
        return f"string ({fmt})"
    if t == "integer" and fmt:
        return f"integer ({fmt})"
    if "enum" in prop_def:
        return "enum"
    return t


def format_description(raw: str | None) -> str:
    if not raw:
        return ""
    # Collapse whitespace and escape pipes for table safety
    cleaned = re.sub(r"\s+", " ", raw).strip()
    return cleaned.replace("|", "\\|")


# ---------------------------------------------------------------------------
# OCF mapping — loaded from ocf_mapping.yaml
# ---------------------------------------------------------------------------


def load_ocf_mapping() -> dict[str, dict]:
    if not OCF_MAPPING_PATH.exists():
        print(f"  note: {OCF_MAPPING_PATH.name} not found, skipping OCF sections")
        return {}
    if yaml is None:
        print("  note: PyYAML not installed, skipping OCF sections")
        return {}
    data = yaml.safe_load(OCF_MAPPING_PATH.read_text()) or {}
    if not isinstance(data, dict):
        print(f"  warn: {OCF_MAPPING_PATH.name} did not parse to a dict, ignoring")
        return {}
    return data


def ocf_url(entry: dict) -> str:
    """Build a doc-site URL for an OCF schema entry."""
    name = entry.get("name", "")
    kind = entry.get("kind", "object")
    if kind == "transaction":
        category = entry.get("category", "")
        return f"{OCF_DOCS_BASE}/schema_markdown/schema/objects/transactions/{category}/{name}/"
    return f"{OCF_DOCS_BASE}/schema_markdown/schema/objects/{name}/"


def render_ocf_section(mapping: dict[str, dict], key: str) -> str:
    """Render the 'OCF Equivalent' markdown section for a given mapping key.

    Returns an empty string if there's no entry for this key at all (caller can
    decide whether to omit or to show a "not mapped" stub).
    """
    entry = mapping.get(key)
    if entry is None:
        return ""
    summary = (entry.get("summary") or "").strip()
    ocf_list = entry.get("ocf") or []

    parts: list[str] = ["## OCF Equivalent\n"]
    if summary:
        parts.append(f"{summary}\n")

    if not ocf_list:
        parts.append(
            "_No direct Open Cap Format equivalent — see the summary above for why._\n"
        )
        return "\n".join(parts)

    # Split into primary and "also" bullets so the closest match is visually distinct.
    primary = [e for e in ocf_list if e.get("role", "primary") == "primary"]
    also = [e for e in ocf_list if e.get("role") == "also"]

    def render_bullet(e: dict) -> str:
        name = e.get("name", "?")
        url = ocf_url(e)
        kind = e.get("kind", "object")
        tag = f"_{e.get('category','')}_ tx" if kind == "transaction" else "object"
        note = e.get("note", "")
        line = f"- [`{name}`]({url}) — {tag}"
        if note:
            line += f". {note.strip()}"
        return line

    parts.append("")  # blank line before list
    for e in primary:
        parts.append(render_bullet(e))
    if also:
        parts.append("")
        parts.append("**Related:**")
        parts.append("")
        for e in also:
            parts.append(render_bullet(e))
    parts.append("")
    return "\n".join(parts)


# ---------------------------------------------------------------------------
# OCF markdown fetch / parse / link-rewrite
# ---------------------------------------------------------------------------


def _ocf_source_rel_path(entry: dict) -> str:
    """Return the OCF markdown file's path relative to `schema/`.

    e.g. "objects/StockClass.md"
      or "objects/transactions/issuance/StockIssuance.md"
    """
    name = entry.get("name", "")
    if entry.get("kind") == "transaction":
        category = entry.get("category", "")
        return f"objects/transactions/{category}/{name}.md"
    return f"objects/{name}.md"


def fetch_ocf_markdown(entry: dict) -> str | None:
    """Return the OCF markdown for `entry`, caching locally.

    Returns None on fetch failure — caller falls back to text-only OCF section.
    """
    rel = _ocf_source_rel_path(entry)
    cache_path = OCF_CACHE_DIR / rel
    if cache_path.exists():
        return cache_path.read_text()
    url = f"{OCF_RAW_BASE}/{rel}"
    try:
        with urllib.request.urlopen(url, timeout=15) as resp:
            text = resp.read().decode("utf-8")
    except (urllib.error.URLError, TimeoutError) as exc:
        print(f"  warn: failed to fetch {url}: {exc}")
        return None
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache_path.write_text(text)
    return text


_DESC_RE = re.compile(r"^\*\*Description:\*\*\s*_?([^_\n]+)_?\s*$", re.MULTILINE)
_PROPS_HEADER_RE = re.compile(r"^\*\*Properties:\*\*\s*$", re.MULTILINE)


def _rewrite_ocf_link(md_link: str, source_rel: str) -> str:
    """Rewrite a relative `.md` link inside an OCF markdown file to an
    absolute URL on the OCF doc site.

    `source_rel` is the location of the source file relative to `schema/`
    (e.g. "objects/StockClass.md") — relative links inside that file are
    resolved against its containing directory.
    """

    def repl(m: re.Match[str]) -> str:
        label = m.group(1)
        href = m.group(2)
        # Absolute URLs pass through untouched.
        if href.startswith(("http://", "https://")):
            return m.group(0)
        # Compute absolute path under `schema/`.
        base_dir = posixpath.dirname(source_rel)
        joined = posixpath.normpath(posixpath.join(base_dir, href))
        # Strip a trailing `.md`, append `/` to match the doc-site URL convention.
        if joined.endswith(".md"):
            joined = joined[:-3] + "/"
        url = f"{OCF_DOCS_BASE}/schema_markdown/schema/{joined}"
        return f"[{label}]({url})"

    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", repl, md_link)


@dataclass
class OcfView:
    name: str
    doc_url: str
    description: str
    properties_table: str  # multi-line markdown table (header + body rows)


def parse_ocf_markdown(md: str, entry: dict) -> OcfView | None:
    """Extract description and Properties table from an OCF markdown doc.

    Returns None if the expected structure isn't present.
    """
    desc_match = _DESC_RE.search(md)
    description = desc_match.group(1).strip().strip("_") if desc_match else ""

    header_match = _PROPS_HEADER_RE.search(md)
    if not header_match:
        return None
    after_header = md[header_match.end():]

    # The properties section is a markdown table: header line + separator + body,
    # followed by a blank line (which terminates the table) and then another
    # `**Section:**` header. Collect contiguous table rows.
    table_lines: list[str] = []
    in_table = False
    for line in after_header.splitlines():
        stripped = line.strip()
        if not in_table:
            if stripped.startswith("|"):
                in_table = True
                table_lines.append(line.rstrip())
            continue
        if stripped.startswith("|"):
            table_lines.append(line.rstrip())
        else:
            break  # end of table

    if len(table_lines) < 2:
        return None  # no header+separator+rows

    source_rel = _ocf_source_rel_path(entry)
    rewritten = "\n".join(
        _rewrite_ocf_link(line, source_rel) for line in table_lines
    )

    return OcfView(
        name=entry.get("name", ""),
        doc_url=ocf_url(entry),
        description=description,
        properties_table=rewritten,
    )


def get_ocf_primary_view(mapping: dict[str, dict], key: str) -> OcfView | None:
    """Fetch + parse the OCF markdown for the first `role: primary` entry
    under the given mapping key, or return None if no fetch is possible."""
    entry = mapping.get(key)
    if not entry:
        return None
    primaries = [e for e in (entry.get("ocf") or []) if e.get("role", "primary") == "primary"]
    if not primaries:
        return None
    first = primaries[0]
    md = fetch_ocf_markdown(first)
    if md is None:
        return None
    return parse_ocf_markdown(md, first)


def render_side_by_side(
    carta_title: str,
    carta_link: str,
    carta_table_md: str,
    ocf_view: OcfView,
) -> str:
    """Emit an HTML flex container with the Carta and OCF property tables
    rendered as two columns. Uses md_in_html so nested markdown tables parse.
    """
    ocf_desc = (ocf_view.description or "").replace("\n", " ")
    parts = [
        '<div class="domain-compare" markdown="1">\n',
        '<div class="domain-compare__col" markdown="1">\n',
        f"**Carta** — {carta_link}\n\n",
        f"_{carta_title}_\n\n",
        carta_table_md,
        "\n</div>\n",
        '<div class="domain-compare__col" markdown="1">\n',
        f"**OCF** — [`{ocf_view.name}`]({ocf_view.doc_url})\n\n",
        f"_{ocf_desc}_\n\n" if ocf_desc else "\n",
        ocf_view.properties_table,
        "\n</div>\n",
        "</div>\n",
    ]
    return "".join(parts)


def render_properties_table(schema: dict) -> str:
    props = schema.get("properties") or {}
    if not props:
        return "_(no properties defined)_\n"
    required = set(schema.get("required", []))
    lines = [
        "| Property | Type | Required | Description |",
        "|---|---|---|---|",
    ]
    for name, prop_def in props.items():
        ts = type_string(prop_def) if isinstance(prop_def, dict) else "?"
        desc = format_description(prop_def.get("description") if isinstance(prop_def, dict) else None)
        req = "✓" if name in required else ""
        lines.append(f"| `{name}` | {ts} | {req} | {desc} |")
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# Referenced-by index: which schemas embed this one as a property?
# ---------------------------------------------------------------------------


def build_referenced_by(schemas: dict) -> dict[str, list[tuple[str, str]]]:
    """target_schema -> [(parent_schema, property_name), ...]"""
    out: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for parent_name, parent_schema in schemas.items():
        props = parent_schema.get("properties") or {}
        for prop_name, prop_def in props.items():
            if not isinstance(prop_def, dict):
                continue
            # direct $ref
            if "$ref" in prop_def:
                m = REF_RE.match(prop_def["$ref"])
                if m:
                    out[m.group(1)].append((parent_name, prop_name))
            # array items $ref
            elif prop_def.get("type") == "array":
                items = prop_def.get("items") or {}
                if "$ref" in items:
                    m = REF_RE.match(items["$ref"])
                    if m:
                        out[m.group(1)].append((parent_name, prop_name))
    return out


# ---------------------------------------------------------------------------
# Endpoint-to-domain pairing
# ---------------------------------------------------------------------------


def build_domain_endpoints(
    spec: dict, schemas: dict
) -> dict[str, list[EndpointHit]]:
    """domain_schema -> list of EndpointHit entries that expose it."""
    wrapper_hits = find_wrapper_endpoints(spec)
    out: dict[str, list[EndpointHit]] = defaultdict(list)
    for wrapper, hits in wrapper_hits.items():
        wrapper_schema = schemas.get(wrapper)
        if not wrapper_schema:
            continue
        inner = unwrap(wrapper_schema)
        if not inner:
            continue
        for prop_name, domain_schema, cardinality in inner:
            for path, method, role in hits:
                out[domain_schema].append(
                    EndpointHit(
                        method=method,
                        path=path,
                        role=role,
                        cardinality=cardinality,
                        wrapper=wrapper,
                        property_name=prop_name,
                    )
                )
    return out


# ---------------------------------------------------------------------------
# Page rendering
# ---------------------------------------------------------------------------


def render_endpoints_section(hits: list[EndpointHit]) -> str:
    if not hits:
        return "_(no endpoints)_\n"
    # Collapse to unique (method, path, cardinality, role) — a wrapper can
    # appear in both response and request role for different methods.
    seen: set[tuple[str, str, str, str]] = set()
    lines: list[str] = []
    for hit in sorted(hits, key=lambda h: (h.path, h.method)):
        key = (hit.method, hit.path, hit.cardinality, hit.role)
        if key in seen:
            continue
        seen.add(key)
        marker = "list" if hit.cardinality == "list" else "single"
        role_tag = "" if hit.role.startswith("resp") else f" _(request body)_"
        lines.append(f"- `{hit.method} {hit.path}` — {marker}{role_tag}")
    return "\n".join(lines) + "\n"


def render_referenced_by_section(
    referenced_by: list[tuple[str, str]], self_schema: str
) -> str:
    # Exclude self-references and wrappers (wrappers we already list in Endpoints).
    filtered = [
        (parent, prop)
        for (parent, prop) in referenced_by
        if parent != self_schema
        and not parent.endswith("Response")
        and not parent.endswith("Body")
    ]
    if not filtered:
        return "_(not embedded in other domain objects)_\n"
    lines: list[str] = []
    seen: set[tuple[str, str]] = set()
    for parent, prop in sorted(filtered):
        if (parent, prop) in seen:
            continue
        seen.add((parent, prop))
        lines.append(f"- {cross_link(parent)}.`{prop}`")
    return "\n".join(lines) + "\n"


def render_entity_page(
    entity: DomainEntity, schema: dict, ocf_mapping: dict[str, dict]
) -> str:
    title = title_case(entity.sanitized)
    description = format_description(
        schema.get("description") or schema.get("title") or ""
    )
    parts: list[str] = [f"# {title}\n"]
    if description:
        parts.append(f"{description}\n")

    # Render the text-only OCF Equivalent section (summary + primary/also links).
    # This stays on every page so readers see the "no equivalent" rationale and
    # any secondary/related OCF types even when we also emit the side-by-side view.
    ocf_section = render_ocf_section(ocf_mapping, entity.schema_name)
    if ocf_section:
        parts.append(ocf_section)

    parts.append("## Endpoints\n")
    parts.append(render_endpoints_section(entity.endpoints))

    # Properties: side-by-side if we have a primary OCF view, otherwise the
    # familiar single-table layout.
    ocf_view = get_ocf_primary_view(ocf_mapping, entity.schema_name)
    if ocf_view is not None:
        parts.append("\n## Properties side-by-side\n")
        parts.append(
            render_side_by_side(
                carta_title=description or title,
                carta_link=cross_link(entity.schema_name),
                carta_table_md=render_properties_table(schema),
                ocf_view=ocf_view,
            )
        )
    else:
        parts.append("\n## Properties\n")
        parts.append(render_properties_table(schema))

    parts.append("\n## Referenced by\n")
    parts.append(render_referenced_by_section(entity.referenced_by, entity.schema_name))
    parts.append("\n---\n")
    parts.append(f"_Underlying schema: {cross_link(entity.schema_name)}_\n")
    parts.append("\n[← Back to Domain Index](index.md)\n")
    return "\n".join(parts)


def render_transaction_hub(ocf_mapping: dict[str, dict]) -> str:
    parts: list[str] = [
        "# Transaction\n",
        (
            "The Carta API does not expose a single `Transaction` type. Instead, "
            "`GET /v1alpha1/issuers/{issuerId}/transactions` returns **eight "
            "parallel arrays**, one per security type. Conceptually these are "
            "variants of the same `Transaction` domain concept; the spec models "
            "them as sibling fields rather than as a discriminated union.\n"
        ),
    ]
    ocf_section = render_ocf_section(ocf_mapping, "__transaction_hub__")
    if ocf_section:
        parts.append(ocf_section)
    parts += [
        "## Endpoints\n",
        "- `GET /v1alpha1/issuers/{issuerId}/transactions` — returns all variants in one response\n",
        "\n## Variants\n",
    ]
    for schema_name, label in TRANSACTION_VARIANTS:
        link = cross_link(schema_name)
        parts.append(f"- **{label}** — {link}")
    parts.append("\n## Response shape\n")
    parts.append(
        "```\n"
        "ListTransactionsResponse {\n"
        "  optionTransactions:      OptionTransactionItem[]\n"
        "  rsuTransactions:         RsuTransactionItem[]\n"
        "  rsaTransactions:         RsaTransactionItem[]\n"
        "  certificateTransactions: CertificateTransactionItem[]\n"
        "  warrantTransactions:     WarrantTransactionItem[]\n"
        "  convertibleTransactions: ConvertibleTransactionItem[]\n"
        "  piuTransactions:         PiuTransactionItem[]\n"
        "  sarTransactions:         SarTransactionItem[]\n"
        "}\n"
        "```\n"
    )
    parts.append("\n## Modeling note\n")
    parts.append(
        "If you are building a client-side domain model, you will likely want "
        "to merge these eight variants into a single polymorphic `Transaction` "
        "type with a discriminator field. The wire format does not provide one.\n"
    )
    parts.append("\n[← Back to Domain Index](index.md)\n")
    return "\n".join(parts)


def render_stakeholder_hub(ocf_mapping: dict[str, dict]) -> str:
    parts: list[str] = [
        "# Stakeholder\n",
        (
            "The spec defines **five** separate `Stakeholder`-related schemas — "
            "different projections of the same conceptual entity depending on "
            "where it appears. The table below maps each view to its usage "
            "context. From a domain-modeling standpoint these are all the same "
            "`Stakeholder` aggregate root and you will typically want to merge "
            "them in any client-side model.\n"
        ),
    ]
    ocf_section = render_ocf_section(ocf_mapping, "__stakeholder_hub__")
    if ocf_section:
        parts.append(ocf_section)
    parts += [
        "## Endpoints (canonical stakeholder view)\n",
        "- `GET /v1alpha1/issuers/{issuerId}/stakeholders` — list",
        "- `GET /v1alpha1/issuers/{issuerId}/stakeholders/{id}` — single",
        "\n## Views\n",
    ]
    for schema_name, usage in STAKEHOLDER_VIEWS:
        link = cross_link(schema_name)
        parts.append(f"### {link}\n")
        parts.append(f"{usage}\n")
    parts.append("\n## Modeling note\n")
    parts.append(
        "A real domain layer over this API should unify these views into a "
        "single `Stakeholder` entity with optional context-specific fields. "
        "The wire-format split exists because the spec generator exposed each "
        "service's projection separately.\n"
    )
    parts.append("\n[← Back to Domain Index](index.md)\n")
    return "\n".join(parts)


def render_benchmarks_hub(ocf_mapping: dict[str, dict]) -> str:
    parts: list[str] = [
        "# Compensation Benchmarks\n",
        (
            "Compensation Benchmarks is a small subsystem bolted onto the "
            "corporations surface. Two endpoints serve four related types that "
            "together describe benchmark datasets, the jobs inside them, the "
            "metadata describing them, and the caller's access level.\n"
        ),
    ]
    ocf_section = render_ocf_section(ocf_mapping, "__compensation_benchmarks_hub__")
    if ocf_section:
        parts.append(ocf_section)
    parts += [
        "## Endpoints\n",
        "- `GET /v1alpha1/corporations/{corporationId}/compensationBenchmarks` "
        "— benchmark data + access + metadata",
        "- `GET /v1alpha1/corporations/{corporationId}/compensationBenchmarkAttributes` "
        "— benchmark jobs + metadata",
        "\n## Members\n",
    ]
    for schema_name, desc in BENCHMARKS_MEMBERS:
        link = cross_link(schema_name)
        parts.append(f"- {link} — {desc}")
    parts.append("\n[← Back to Domain Index](index.md)\n")
    return "\n".join(parts)


def render_index(
    entities: dict[str, DomainEntity], schemas: dict
) -> str:
    lines: list[str] = [
        "# Domain Objects\n",
        (
            "Conceptual entities exposed by the Carta Issuer API. These pages "
            "unwrap the RPC-style `Get…Response` / `List…Response` envelopes "
            "to show the underlying domain objects and the endpoints that "
            "serve them. Polymorphic unions and multi-view entities are "
            "presented as hub pages with drill-downs to the leaf types.\n"
        ),
    ]
    for category, members in CATEGORIES:
        lines.append(f"\n## {category}\n")
        for m in members:
            if m == "__transaction_hub__":
                lines.append("- [Transaction](transaction.md) — polymorphic union, 8 variants")
            elif m == "__stakeholder_hub__":
                lines.append("- [Stakeholder](stakeholder.md) — 5 context-specific views")
            elif m == "__compensation_benchmarks_hub__":
                lines.append(
                    "- [Compensation Benchmarks](compensation_benchmarks.md) — "
                    "4-type subsystem"
                )
            else:
                entity = entities.get(m)
                if not entity:
                    continue
                desc = format_description(
                    (schemas.get(m) or {}).get("description") or ""
                )
                if desc and len(desc) > 100:
                    desc = desc[:97] + "…"
                suffix = f" — {desc}" if desc else ""
                lines.append(
                    f"- [{title_case(entity.sanitized)}]({entity.sanitized}.md){suffix}"
                )
    lines.append("\n---\n")
    lines.append(
        "[← Back to Home](../index.md) | "
        "[API Objects →](../objects/index.md) | "
        "[Supporting Types →](../types/index.md)\n"
    )
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> None:
    spec = json.loads(SPEC_PATH.read_text())
    schemas = spec["components"]["schemas"]
    DOMAIN_DIR.mkdir(parents=True, exist_ok=True)

    ocf_mapping = load_ocf_mapping()
    domain_endpoints = build_domain_endpoints(spec, schemas)
    referenced_by = build_referenced_by(schemas)

    # Figure out which domain schemas we'll actually render as per-entity pages.
    # Hubs (Transaction, Stakeholder, Benchmarks) are handled separately; skip
    # their member schemas so we don't double-publish.
    hub_members = {name for name, _ in TRANSACTION_VARIANTS}
    hub_members |= {name for name, _ in STAKEHOLDER_VIEWS}
    hub_members |= {name for name, _ in BENCHMARKS_MEMBERS}

    # Build DomainEntity objects only for schemas referenced in CATEGORIES
    # (not the hub placeholders).
    categorized_schemas: list[str] = []
    for _, members in CATEGORIES:
        for m in members:
            if not m.startswith("__"):
                categorized_schemas.append(m)

    entities: dict[str, DomainEntity] = {}
    for schema_name in categorized_schemas:
        if schema_name not in schemas:
            print(f"  WARN: {schema_name} not found in spec, skipping")
            continue
        entities[schema_name] = DomainEntity(
            schema_name=schema_name,
            sanitized=sanitize(schema_name),
            endpoints=domain_endpoints.get(schema_name, []),
            referenced_by=referenced_by.get(schema_name, []),
        )

    # Write per-entity pages
    print(f"Writing {len(entities)} per-entity pages…")
    missing_ocf: list[str] = []
    for schema_name, entity in entities.items():
        if ocf_mapping and schema_name not in ocf_mapping:
            missing_ocf.append(schema_name)
        page = render_entity_page(entity, schemas[schema_name], ocf_mapping)
        out = DOMAIN_DIR / f"{entity.sanitized}.md"
        out.write_text(page)
        print(f"  {out.relative_to(ROOT)}")

    # Write hub pages
    for hub_name, renderer in (
        ("transaction", render_transaction_hub),
        ("stakeholder", render_stakeholder_hub),
        ("compensation_benchmarks", render_benchmarks_hub),
    ):
        out = DOMAIN_DIR / f"{hub_name}.md"
        out.write_text(renderer(ocf_mapping))
        print(f"  {out.relative_to(ROOT)}")

    if missing_ocf:
        print("\nNo OCF mapping entry for:")
        for n in missing_ocf:
            print(f"  - {n}")

    # Write index
    index_out = DOMAIN_DIR / "index.md"
    index_out.write_text(render_index(entities, schemas))
    print(f"  {index_out.relative_to(ROOT)}")

    # Sanity warnings: flag domain schemas we found but didn't categorize
    all_found = set(domain_endpoints.keys()) - hub_members
    uncategorized = all_found - set(categorized_schemas)
    # Also exclude things that look like primitives / metadata false positives
    uncategorized = {
        n
        for n in uncategorized
        if not n.startswith("v1alpha1Iso")
        and n
        not in {
            "v1alpha1OptionExerciseMoneyMovement",
            "v1alpha1OptionExerciseTaxWithholdingLineItem",
        }
    }
    if uncategorized:
        print("\nUncategorized domain schemas (consider adding to CATEGORIES):")
        for n in sorted(uncategorized):
            print(f"  - {n}")

    print(f"\nDone. Domain docs in {DOMAIN_DIR.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
