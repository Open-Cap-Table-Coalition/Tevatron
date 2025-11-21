# Cartevatron

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

This will:
1. Parse `carta-issuer-api.openapi.json`
2. Generate markdown files in `docs/objects/` (primary API resources) and `docs/types/` (supporting types)
3. Update the index in `docs/README.md`

### View Documentation

After generation, browse the documentation starting at `docs/README.md`.

## Scripts

### `generate_docs.py`

**Main documentation generator** - Converts OpenAPI schemas to markdown.

**Features:**
- Enum value rendering (30 enum schemas)
- Example data display (64 schemas with examples)
- Validation constraints (pattern, format, min/max)
- Title fallback for missing descriptions
- Automatic cross-linking between schemas

**Output Structure:**
```
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

Located in `ocf_examples/generate-docs/`, this is an advanced two-stage documentation system for OCF schemas:

```bash
cd ocf_examples/generate-docs
npx tsx index-two-stage.ts
```

**Note:** Requires specific directory structures (`schema/`, `samples/`, `docs/supplemental/`) not present in the repository root.

## Project Structure

```
/
├── carta-issuer-api.openapi.json   # OpenAPI 3.0 specification
├── generate_docs.py                # Python doc generator
├── schemas/                        # Individual schema definitions
│   ├── GET/                       # Response schemas
│   └── POST/                      # Request body schemas
├── docs/                          # Generated documentation
│   ├── README.md                  # Auto-generated index
│   ├── objects/                   # Primary API objects
│   └── types/                     # Supporting types
└── ocf_examples/                  # TypeScript documentation tools
    └── generate-docs/             # Two-stage doc generator
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
   # Edit generate_docs.py
   ```

2. **Test your changes:**
   ```bash
   # Clean existing docs
   rm -rf docs/objects docs/types

   # Regenerate
   python generate_docs.py

   # Verify output
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

**When modifying `generate_docs.py`:**

- Maintain the separation of concerns:
  - `sanitize_name()` - Schema name normalization
  - `classify_and_map_schemas()` - Object vs. type classification
  - `generate_markdown_for_schema()` - Markdown generation
  - `format_type()` - Type representation with links

- Preserve existing features:
  - Cross-reference links (use relative paths)
  - Required field marking
  - Property sorting (alphabetical)
  - Constraint display (pattern, format, lengths, min/max)

- Add tests for new schema patterns you encounter

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
