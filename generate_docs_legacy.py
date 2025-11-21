import json
import os
import re
from collections import defaultdict

# --- Configuration ---
INPUT_FILE = 'carta-issuer-api.openapi.json'
DOCS_DIR = 'docs'
OBJECTS_DIR = os.path.join(DOCS_DIR, 'objects')
TYPES_DIR = os.path.join(DOCS_DIR, 'types')
README_PATH = os.path.join(DOCS_DIR, 'README.md')
INDEX_PLACEHOLDER = '<!-- INDEX -->'

# --- Helper Functions ---

def sanitize_name(schema_name):
    """
    Converts a schema name like 'v1alpha1MyThing' to a clean 'my_thing'.
    """
    name = schema_name.split("v1alpha1")[-1]
    
    # Convert the remaining CamelCase string to snake_case
    snake_case_name = re.sub(r'(?<!^)(?=[A-Z])', '_', name).lstrip('_').lower()

    return snake_case_name if snake_case_name else schema_name.lower()

# --- Main Execution ---
def main():
    """
    Orchestrates the documentation generation process.
    """
    os.makedirs(OBJECTS_DIR, exist_ok=True)
    os.makedirs(TYPES_DIR, exist_ok=True)

    with open(INPUT_FILE, 'r') as f:
        spec = json.load(f)
    all_schemas = spec.get('components', {}).get('schemas', {})
    paths = spec.get('paths', {})

    primary_object_schemas, schema_to_doc_path = classify_and_map_schemas(paths, all_schemas)

    for schema_name, schema_def in all_schemas.items():
        doc_path = schema_to_doc_path.get(schema_name)
        if not doc_path:
            continue

        endpoint_info = primary_object_schemas.get(schema_name)
        markdown_content = generate_markdown_for_schema(
            schema_name, schema_def, endpoint_info, schema_to_doc_path
        )
        
        with open(doc_path, 'w') as f:
            f.write(markdown_content)

    generate_and_inject_index(schema_to_doc_path)

    print("Documentation generation complete.")
    print(f"Generated {len(schema_to_doc_path)} markdown files.")
    print(f"Updated index in '{README_PATH}'.")


def classify_and_map_schemas(paths, all_schemas):
    """
    Identifies primary vs. type schemas and maps all schemas to their future doc path.
    """
    primary_object_schemas = defaultdict(list)
    schema_to_doc_path = {}

    for path, methods in paths.items():
        for method, definition in methods.items():
            if method not in ['get', 'post']:
                continue
            
            schema_ref = None
            if method == 'get':
                response_ref = definition.get('responses', {}).get('200', {}).get('content', {}).get('application/json', {}).get('schema', {}).get('$ref')
                if response_ref:
                    wrapper_schema = all_schemas.get(response_ref.split('/')[-1], {})
                    for prop in wrapper_schema.get('properties', {}).values():
                        if prop.get('type') == 'array' and '$ref' in prop.get('items', {}):
                            schema_ref = prop['items']['$ref']
                            break
            elif method == 'post':
                schema_ref = definition.get('requestBody', {}).get('content', {}).get('application/json', {}).get('schema', {}).get('$ref')

            if schema_ref:
                schema_name = schema_ref.split('/')[-1]
                primary_object_schemas[schema_name].append({'method': method.upper(), 'path': path})

    for schema_name in all_schemas.keys():
        clean_name = sanitize_name(schema_name)
        if schema_name in primary_object_schemas:
            schema_to_doc_path[schema_name] = os.path.join(OBJECTS_DIR, f"{clean_name}.md")
        else:
            schema_to_doc_path[schema_name] = os.path.join(TYPES_DIR, f"{clean_name}.md")
            
    return primary_object_schemas, schema_to_doc_path

