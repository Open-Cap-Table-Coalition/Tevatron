# Tevatron

Documentation generator for the Carta Issuer API OpenAPI specification.

## Purpose

This project provides tools to generate comprehensive, human-readable documentation from the Carta Issuer API OpenAPI 3.0 specification. The documentation includes:

- Detailed schema descriptions with examples
- Property tables with types, descriptions, and validation constraints
- Enum value listings
- Cross-referenced links between related schemas
- Automatic categorization of objects vs. types

## Quick Start

### Generate Documentation

Run the Python documentation generator:

```bash
python generate_docs.py
```

This runs a two-stage pipeline:
1. **Stage 1:** Compose schemas from `carta-issuer-api.openapi.json` → `build/composed-schemas/`
2. **Stage 2:** Generate markdown from composed schemas → `docs/objects/` and `docs/types/`
3. Update the index in `docs/README.md`

You can also run stages independently:
```bash
python generate_docs.py --stage1  # Run only composition
python generate_docs.py --stage2  # Run only markdown generation
```

### View Documentation

After generation, browse the documentation starting at `docs/README.md`.

## Scripts

### `generate_docs.py` (Two-Stage Pipeline)

**Main documentation generator** - Uses a two-stage architecture to convert OpenAPI schemas to markdown.

**Architecture:**

**Stage 1: Schema Composition** (`schema_composer.py`)
- Reads `carta-issuer-api.openapi.json`
- Extracts and enriches schemas with metadata
- Classifies schemas as "objects" (with endpoints) or "types"
- Builds cross-reference graph
- Writes composed schemas to `build/composed-schemas/`

**Stage 2: Markdown Generation** (`markdown_generator.py`)
- Reads composed schemas from `build/composed-schemas/`
- Generates markdown documentation
- Writes to `docs/objects/` and `docs/types/`
- Creates index in `docs/README.md`

**Features:**
- ✅ Enum value rendering (30 enum schemas)
- ✅ Example data display (64 schemas with examples)
- ✅ Validation constraints (pattern, format, min/max)
- ✅ Title fallback for missing descriptions
- ✅ Automatic cross-linking between schemas
- ✅ Intermediate schema output for debugging
- ✅ Independent stage execution

**Output Structure:**
```
build/
└── composed-schemas/      # Stage 1 output (intermediate)
    ├── _index.json        # Schema index
    ├── corporation.json   # Composed schema with metadata
    └── ...

docs/
├── README.md              # Auto-generated index
├── objects/               # Primary API resources (with endpoints)
│   ├── corporation.md
│   ├── option_grant.md
│   └── ...
└── types/                 # Supporting types
    ├── date.md
    ├── decimal.md
    └── ...
```

### TypeScript Generator (OCF Examples)

Located in `ocf_examples/generate-docs/`, this is a reference implementation of the two-stage pattern for OCF schemas (provided as an example, not used for Carta API spec).

```bash
cd ocf_examples/generate-docs
npx tsx index-two-stage.ts
```

## Project Structure

```
/
├── carta-issuer-api.openapi.json   # OpenAPI 3.0 specification
├── generate_docs.py                # Main orchestrator (two-stage pipeline)
├── schema_composer.py              # Stage 1: Schema composition
├── markdown_generator.py           # Stage 2: Markdown generation
├── schemas/                        # Individual schema definitions (reference)
│   ├── GET/                       # Response schemas
│   └── POST/                      # Request body schemas
├── build/                         # Generated intermediate files
│   └── composed-schemas/          # Stage 1 output (enriched schemas)
├── docs/                          # Generated documentation
│   ├── README.md                  # Auto-generated index
│   ├── objects/                   # Primary API objects
│   └── types/                     # Supporting types
└── ocf_examples/                  # Reference implementation (two-stage pattern)
    └── generate-docs/             # TypeScript two-stage generator
```

## API Overview

The Carta Issuer API provides endpoints for:

