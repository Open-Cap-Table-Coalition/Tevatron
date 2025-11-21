# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains the Carta Issuer API specification and documentation generation tools. The project serves two main purposes:

1. **API Specification**: Contains the OpenAPI 3.0 specification for the Carta Issuer API (`carta-issuer-api.openapi.json`)
2. **Documentation Generation**: Provides tools to generate markdown documentation from the API specification

## Primary Commands

### Python Documentation Generator

Generate documentation from the OpenAPI specification:

```bash
python generate_docs.py
```

This script:
- Parses `carta-issuer-api.openapi.json`
- Classifies schemas as either "objects" (primary resources with endpoints) or "types" (supporting types)
- Generates markdown files in `docs/objects/` and `docs/types/`
- Updates the index in `docs/README.md`

### TypeScript Two-Stage Documentation Generator (OCF Examples)

Located in `ocf_examples/generate-docs/`, this is a more sophisticated documentation generation system:

```bash
# Run from ocf_examples/generate-docs directory
npx tsx index-two-stage.ts
```

This performs a two-stage process:
1. **Stage 1**: Schema composition - resolves `allOf` references, merges properties, tracks inheritance
2. **Stage 2**: Markdown generation - creates documentation with examples and supplemental content

Note: This TypeScript tool expects specific directory structures (`schema/`, `samples/`, `docs/supplemental/`) that may not be present in the current repository root.

## Architecture

### Python Documentation Generator (`generate_docs.py`)

**Key Components**:

- `sanitize_name()`: Converts schema names (e.g., `v1alpha1MyThing`) to clean snake_case (e.g., `my_thing`)
- `classify_and_map_schemas()`: Distinguishes between:
  - **Primary objects**: Schemas returned by GET endpoints or accepted by POST endpoints (goes to `docs/objects/`)
  - **Types**: Supporting schemas referenced by objects (goes to `docs/types/`)
- `generate_markdown_for_schema()`: Creates markdown tables with property details, types, and required fields
  - Handles enum schemas with complete value listings
  - Displays schema examples in JSON format
  - Falls back to `title` field when `description` is missing
  - Shows validation constraints (pattern, format, min/max length, min/max value)
- `format_type()`: Generates type representations with relative links to referenced schemas

**Data Flow**:
1. Load OpenAPI spec JSON
2. Analyze paths to identify primary objects vs supporting types
3. Generate markdown for each schema with cross-references
4. Update `docs/README.md` with auto-generated index

**Features**:
- ✅ Enum value rendering (30 enum schemas)
- ✅ Example data display (64 schemas with examples)
- ✅ Validation constraints (145 properties with constraints)
- ✅ Title fallback for descriptions (12 schemas)
- ✅ Pattern, format, and length constraint display
- ✅ Cross-referenced links between schemas

### TypeScript OCF Documentation Generator

**Architecture** (two-stage pipeline):

**Stage 1 - Schema Composition** (`SchemaComposer`):
- Reads raw JSON schemas from disk
- Walks `allOf` inheritance chains recursively
- Merges properties from parent schemas (later definitions override earlier ones)
- Tracks property provenance (direct vs inherited)
- Detects compatibility wrappers (schemas with only `object_type` + single `allOf`)
- Outputs fully composed schemas with flattened property trees

**Stage 2 - Markdown Generation** (`MarkdownGenerator`):
- Takes composed schemas from Stage 1
- Integrates examples from `samples/` directory
- Integrates supplemental documentation from `docs/supplemental/`
- Generates markdown files with complete property documentation

**Key Classes**:
- `SchemaComposer`: Handles allOf resolution and property inheritance
- `ComposedSchemaNode`: Represents a fully composed schema with metadata
- `TwoStageDocGenerator`: Orchestrates the entire generation process
- `SchemaReader`: Reads schema files from filesystem
- `ExamplesReader`: Reads example JSON files
- `SupplementalsReader`: Reads supplemental markdown content

## Directory Structure

```
/
├── carta-issuer-api.openapi.json   # Main OpenAPI specification
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
        ├── Schema/                # Schema reading/parsing
        ├── SchemaComposer/        # Schema composition & markdown generation
        └── index-two-stage.ts     # Entry point
```

## API Structure

The Carta Issuer API is organized into several service areas:

- **Corporations**: Manage corporation information
- **Compensation Benchmarks**: Access compensation benchmark data
- **Securities**: Manage certificates, option grants, convertible notes, etc.
- **Draft Securities**: Work with draft securities before finalization
- **Capitalization Table**: Retrieve cap table data
- **Securities Templates**: Manage templates for creating securities
- **Issuers**: Manage issuer information
- **Interests**: Manage interests for an issuer

## Authentication

The API uses OAuth 2.0 for authentication. Required scopes are listed in the `security` section of each operation in the OpenAPI spec.

## Schema Naming Conventions

- API schemas follow the pattern: `v1alpha1<ResourceName>`
- Generated markdown files use snake_case: `v1alpha1_resource_name.md`
- Primary objects (with endpoints) are separated from supporting types