def generate_markdown_for_schema(schema_name, schema_def, endpoint_info_list, schema_to_doc_path):
    """
    Generates markdown content for a single schema.
    """
    title = sanitize_name(schema_name).replace('_', ' ').title()
    # Fallback to title if description is missing
    description = schema_def.get('description') or schema_def.get('title', 'No description available.')

    md_parts = [f"### {title}"]

    if endpoint_info_list:
        endpoints_str = ", ".join([f"`{info['method']} {info['path']}`" for info in endpoint_info_list])
        md_parts.append(f"**Endpoints:** {endpoints_str}")

    md_parts.append(f"**Description:** _{description}_")

    # Add example if present
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

    properties = schema_def.get('properties', {})
    required_props = schema_def.get('required', [])

    if not properties:
        md_parts.append("\n_No properties defined._")
    else:
        header = ["Property", "Type", "Description", "Required"]
        separator = ["---"] * len(header)
        table_rows = [header, separator]

        current_doc_path = schema_to_doc_path[schema_name]

        for prop_name, prop_schema in sorted(properties.items()):
            # Get property description and append constraints
            prop_desc = prop_schema.get('description', '').replace('\n', ' ')

            # Add constraints to description
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

            if constraints:
                constraint_text = " <br/>**Constraints:** " + ", ".join(constraints)
                prop_desc = (prop_desc + constraint_text) if prop_desc else constraint_text[6:]  # Skip leading <br/>

            prop_type_md = format_type(prop_schema, current_doc_path, schema_to_doc_path)
            is_required = '`REQUIRED`' if prop_name in required_props else '-'
            table_rows.append([f"`{prop_name}`", prop_type_md, prop_desc, is_required])
        
        markdown_rows = []
        for row in table_rows:
            formatted_row = f"| {' | '.join(row)} |"
            markdown_rows.append(formatted_row)
        md_table = "\n".join(markdown_rows)
        md_parts.append("**Properties:**\n" + md_table)

    return "\n\n".join(md_parts)

def format_type(prop_schema, current_doc_path, schema_to_doc_path):
    """
    Formats the property type, creating links for $ref types.
    """
    if '$ref' in prop_schema:
        ref_name = prop_schema['$ref'].split('/')[-1]
        target_doc_path = schema_to_doc_path.get(ref_name)
        if target_doc_path:
            relative_path = os.path.relpath(target_doc_path, os.path.dirname(current_doc_path))
            link_text = sanitize_name(ref_name).replace('_', ' ').title()
            return f"[{link_text}]({relative_path})"
        else:
            return f"`{sanitize_name(ref_name).title()}`"

    prop_type = prop_schema.get('type')
    if not prop_type:
        return '`ANY`'

    if prop_type == 'array':
        items = prop_schema.get('items', {})
        item_type_md = format_type(items, current_doc_path, schema_to_doc_path)
        return f"[`Array` of {item_type_md}]"
    
    return f"`{prop_type.upper()}`"

def generate_and_inject_index(schema_to_doc_path):
    """
    Generates a markdown index and injects it into the README file.
    """
    objects_md = ["\n#### Objects\n"]
    types_md = ["\n#### Types\n"]

    sorted_paths = sorted(schema_to_doc_path.items(), key=lambda item: sanitize_name(item[0]))

    for schema_name, doc_path in sorted_paths:
        title = sanitize_name(schema_name).replace('_', ' ').title()
        relative_path = os.path.relpath(doc_path, DOCS_DIR)
        link = f"- [{title}]({relative_path})"
        
        if doc_path.startswith(OBJECTS_DIR):
            objects_md.append(link)
        else:
            types_md.append(link)

    index_markdown = "\n".join(objects_md) + "\n" + "\n".join(types_md)

    with open(README_PATH, 'r') as f:
        readme_content = f.read()

    new_content = readme_content.replace(INDEX_PLACEHOLDER, index_markdown)

    with open(README_PATH, 'w') as f:
        f.write(new_content)

if __name__ == '__main__':
    print("--- SCRIPT EXECUTION STARTED ---")
    main()