- **Corporations** - Manage corporation information
- **Compensation Benchmarks** - Access compensation benchmark data
- **Securities** - Manage certificates, option grants, convertible notes, RSUs, RSAs
- **Draft Securities** - Work with draft securities before finalization
- **Capitalization Table** - Retrieve cap table data
- **Securities Templates** - Manage templates for creating securities
- **Issuers** - Manage issuer information
- **Interests** - Manage interests for an issuer

**Authentication:** OAuth 2.0 (scopes listed in each endpoint)

## Contributing as a Developer

### Prerequisites

- Python 3.7+ (for `generate_docs.py`)
- Node.js 18+ (for TypeScript tools, optional)

### Development Workflow

1. **Make changes to the generator:**
   ```bash
   # Edit schema_composer.py for Stage 1 changes
   # Edit markdown_generator.py for Stage 2 changes
   # Edit generate_docs.py for orchestration changes
   ```

2. **Test your changes:**
   ```bash
   # Clean existing outputs
   rm -rf build docs/objects docs/types

   # Regenerate (both stages)
   python generate_docs.py

   # Or test stages independently
   python generate_docs.py --stage1  # Test composition only
   python generate_docs.py --stage2  # Test markdown only

   # Inspect intermediate output
   cat build/composed-schemas/_index.json    # Check schema index
   cat build/composed-schemas/decimal.json   # Check composed schema

   # Verify final output
   cat docs/types/stakeholder_entity_type.md  # Check enum rendering
   cat docs/types/decimal.md                  # Check constraints
   cat docs/objects/option_grant.md           # Check examples
   ```

3. **Verify generated documentation:**
   - Check that all links work correctly
   - Verify enum values are displayed
   - Confirm examples are properly formatted
   - Ensure constraints are shown (pattern, format, min/max)

### Code Guidelines

**Two-Stage Architecture:**

The generator is split into two independent stages for modularity and debuggability:

**Stage 1: `schema_composer.py`**
- Reads OpenAPI spec and produces enriched schema objects
- Key classes:
  - `SchemaComposer` - Main composition orchestrator
  - `ComposedSchema` - Data class for enriched schemas
- Outputs: JSON files in `build/composed-schemas/`

**Stage 2: `markdown_generator.py`**
- Reads composed schemas and generates markdown
- Key classes:
  - `MarkdownGenerator` - Markdown generation orchestrator
- Outputs: Markdown files in `docs/objects/` and `docs/types/`

**When making changes:**

- Maintain separation between stages - Stage 2 should only depend on Stage 1 output
- Preserve the `ComposedSchema` data structure contract
- Keep cross-reference links working (relative paths)
- Maintain required field marking, property sorting, constraint display
- Test both stages independently after changes

### Testing Edge Cases

When making changes, test against these schema patterns:

```bash
# Enum schemas
python -c "import json; spec = json.load(open('carta-issuer-api.openapi.json'));
print([k for k,v in spec['components']['schemas'].items() if 'enum' in v][:3])"

# Schemas with examples
python -c "import json; spec = json.load(open('carta-issuer-api.openapi.json'));
print([k for k,v in spec['components']['schemas'].items() if 'example' in v][:3])"

# Properties with constraints
python -c "import json; spec = json.load(open('carta-issuer-api.openapi.json'));
[print(f'{k}.{p}') for k,v in spec['components']['schemas'].items()
if 'properties' in v for p,pv in v['properties'].items()
if 'pattern' in pv or 'format' in pv][:5]"
```

### Updating the OpenAPI Spec

If you update `carta-issuer-api.openapi.json`:

1. Validate the OpenAPI spec:
   ```bash
   # Use Swagger Editor or similar tool
   # https://editor.swagger.io/
   ```

2. Regenerate documentation:
   ```bash
   python generate_docs.py
   ```

3. Review the diff in `docs/` to ensure changes are correct

### Submitting Changes

1. Ensure documentation generates without errors
2. Verify sample output files look correct
3. Update `CLAUDE.md` if you change the architecture
4. Include before/after examples in your PR description

## Documentation

- `CLAUDE.md` - Detailed architecture guide for AI assistants
- `docs/README.md` - Auto-generated schema index

## License

Contact Carta - Developer Ecosystem Team (developers@carta.com)

## Support

For API-related questions, contact: developers@carta.com
