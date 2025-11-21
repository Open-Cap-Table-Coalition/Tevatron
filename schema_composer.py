"""
Stage 1: Schema Composition

Reads the OpenAPI specification and produces enriched schema objects
with all metadata needed for documentation generation.
"""

import json
import os
from dataclasses import dataclass, asdict
from typing import Dict, List, Optional, Any
from collections import defaultdict


@dataclass
class EndpointInfo:
    """Information about an API endpoint."""
    method: str  # GET, POST, etc.
    path: str    # /v1alpha1/corporations


@dataclass
class ComposedSchema:
    """
    A fully composed schema with all metadata needed for documentation.
    """
    # Identity
    name: str                           # Schema name from OpenAPI (e.g., v1alpha1Corporation)
    sanitized_name: str                # Clean name (e.g., corporation)

    # Classification
    schema_type: str                   # "object" or "type"

    # Schema definition
    schema_def: Dict[str, Any]         # Original schema from OpenAPI

    # Endpoints (for objects only)
    endpoints: List[EndpointInfo]      # List of endpoints using this schema

    # Cross-references
    referenced_by: List[str]           # Schemas that reference this one
    references: List[str]              # Schemas this one references

    # Documentation path
    output_path: str                   # Where to write the markdown file


class SchemaComposer:
    """
    Stage 1: Compose schemas from OpenAPI specification.

    Reads the OpenAPI spec and produces enriched ComposedSchema objects
    with endpoint information, cross-references, and classification.
    """

    def __init__(self, openapi_spec_path: str):
        """
        Initialize the composer with an OpenAPI specification.

        Args:
            openapi_spec_path: Path to the OpenAPI JSON file
        """
        self.spec_path = openapi_spec_path
        self.spec = None
        self.schemas = {}
        self.composed_schemas = {}

    def compose(self) -> Dict[str, ComposedSchema]:
        """
        Compose all schemas from the OpenAPI specification.

        Returns:
            Dictionary mapping schema names to ComposedSchema objects
        """
        # Load spec
        self._load_spec()

        # Extract schemas
        self.schemas = self.spec.get('components', {}).get('schemas', {})

        # Classify schemas (object vs type)
        primary_objects = self._classify_schemas()

        # Build cross-reference graph
        references = self._build_reference_graph()

        # Compose each schema
        for schema_name, schema_def in self.schemas.items():
            composed = self._compose_schema(
                schema_name,
                schema_def,
                primary_objects.get(schema_name, []),
                references
            )
            self.composed_schemas[schema_name] = composed

        return self.composed_schemas

    def _load_spec(self):
        """Load the OpenAPI specification from disk."""
        with open(self.spec_path, 'r') as f:
            self.spec = json.load(f)

    def _classify_schemas(self) -> Dict[str, List[EndpointInfo]]:
        """
        Classify schemas as primary objects (with endpoints) or supporting types.

        Returns:
            Dictionary mapping primary object schema names to their endpoints
        """
        primary_objects = defaultdict(list)
        paths = self.spec.get('paths', {})

        for path, methods in paths.items():
            for method, definition in methods.items():
                if method not in ['get', 'post']:
                    continue

                schema_name = None

                if method == 'get':
                    # Extract from response
                    response_ref = (definition.get('responses', {})
                                   .get('200', {})
                                   .get('content', {})
                                   .get('application/json', {})
                                   .get('schema', {})
                                   .get('$ref'))

                    if response_ref:
                        wrapper_schema_name = response_ref.split('/')[-1]
                        wrapper_schema = self.schemas.get(wrapper_schema_name, {})

                        # Look for array items in response wrapper
                        for prop in wrapper_schema.get('properties', {}).values():
                            if prop.get('type') == 'array' and '$ref' in prop.get('items', {}):
                                schema_name = prop['items']['$ref'].split('/')[-1]
                                break

                elif method == 'post':
                    # Extract from request body
                    schema_ref = (definition.get('requestBody', {})
                                 .get('content', {})
                                 .get('application/json', {})
                                 .get('schema', {})
                                 .get('$ref'))

                    if schema_ref:
                        schema_name = schema_ref.split('/')[-1]

                if schema_name:
                    primary_objects[schema_name].append(
                        EndpointInfo(method=method.upper(), path=path)
                    )

        return primary_objects

    def _build_reference_graph(self) -> Dict[str, Dict[str, List[str]]]:
        """
        Build a graph of schema references.

        Returns:
            Dictionary with 'references' and 'referenced_by' for each schema
        """
        graph = {
            schema_name: {'references': [], 'referenced_by': []}
            for schema_name in self.schemas.keys()
        }

        # Find all $ref usages
        for schema_name, schema_def in self.schemas.items():
            refs = self._find_refs_in_schema(schema_def)
            graph[schema_name]['references'] = refs

            # Update referenced_by for each referenced schema
            for ref in refs:
                if ref in graph:
                    graph[ref]['referenced_by'].append(schema_name)

        return graph

    def _find_refs_in_schema(self, obj: Any, refs: Optional[List[str]] = None) -> List[str]:
        """
        Recursively find all $ref values in a schema object.

        Args:
            obj: Schema object to search
            refs: Accumulated list of references

        Returns:
            List of referenced schema names
        """
        if refs is None:
            refs = []

        if isinstance(obj, dict):
            if '$ref' in obj:
                ref_name = obj['$ref'].split('/')[-1]
                if ref_name not in refs:
                    refs.append(ref_name)

            for value in obj.values():
                self._find_refs_in_schema(value, refs)

        elif isinstance(obj, list):
            for item in obj:
                self._find_refs_in_schema(item, refs)

        return refs

    def _compose_schema(
        self,
        schema_name: str,
        schema_def: Dict[str, Any],
        endpoints: List[EndpointInfo],
        references: Dict[str, Dict[str, List[str]]]
    ) -> ComposedSchema:
        """
        Compose a single schema with all metadata.

        Args:
            schema_name: Name of the schema
            schema_def: Schema definition from OpenAPI
            endpoints: List of endpoints using this schema
            references: Cross-reference graph

        Returns:
            ComposedSchema object
        """
        sanitized_name = self._sanitize_name(schema_name)

        # Determine schema type
        schema_type = "object" if endpoints else "type"

        # Determine output path
        subdir = "objects" if schema_type == "object" else "types"
        output_path = os.path.join("docs", subdir, f"{sanitized_name}.md")

        return ComposedSchema(
            name=schema_name,
            sanitized_name=sanitized_name,
            schema_type=schema_type,
            schema_def=schema_def,
            endpoints=endpoints,
            referenced_by=references.get(schema_name, {}).get('referenced_by', []),
            references=references.get(schema_name, {}).get('references', []),
            output_path=output_path
        )

    @staticmethod
    def _sanitize_name(schema_name: str) -> str:
        """
        Convert schema name to human-readable snake_case, preserving namespace context.

        Examples:
            v1alpha1MyThing -> my_thing
            issuerscapitalizationv1alpha1Stakeholder -> issuers_capitalization_stakeholder
            publicapiissuersv1alpha1Stakeholder -> publicapi_issuers_stakeholder
        """
        import re

        # Split on v1alpha1 to separate namespace from schema name
        parts = schema_name.split("v1alpha1")

        if len(parts) == 2 and parts[0]:
            # Has a namespace prefix (e.g., issuerscapitalization)
            namespace = parts[0]
            schema = parts[1]

            # Convert both to snake_case
            namespace_snake = re.sub(r'(?<!^)(?=[A-Z])', '_', namespace).lower()
            schema_snake = re.sub(r'(?<!^)(?=[A-Z])', '_', schema).lstrip('_').lower()

            # Combine with underscore
            return f"{namespace_snake}_{schema_snake}"
        else:
            # No namespace, just convert the schema name
            name = parts[-1] if parts else schema_name
            snake_case_name = re.sub(r'(?<!^)(?=[A-Z])', '_', name).lstrip('_').lower()
            return snake_case_name if snake_case_name else schema_name.lower()

    def write_composed_schemas(self, output_dir: str):
        """
        Write composed schemas to disk as JSON files.

        Args:
            output_dir: Directory to write composed schema JSON files
        """
        os.makedirs(output_dir, exist_ok=True)

        # Write individual schema files
        for schema_name, composed in self.composed_schemas.items():
            file_path = os.path.join(output_dir, f"{composed.sanitized_name}.json")

            # Convert to dict
            schema_dict = asdict(composed)

            with open(file_path, 'w') as f:
                json.dump(schema_dict, f, indent=2)

        # Write index file
        index_path = os.path.join(output_dir, "_index.json")
        index = {
            "total_schemas": len(self.composed_schemas),
            "objects": sum(1 for s in self.composed_schemas.values() if s.schema_type == "object"),
            "types": sum(1 for s in self.composed_schemas.values() if s.schema_type == "type"),
            "schemas": [
                {
                    "name": s.name,
                    "sanitized_name": s.sanitized_name,
                    "type": s.schema_type,
                    "output_path": s.output_path
                }
                for s in self.composed_schemas.values()
            ]
        }

        with open(index_path, 'w') as f:
            json.dump(index, f, indent=2)

        print(f"Wrote {len(self.composed_schemas)} composed schemas to {output_dir}")


def main():
    """Run Stage 1: Compose schemas from OpenAPI spec."""
    print("=" * 80)
    print("STAGE 1: SCHEMA COMPOSITION")
    print("=" * 80)

    composer = SchemaComposer('carta-issuer-api.openapi.json')
    composed_schemas = composer.compose()

    print(f"\n✓ Composed {len(composed_schemas)} schemas")
    print(f"  - Objects: {sum(1 for s in composed_schemas.values() if s.schema_type == 'object')}")
    print(f"  - Types: {sum(1 for s in composed_schemas.values() if s.schema_type == 'type')}")

    # Write to build directory
    output_dir = 'build/composed-schemas'
    composer.write_composed_schemas(output_dir)
    print(f"\n✓ Wrote composed schemas to: {output_dir}")

    print("\n" + "=" * 80)
    print("STAGE 1 COMPLETE")
    print("=" * 80)


if __name__ == '__main__':
    main()
