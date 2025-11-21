#!/usr/bin/env python3
"""
Two-Stage Documentation Generator for Carta Issuer API

Stage 1: Schema Composition - Extracts and enriches schemas from OpenAPI spec
Stage 2: Markdown Generation - Generates documentation from composed schemas

Usage:
    python generate_docs.py              # Run both stages
    python generate_docs.py --stage1     # Run only stage 1
    python generate_docs.py --stage2     # Run only stage 2
"""

import argparse
import sys
from schema_composer import SchemaComposer
from markdown_generator import MarkdownGenerator


def run_stage1(spec_path: str = 'carta-issuer-api.openapi.json',
               output_dir: str = 'build/composed-schemas'):
    """
    Run Stage 1: Compose schemas from OpenAPI specification.

    Args:
        spec_path: Path to OpenAPI JSON file
        output_dir: Directory for composed schema output
    """
    print("=" * 80)
    print("STAGE 1: SCHEMA COMPOSITION")
    print("=" * 80)
    print()

    composer = SchemaComposer(spec_path)
    composed_schemas = composer.compose()

    print(f"✓ Composed {len(composed_schemas)} schemas")
    print(f"  - Objects: {sum(1 for s in composed_schemas.values() if s.schema_type == 'object')}")
    print(f"  - Types: {sum(1 for s in composed_schemas.values() if s.schema_type == 'type')}")

    composer.write_composed_schemas(output_dir)

    print()
    print("=" * 80)
    print("STAGE 1 COMPLETE")
    print("=" * 80)
    print()


def run_stage2(schemas_dir: str = 'build/composed-schemas',
               output_dir: str = 'docs'):
    """
    Run Stage 2: Generate markdown from composed schemas.

    Args:
        schemas_dir: Directory containing composed schemas
        output_dir: Directory for markdown output
    """
    print("=" * 80)
    print("STAGE 2: MARKDOWN GENERATION")
    print("=" * 80)
    print()

    generator = MarkdownGenerator(schemas_dir)
    generator.generate(output_dir)

    print()
    print("=" * 80)
    print("STAGE 2 COMPLETE")
    print("=" * 80)
    print()


def main():
    """Main entry point for the two-stage documentation generator."""
    parser = argparse.ArgumentParser(
        description='Generate documentation from Carta Issuer API OpenAPI spec',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python generate_docs.py              # Run both stages
  python generate_docs.py --stage1     # Run only stage 1 (composition)
  python generate_docs.py --stage2     # Run only stage 2 (markdown generation)

Two-Stage Pipeline:
  Stage 1 reads the OpenAPI spec and produces enriched schema objects with
  endpoint info, cross-references, and metadata in build/composed-schemas/

  Stage 2 reads the composed schemas and generates markdown documentation
  in docs/objects/ and docs/types/
        """
    )

    parser.add_argument(
        '--stage1',
        action='store_true',
        help='Run only Stage 1 (schema composition)'
    )

    parser.add_argument(
        '--stage2',
        action='store_true',
        help='Run only Stage 2 (markdown generation)'
    )

    parser.add_argument(
        '--spec',
        default='carta-issuer-api.openapi.json',
        help='Path to OpenAPI specification (default: carta-issuer-api.openapi.json)'
    )

    args = parser.parse_args()

    # Determine which stages to run
    run_both = not (args.stage1 or args.stage2)

    try:
        if args.stage1 or run_both:
            run_stage1(spec_path=args.spec)

        if args.stage2 or run_both:
            run_stage2()

        if run_both:
            print()
            print("=" * 80)
            print("DOCUMENTATION GENERATION COMPLETE")
            print("=" * 80)
            print()
            print("Generated documentation is available in:")
            print("  - docs/objects/  (Primary API resources)")
            print("  - docs/types/    (Supporting types)")
            print("  - docs/README.md (Index)")
            print()

    except FileNotFoundError as e:
        print(f"\n❌ Error: {e}", file=sys.stderr)
        print("\nMake sure you're running from the repository root.", file=sys.stderr)
        sys.exit(1)

    except Exception as e:
        print(f"\n❌ Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
