"""
Stage 2: Markdown Generation

Reads composed schemas and generates markdown documentation files.
"""

import json
import os
from typing import Dict, List, Any, Optional
from dataclasses import dataclass


@dataclass
class ComposedSchemaData:
    """Data class for loading composed schemas from JSON."""
    name: str
    sanitized_name: str
    schema_type: str
    schema_def: Dict[str, Any]
    endpoints: List[Dict[str, str]]
    referenced_by: List[str]
    references: List[str]
    output_path: str


class MarkdownGenerator:
    """
    Stage 2: Generate markdown documentation from composed schemas.

    Reads composed schema JSON files and generates markdown documentation
    with examples, constraints, cross-references, and more.
    """

    def __init__(self, composed_schemas_dir: str):
        """
        Initialize the markdown generator.

        Args:
            composed_schemas_dir: Directory containing composed schema JSON files
        """
        self.schemas_dir = composed_schemas_dir
        self.schemas: Dict[str, ComposedSchemaData] = {}
        self.schema_to_path: Dict[str, str] = {}

    def generate(self, output_dir: str = 'docs'):
        """
        Generate all markdown documentation.

        Args:
            output_dir: Base directory for documentation output
        """
        # Load composed schemas
        self._load_schemas()

        # Create output directories
        objects_dir = os.path.join(output_dir, 'objects')
        types_dir = os.path.join(output_dir, 'types')
        os.makedirs(objects_dir, exist_ok=True)
        os.makedirs(types_dir, exist_ok=True)

        # Generate markdown for each schema
        for schema_name, schema_data in self.schemas.items():
            markdown = self._generate_schema_markdown(schema_data)

            # Write to file
            with open(schema_data.output_path, 'w') as f:
                f.write(markdown)

        # Generate index
        self._generate_index(output_dir)

        print(f"\n✓ Generated {len(self.schemas)} markdown files")

    def _load_schemas(self):
        """Load all composed schemas from JSON files."""
        # Load index
        index_path = os.path.join(self.schemas_dir, '_index.json')
        with open(index_path, 'r') as f:
            index = json.load(f)

        # Load each schema
        for schema_info in index['schemas']:
            file_path = os.path.join(
                self.schemas_dir,
                f"{schema_info['sanitized_name']}.json"
            )

            with open(file_path, 'r') as f:
                data = json.load(f)

            schema_data = ComposedSchemaData(**data)
            self.schemas[schema_data.name] = schema_data
            self.schema_to_path[schema_data.name] = schema_data.output_path

        print(f"✓ Loaded {len(self.schemas)} composed schemas")

    def _generate_schema_markdown(self, schema: ComposedSchemaData) -> str:
        """
        Generate markdown for a single schema.

        Args:
            schema: ComposedSchema data

        Returns:
            Markdown content as a string
        """
        schema_def = schema.schema_def
        md_parts = []

        # Title
        title = schema.sanitized_name.replace('_', ' ').title()
        md_parts.append(f"### {title}")

        # Endpoints (for objects)
        if schema.endpoints:
            endpoints_str = ", ".join([
                f"`{ep['method']} {ep['path']}`"
                for ep in schema.endpoints
            ])
            md_parts.append(f"**Endpoints:** {endpoints_str}")

        # Description (with title fallback)
        description = schema_def.get('description') or schema_def.get('title', 'No description available.')
        md_parts.append(f"**Description:** _{description}_")

        # Example
        if 'example' in schema_def:
            example_json = json.dumps(schema_def['example'], indent=2)
            md_parts.append(f"**Example:**\n```json\n{example_json}\n```")

        # Handle enum schemas
        if 'enum' in schema_def:
            enum_values = schema_def['enum']
            enum_type = schema_def.get('type', 'string').upper()
            enum_list = "\n".join([f"- `{val}`" for val in enum_values])
            md_parts.append(f"**Type:** `{enum_type}`\n\n**Allowed Values:**\n{enum_list}")
            return "\n\n".join(md_parts)

        # Properties table
        properties = schema_def.get('properties', {})
        required_props = schema_def.get('required', [])

        if not properties:
            md_parts.append("\n_No properties defined._")
        else:
            md_parts.append(self._generate_properties_table(
                properties,
                required_props,
                schema.output_path
            ))

        return "\n\n".join(md_parts)

    def _generate_properties_table(
        self,
        properties: Dict[str, Any],
        required_props: List[str],
        current_doc_path: str
    ) -> str:
        """
        Generate a markdown table for schema properties.

        Args:
            properties: Property definitions
            required_props: List of required property names
            current_doc_path: Path to current doc (for relative links)

        Returns:
            Markdown table as a string
        """
        header = ["Property", "Type", "Description", "Required"]
        separator = ["---"] * len(header)
        table_rows = [header, separator]

        for prop_name, prop_schema in sorted(properties.items()):
            # Get description
            prop_desc = prop_schema.get('description', '').replace('\n', ' ')

            # Add constraints
            constraints = self._extract_constraints(prop_schema)
            if constraints:
                constraint_text = " <br/>**Constraints:** " + ", ".join(constraints)
                prop_desc = (prop_desc + constraint_text) if prop_desc else constraint_text[6:]

            # Format type with links
            prop_type_md = self._format_type(prop_schema, current_doc_path)

            # Required indicator
            is_required = '`REQUIRED`' if prop_name in required_props else '-'

            table_rows.append([f"`{prop_name}`", prop_type_md, prop_desc, is_required])

        # Build markdown table
        markdown_rows = []
        for row in table_rows:
            formatted_row = f"| {' | '.join(row)} |"
            markdown_rows.append(formatted_row)

        return "**Properties:**\n" + "\n".join(markdown_rows)

    def _extract_constraints(self, prop_schema: Dict[str, Any]) -> List[str]:
        """
        Extract validation constraints from a property schema.

        Args:
            prop_schema: Property schema definition

        Returns:
            List of constraint strings
        """
        constraints = []

        if 'pattern' in prop_schema:
            constraints.append(f"Pattern: `{prop_schema['pattern']}`")
        if 'format' in prop_schema:
            constraints.append(f"Format: `{prop_schema['format']}`")
        if 'minLength' in prop_schema:
            constraints.append(f"Min length: {prop_schema['minLength']}")
        if 'maxLength' in prop_schema:
            constraints.append(f"Max length: {prop_schema['maxLength']}")
        if 'minimum' in prop_schema:
            constraints.append(f"Min: {prop_schema['minimum']}")
        if 'maximum' in prop_schema:
            constraints.append(f"Max: {prop_schema['maximum']}")
        if 'enum' in prop_schema:
            enum_vals = ', '.join([f"`{v}`" for v in prop_schema['enum'][:3]])
            if len(prop_schema['enum']) > 3:
                enum_vals += f", ... ({len(prop_schema['enum'])} total)"
            constraints.append(f"Enum: {enum_vals}")

        return constraints

    def _format_type(self, prop_schema: Dict[str, Any], current_doc_path: str) -> str:
        """
        Format property type with links to referenced schemas.

        Args:
            prop_schema: Property schema definition
            current_doc_path: Path to current doc (for relative links)

        Returns:
            Formatted type string with markdown links
        """
        # Handle $ref
        if '$ref' in prop_schema:
            ref_name = prop_schema['$ref'].split('/')[-1]
            return self._create_schema_link(ref_name, current_doc_path)

        # Handle basic types
        prop_type = prop_schema.get('type')
        if not prop_type:
            return '`ANY`'

        # Handle arrays
        if prop_type == 'array':
            items = prop_schema.get('items', {})
            item_type_md = self._format_type(items, current_doc_path)
            return f"[`Array` of {item_type_md}]"

        return f"`{prop_type.upper()}`"

    def _create_schema_link(self, ref_name: str, current_doc_path: str) -> str:
        """
        Create a markdown link to another schema.

        Args:
            ref_name: Referenced schema name
            current_doc_path: Current document path (for relative links)

        Returns:
            Markdown link string
        """
        target_doc_path = self.schema_to_path.get(ref_name)

        if target_doc_path:
            # Calculate relative path
            relative_path = os.path.relpath(
                target_doc_path,
                os.path.dirname(current_doc_path)
            )

            # Create link text
            schema_data = self.schemas.get(ref_name)
            if schema_data:
                link_text = schema_data.sanitized_name.replace('_', ' ').title()
            else:
                link_text = ref_name

            return f"[{link_text}]({relative_path})"
        else:
            # Fallback if schema not found
            return f"`{ref_name}`"

    def _generate_index(self, output_dir: str):
        """
        Generate the README index file.

        Args:
            output_dir: Output directory for documentation
        """
        readme_path = os.path.join(output_dir, 'README.md')

        # Separate objects and types
        objects = []
        types = []

        for schema in sorted(self.schemas.values(), key=lambda s: s.sanitized_name):
            title = schema.sanitized_name.replace('_', ' ').title()
            relative_path = os.path.relpath(schema.output_path, output_dir)
            link = f"- [{title}]({relative_path})"

            if schema.schema_type == "object":
                objects.append(link)
            else:
                types.append(link)

        # Build index markdown
        index_parts = [
            "# Carta API Schema Documentation",
            "",
            "This directory contains documentation for the JSON schemas used in the Carta API. "
            "The documentation is auto-generated from the OpenAPI specification.",
            "",
            "## Schema Index",
            "",
            "#### Objects",
            ""
        ]
        index_parts.extend(objects)
        index_parts.extend(["", "#### Types", ""])
        index_parts.extend(types)
        index_parts.extend(["", "---", "_This documentation is auto-generated._", ""])

        with open(readme_path, 'w') as f:
            f.write("\n".join(index_parts))

        print(f"✓ Generated index: {readme_path}")


def main():
    """Run Stage 2: Generate markdown from composed schemas."""
    print("=" * 80)
    print("STAGE 2: MARKDOWN GENERATION")
    print("=" * 80)

    generator = MarkdownGenerator('build/composed-schemas')
    generator.generate('docs')

    print("\n" + "=" * 80)
    print("STAGE 2 COMPLETE")
    print("=" * 80)


if __name__ == '__main__':
    main()
