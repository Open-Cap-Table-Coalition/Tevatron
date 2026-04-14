# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains the Carta Issuer API specification and documentation generation tools. The project serves two main purposes:

1. **API Specification**: Contains the OpenAPI 3.0 specification for the Carta Issuer API (`carta-issuer-api.openapi.json`)
2. **Documentation Generation**: Provides tools to generate markdown documentation from the API specification

## Primary Commands

### Python Documentation Generator (Two-Stage Pipeline)

Generate documentation from the OpenAPI specification:

```bash
python generate_docs.py              # Run both stages
python generate_docs.py --stage1     # Run only Stage 1 (composition)
python generate_docs.py --stage2     # Run only Stage 2 (markdown generation)
```

**Two-Stage Process:**

1. **Stage 1 (Schema Composition)**:
   - Parses `carta-issuer-api.openapi.json`
   - Classifies schemas as "objects" (with endpoints) or "types" (supporting types)
   - Builds cross-reference graph between schemas
   - Writes enriched schemas to `build/composed-schemas/`

2. **Stage 2 (Markdown Generation)**:
   - Reads composed schemas from `build/composed-schemas/`
   - Generates markdown files in `docs/objects/` and `docs/types/`
   - Updates the index in `docs/README.md`

**Benefits of Two-Stage Approach:**
- Intermediate schemas can be inspected for debugging
- Stages can be run independently for faster iteration
- Clear separation between data processing and presentation
- Easier to add supplemental content between stages

### TypeScript Generator (OCF Examples - Reference Implementation)

Located in `ocf_examples/generate-docs/`, this is a reference implementation showing the two-stage pattern for OCF schemas:

```bash
cd ocf_examples/generate-docs
npx tsx index-two-stage.ts
```

**Note:** This TypeScript tool is provided as an architectural example and is not used for the Carta API spec. It demonstrates the two-stage pattern with `allOf` resolution and property inheritance.

## Architecture

### Python Documentation Generator (Two-Stage Pipeline)

The documentation generator uses a two-stage architecture inspired by the OCF TypeScript generator, separating data processing from presentation.

#### Stage 1: Schema Composition (`schema_composer.py`)

**Purpose:** Extract and enrich schemas from the OpenAPI spec with metadata needed for documentation.

**Key Classes:**
- `SchemaComposer`: Main orchestrator for schema composition
- `ComposedSchema`: Data class representing an enriched schema with metadata
- `EndpointInfo`: Data class for endpoint information

**Process:**
1. Load OpenAPI spec JSON
2. Extract all schemas from `components.schemas`
3. Classify schemas by analyzing API paths:
   - **Objects**: Schemas used in GET responses or POST request bodies
   - **Types**: Supporting schemas referenced by objects
4. Build cross-reference graph (what references what)
5. Compose each schema with:
   - Original schema definition
   - Endpoint information (method + path)
   - Classification (object vs type)
   - References and referenced_by lists
   - Output path for markdown file
6. Write composed schemas as JSON to `build/composed-schemas/`

**Key Methods:**
- `_sanitize_name()`: Converts `v1alpha1MyThing` → `my_thing`
- `_classify_schemas()`: Identifies primary objects vs supporting types
- `_build_reference_graph()`: Maps schema dependencies
- `_compose_schema()`: Creates enriched `ComposedSchema` objects

#### Stage 2: Markdown Generation (`markdown_generator.py`)

**Purpose:** Generate markdown documentation from composed schemas.

**Key Classes:**
- `MarkdownGenerator`: Main orchestrator for markdown generation
- `ComposedSchemaData`: Data class for loading composed schemas

**Process:**
1. Load composed schemas from `build/composed-schemas/`
2. For each schema, generate markdown with:
   - Title (sanitized name)
   - Endpoints (for objects)
   - Description (with title fallback)
   - Examples (JSON format)
   - Enum values (for enum schemas)
   - Properties table with:
     - Type (with cross-reference links)
     - Description
     - Constraints (pattern, format, min/max)
     - Required indicator
3. Write markdown files to `docs/objects/` or `docs/types/`
4. Generate index in `docs/README.md`

**Key Methods:**
- `_generate_schema_markdown()`: Creates markdown for a single schema
- `_generate_properties_table()`: Builds property table with constraints
- `_extract_constraints()`: Pulls validation rules from schema
- `_format_type()`: Creates type strings with cross-reference links
- `_create_schema_link()`: Generates relative markdown links

#### Main Orchestrator (`generate_docs.py`)

**Purpose:** Coordinate the two-stage pipeline with CLI interface.

**Features:**
- Run both stages sequentially
- Run Stage 1 only (`--stage1`)
- Run Stage 2 only (`--stage2`)
- Command-line argument parsing
- Error handling and user feedback

**Data Flow:**
```
carta-issuer-api.openapi.json
         ↓
    [Stage 1: Schema Composition]
         ↓
build/composed-schemas/*.json
         ↓
    [Stage 2: Markdown Generation]
         ↓
docs/objects/*.md + docs/types/*.md
```

**Features:**
- ✅ Enum value rendering (30 enum schemas)
- ✅ Example data display (64 schemas with examples)
- ✅ Validation constraints (145 properties with constraints)
- ✅ Title fallback for descriptions (12 schemas)
- ✅ Pattern, format, and length constraint display
- ✅ Cross-referenced links between schemas
- ✅ Intermediate schema output for debugging
- ✅ Independent stage execution

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
├── generate_docs.py                # Main orchestrator (two-stage pipeline)
├── schema_composer.py              # Stage 1: Schema composition
├── markdown_generator.py           # Stage 2: Markdown generation
├── schemas/                        # Individual schema definitions (reference)
│   ├── GET/                       # Response schemas
│   └── POST/                      # Request body schemas
├── build/                         # Generated intermediate files
│   └── composed-schemas/          # Stage 1 output
│       ├── _index.json            # Schema index
│       ├── corporation.json       # Composed schema with metadata
│       ├── decimal.json           # Composed schema with metadata
│       └── ...                    # One JSON file per schema
├── docs/                          # Generated documentation (Stage 2 output)
│   ├── README.md                  # Auto-generated index
│   ├── objects/                   # Primary API objects (with endpoints)
│   │   ├── corporation.md
│   │   ├── option_grant.md
│   │   └── ...
│   └── types/                     # Supporting types
│       ├── date.md
│       ├── decimal.md
│       └── ...
└── ocf_examples/                  # Reference implementation (not for Carta spec)
    └── generate-docs/             # TypeScript two-stage generator example
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

## Commit and PR Conventions

- Do **not** add `Co-Authored-By: Claude ...` trailers to commits
- Do **not** add "Generated with Claude Code" footers to PR descriptions
- Write commit messages and PR bodies as if authored solely by the user
