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

        # Generate interactive graph visualization
        self._generate_interactive_graph_html(output_dir)

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

    def _generate_schema_graph(self) -> str:
        """
        Generate a Mermaid diagram showing schema relationships.

        Returns:
            Mermaid diagram as a string
        """
        # Build graph focusing on objects and their immediate dependencies
        mermaid_lines = ["```mermaid", "graph TD"]

        # Get all object schemas (primary resources)
        object_schemas = [s for s in self.schemas.values() if s.schema_type == "object"]

        # Track which schemas to include (objects + their immediate references)
        included_schemas = set()
        for obj_schema in object_schemas:
            included_schemas.add(obj_schema.name)
            included_schemas.update(obj_schema.references)

        # Identify highly-used schemas (10+ references)
        reference_counts = {}
        for schema in self.schemas.values():
            reference_counts[schema.name] = len(schema.referenced_by)

        highly_used_threshold = 10
        highly_used_schemas = {name for name, count in reference_counts.items() if count >= highly_used_threshold}

        # Generate nodes with links
        for schema_name in included_schemas:
            schema = self.schemas.get(schema_name)
            if not schema:
                continue

            sanitized = schema.sanitized_name
            display_name = sanitized.replace('_', ' ').title()

            # Truncate long names for readability
            if len(display_name) > 30:
                display_name = display_name[:27] + "..."

            # Determine if schema is highly used
            is_highly_used = schema_name in highly_used_schemas

            # Different styling for objects vs types
            if schema.schema_type == "object":
                # Primary objects in bold boxes
                relative_path = os.path.relpath(schema.output_path, 'docs')
                mermaid_lines.append(f'    {sanitized}["{display_name}"]')
                class_list = "objectNode,highlyUsed" if is_highly_used else "objectNode"
                mermaid_lines.append(f'    class {sanitized} {class_list}')
                mermaid_lines.append(f'    click {sanitized} "{relative_path}"')
            else:
                # Types in rounded boxes
                relative_path = os.path.relpath(schema.output_path, 'docs')
                mermaid_lines.append(f'    {sanitized}("{display_name}")')
                class_list = "typeNode,highlyUsed" if is_highly_used else "typeNode"
                mermaid_lines.append(f'    class {sanitized} {class_list}')
                mermaid_lines.append(f'    click {sanitized} "{relative_path}"')

        # Generate edges (only from objects to their references)
        for obj_schema in object_schemas:
            from_name = obj_schema.sanitized_name
            for ref_name in obj_schema.references:
                ref_schema = self.schemas.get(ref_name)
                if ref_schema:
                    to_name = ref_schema.sanitized_name
                    mermaid_lines.append(f'    {from_name} --> {to_name}')

        # Add styling with enhancements
        mermaid_lines.extend([
            "",
            "    classDef objectNode fill:#e1f5ff,stroke:#01579b,stroke-width:3px,font-size:16px,font-weight:bold",
            "    classDef typeNode fill:#f3e5f5,stroke:#4a148c,stroke-width:1px",
            "    classDef highlyUsed fill:#fff9c4,stroke:#f57f17,stroke-width:3px,stroke-dasharray:5 5",
            "```"
        ])

        return "\n".join(mermaid_lines)

    def _generate_graph_data(self) -> Dict[str, Any]:
        """
        Generate graph data structure for D3.js visualization.

        Returns:
            Dictionary with nodes and links for D3.js force graph
        """
        nodes = []
        links = []

        # Create nodes
        for schema in self.schemas.values():
            node = {
                "id": schema.sanitized_name,
                "name": schema.sanitized_name.replace('_', ' ').title(),
                "type": schema.schema_type,
                "url": schema.output_path,
                "references_count": len(schema.references),
                "referenced_by_count": len(schema.referenced_by),
                "description": schema.schema_def.get('description',
                              schema.schema_def.get('title', ''))[:100]
            }

            # Add endpoint info for objects
            if schema.endpoints:
                node["endpoints"] = [
                    {"method": ep["method"], "path": ep["path"]}
                    for ep in schema.endpoints
                ]

            nodes.append(node)

        # Create links
        for schema in self.schemas.values():
            source_id = schema.sanitized_name
            for ref_name in schema.references:
                ref_schema = self.schemas.get(ref_name)
                if ref_schema:
                    target_id = ref_schema.sanitized_name
                    links.append({
                        "source": source_id,
                        "target": target_id
                    })

        return {
            "nodes": nodes,
            "links": links,
            "stats": {
                "total_schemas": len(nodes),
                "total_objects": sum(1 for n in nodes if n["type"] == "object"),
                "total_types": sum(1 for n in nodes if n["type"] == "type"),
                "total_relationships": len(links)
            }
        }

    def _generate_interactive_graph_html(self, output_dir: str):
        """
        Generate an interactive D3.js force-directed graph visualization.

        Args:
            output_dir: Output directory for the HTML file
        """
        graph_data = self._generate_graph_data()

        html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Carta API Schema Dependency Graph</title>
    <script src="https://d3js.org/d3.v7.min.js"></script>
    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
            background: #f5f5f5;
        }

        #container {
            display: flex;
            height: 100vh;
        }

        #graph {
            flex: 1;
            background: white;
            position: relative;
        }

        #sidebar {
            width: 300px;
            background: #2c3e50;
            color: white;
            padding: 20px;
            overflow-y: auto;
            box-shadow: -2px 0 10px rgba(0,0,0,0.1);
        }

        #sidebar h2 {
            margin-top: 0;
            color: #3498db;
        }

        #sidebar .stat {
            margin: 15px 0;
            padding: 10px;
            background: rgba(255,255,255,0.1);
            border-radius: 5px;
        }

        #sidebar .stat-label {
            font-size: 12px;
            color: #95a5a6;
            text-transform: uppercase;
        }

        #sidebar .stat-value {
            font-size: 24px;
            font-weight: bold;
            color: #3498db;
        }

        .controls {
            margin: 20px 0;
        }

        .controls button {
            width: 100%;
            padding: 10px;
            margin: 5px 0;
            background: #3498db;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 14px;
        }

        .controls button:hover {
            background: #2980b9;
        }

        .legend {
            margin-top: 20px;
        }

        .legend-item {
            display: flex;
            align-items: center;
            margin: 10px 0;
        }

        .legend-color {
            width: 20px;
            height: 20px;
            border-radius: 50%;
            margin-right: 10px;
            border: 2px solid white;
        }

        .tooltip {
            position: absolute;
            padding: 10px;
            background: rgba(0, 0, 0, 0.9);
            color: white;
            border-radius: 5px;
            pointer-events: none;
            font-size: 12px;
            max-width: 300px;
            z-index: 1000;
            display: none;
        }

        .tooltip h3 {
            margin: 0 0 5px 0;
            color: #3498db;
        }

        .tooltip .endpoint {
            background: rgba(52, 152, 219, 0.3);
            padding: 2px 6px;
            border-radius: 3px;
            margin: 2px 0;
            font-size: 11px;
        }

        .node {
            cursor: pointer;
            stroke: #fff;
            stroke-width: 2px;
        }

        .node:hover {
            stroke: #f39c12;
            stroke-width: 3px;
        }

        .link {
            stroke: #95a5a6;
            stroke-opacity: 0.3;
            stroke-width: 1.5px;
        }

        .node-label {
            font-size: 10px;
            pointer-events: none;
            text-anchor: middle;
            fill: #2c3e50;
            font-weight: 500;
        }

        #search {
            width: calc(100% - 20px);
            padding: 10px;
            margin-bottom: 15px;
            border: none;
            border-radius: 5px;
            font-size: 14px;
        }

        .highlighted {
            stroke: #f39c12;
            stroke-width: 4px;
        }
    </style>
</head>
<body>
    <div id="container">
        <div id="graph">
            <div class="tooltip" id="tooltip"></div>
        </div>
        <div id="sidebar">
            <h2>📊 Schema Graph</h2>

            <input type="text" id="search" placeholder="Search schemas...">

            <div class="stat">
                <div class="stat-label">Total Schemas</div>
                <div class="stat-value" id="total-schemas"></div>
            </div>

            <div class="stat">
                <div class="stat-label">API Objects</div>
                <div class="stat-value" id="total-objects"></div>
            </div>

            <div class="stat">
                <div class="stat-label">Supporting Types</div>
                <div class="stat-value" id="total-types"></div>
            </div>

            <div class="stat">
                <div class="stat-label">Relationships</div>
                <div class="stat-value" id="total-relationships"></div>
            </div>

            <div class="controls">
                <button onclick="resetZoom()">Reset View</button>
                <button onclick="centerGraph()">Center Graph</button>
                <button onclick="toggleLabels()">Toggle Labels</button>
            </div>

            <div class="legend">
                <h3>Legend</h3>
                <div class="legend-item">
                    <div class="legend-color" style="background: #3498db; width: 28px; height: 28px;"></div>
                    <span>API Objects (larger)</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color" style="background: #9b59b6;"></div>
                    <span>Supporting Types</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color" style="background: #e74c3c; box-shadow: 0 0 10px rgba(231, 76, 60, 0.8);"></div>
                    <span>Highly Referenced (10+ refs, glowing)</span>
                </div>
            </div>
        </div>
    </div>

    <script>
        // Graph data
        const graphData = """ + json.dumps(graph_data, indent=2) + """;

        // Set up dimensions
        const width = window.innerWidth - 300;
        const height = window.innerHeight;

        // Create SVG
        const svg = d3.select("#graph")
            .append("svg")
            .attr("width", width)
            .attr("height", height);

        // Add SVG filters for glow effect
        const defs = svg.append("defs");

        // Glow filter for highly-used schemas
        const glowFilter = defs.append("filter")
            .attr("id", "glow")
            .attr("x", "-50%")
            .attr("y", "-50%")
            .attr("width", "200%")
            .attr("height", "200%");

        glowFilter.append("feGaussianBlur")
            .attr("stdDeviation", "3")
            .attr("result", "coloredBlur");

        const feMerge = glowFilter.append("feMerge");
        feMerge.append("feMergeNode").attr("in", "coloredBlur");
        feMerge.append("feMergeNode").attr("in", "SourceGraphic");

        // Create a group for zoom/pan
        const g = svg.append("g");

        // Set up zoom behavior
        const zoom = d3.zoom()
            .scaleExtent([0.1, 4])
            .on("zoom", (event) => {
                g.attr("transform", event.transform);
            });

        svg.call(zoom);

        // Update stats
        d3.select("#total-schemas").text(graphData.stats.total_schemas);
        d3.select("#total-objects").text(graphData.stats.total_objects);
        d3.select("#total-types").text(graphData.stats.total_types);
        d3.select("#total-relationships").text(graphData.stats.total_relationships);

        // Create force simulation
        const simulation = d3.forceSimulation(graphData.nodes)
            .force("link", d3.forceLink(graphData.links)
                .id(d => d.id)
                .distance(100))
            .force("charge", d3.forceManyBody()
                .strength(-300))
            .force("center", d3.forceCenter(width / 2, height / 2))
            .force("collision", d3.forceCollide().radius(30));

        // Create links
        const link = g.append("g")
            .selectAll("line")
            .data(graphData.links)
            .join("line")
            .attr("class", "link");

        // Create nodes
        const node = g.append("g")
            .selectAll("circle")
            .data(graphData.nodes)
            .join("circle")
            .attr("class", "node")
            .attr("r", d => {
                // Objects are always larger than types
                // Types: 6-12 (scale by connectivity)
                // Objects: 16-26 (scale by connectivity, always larger)
                if (d.type === "object") {
                    const baseSize = 16;
                    const scale = Math.min(d.referenced_by_count * 1.5, 10);
                    return baseSize + scale;
                } else {
                    const baseSize = 6;
                    const scale = Math.min(d.referenced_by_count * 0.5, 6);
                    return baseSize + scale;
                }
            })
            .attr("fill", d => {
                // Color based on type and popularity
                if (d.referenced_by_count > 10) return "#e74c3c"; // Highly referenced
                if (d.type === "object") return "#3498db"; // API objects
                return "#9b59b6"; // Types
            })
            .attr("filter", d => {
                // Apply glow effect to highly-used schemas (10+ references)
                return d.referenced_by_count > 10 ? "url(#glow)" : null;
            })
            .call(d3.drag()
                .on("start", dragStarted)
                .on("drag", dragged)
                .on("end", dragEnded))
            .on("click", (event, d) => {
                window.open(d.url, "_blank");
            })
            .on("mouseover", showTooltip)
            .on("mouseout", hideTooltip);

        // Create labels
        const labels = g.append("g")
            .selectAll("text")
            .data(graphData.nodes)
            .join("text")
            .attr("class", "node-label")
            .text(d => {
                // Truncate long names
                const name = d.name;
                return name.length > 20 ? name.substring(0, 17) + "..." : name;
            })
            .attr("dy", -15);

        let labelsVisible = true;

        // Update positions on simulation tick
        simulation.on("tick", () => {
            link
                .attr("x1", d => d.source.x)
                .attr("y1", d => d.source.y)
                .attr("x2", d => d.target.x)
                .attr("y2", d => d.target.y);

            node
                .attr("cx", d => d.x)
                .attr("cy", d => d.y);

            labels
                .attr("x", d => d.x)
                .attr("y", d => d.y);
        });

        // Drag functions
        function dragStarted(event, d) {
            if (!event.active) simulation.alphaTarget(0.3).restart();
            d.fx = d.x;
            d.fy = d.y;
        }

        function dragged(event, d) {
            d.fx = event.x;
            d.fy = event.y;
        }

        function dragEnded(event, d) {
            if (!event.active) simulation.alphaTarget(0);
            d.fx = null;
            d.fy = null;
        }

        // Tooltip functions
        function showTooltip(event, d) {
            const tooltip = d3.select("#tooltip");

            let html = `<h3>${d.name}</h3>`;
            html += `<div><strong>Type:</strong> ${d.type}</div>`;
            html += `<div><strong>References:</strong> ${d.references_count}</div>`;
            html += `<div><strong>Referenced by:</strong> ${d.referenced_by_count}</div>`;

            if (d.description) {
                html += `<div style="margin-top: 5px; color: #95a5a6;">${d.description}</div>`;
            }

            if (d.endpoints) {
                html += `<div style="margin-top: 5px;"><strong>Endpoints:</strong></div>`;
                d.endpoints.forEach(ep => {
                    html += `<div class="endpoint">${ep.method} ${ep.path}</div>`;
                });
            }

            tooltip
                .html(html)
                .style("display", "block")
                .style("left", (event.pageX + 10) + "px")
                .style("top", (event.pageY - 10) + "px");
        }

        function hideTooltip() {
            d3.select("#tooltip").style("display", "none");
        }

        // Control functions
        function resetZoom() {
            svg.transition().duration(750).call(
                zoom.transform,
                d3.zoomIdentity
            );
        }

        function centerGraph() {
            const bounds = g.node().getBBox();
            const fullWidth = bounds.width;
            const fullHeight = bounds.height;
            const midX = bounds.x + fullWidth / 2;
            const midY = bounds.y + fullHeight / 2;

            const scale = 0.8 / Math.max(fullWidth / width, fullHeight / height);
            const translate = [width / 2 - scale * midX, height / 2 - scale * midY];

            svg.transition().duration(750).call(
                zoom.transform,
                d3.zoomIdentity.translate(translate[0], translate[1]).scale(scale)
            );
        }

        function toggleLabels() {
            labelsVisible = !labelsVisible;
            labels.style("display", labelsVisible ? "block" : "none");
        }

        // Search functionality
        d3.select("#search").on("input", function() {
            const searchTerm = this.value.toLowerCase();

            node.classed("highlighted", d => {
                const matches = d.name.toLowerCase().includes(searchTerm) ||
                               d.id.toLowerCase().includes(searchTerm);
                return matches && searchTerm.length > 0;
            });

            labels.style("font-weight", d => {
                const matches = d.name.toLowerCase().includes(searchTerm) ||
                               d.id.toLowerCase().includes(searchTerm);
                return (matches && searchTerm.length > 0) ? "bold" : "normal";
            });
        });

        // Initial center
        setTimeout(centerGraph, 100);
    </script>
</body>
</html>
"""

        # Write HTML file
        output_path = os.path.join(output_dir, 'schema-graph.html')
        with open(output_path, 'w') as f:
            f.write(html_content)

        print(f"✓ Generated interactive graph: {output_path}")

    def _generate_reference_stats(self) -> str:
        """
        Generate statistics about schema references.

        Returns:
            Markdown formatted statistics
        """
        stats_lines = []

        # Find most referenced schemas
        ref_counts = []
        for schema in self.schemas.values():
            if len(schema.referenced_by) > 0:
                ref_counts.append((
                    schema.sanitized_name.replace('_', ' ').title(),
                    len(schema.referenced_by),
                    os.path.relpath(schema.output_path, 'docs')
                ))

        ref_counts.sort(key=lambda x: x[1], reverse=True)

        stats_lines.append("### Most Referenced Schemas")
        stats_lines.append("")
        stats_lines.append("These schemas are used by many other schemas:")
        stats_lines.append("")

        for name, count, path in ref_counts[:10]:
            stats_lines.append(f"- [{name}]({path}) - referenced by {count} schema{'s' if count != 1 else ''}")

        stats_lines.append("")

        # Find schemas with most dependencies
        dep_counts = []
        for schema in self.schemas.values():
            if len(schema.references) > 0:
                dep_counts.append((
                    schema.sanitized_name.replace('_', ' ').title(),
                    len(schema.references),
                    os.path.relpath(schema.output_path, 'docs')
                ))

        dep_counts.sort(key=lambda x: x[1], reverse=True)

        stats_lines.append("### Most Complex Schemas")
        stats_lines.append("")
        stats_lines.append("These schemas reference many other schemas:")
        stats_lines.append("")

        for name, count, path in dep_counts[:10]:
            stats_lines.append(f"- [{name}]({path}) - references {count} other schema{'s' if count != 1 else ''}")

        return "\n".join(stats_lines)

    def _generate_index(self, output_dir: str):
        """
        Generate the README index file with schema graph and statistics.

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

        # Generate graph and stats
        schema_graph = self._generate_schema_graph()
        reference_stats = self._generate_reference_stats()

        # Build index markdown
        index_parts = [
            "# Carta API Schema Documentation",
            "",
            "This directory contains documentation for the JSON schemas used in the Carta API. "
            "The documentation is auto-generated from the OpenAPI specification.",
            "",
            "## 🎨 Interactive Schema Dependency Graph",
            "",
            "**[Open Interactive Graph →](schema-graph.html)** - Explore the full schema dependency graph with:",
            "- 🔍 **Search** - Find any schema instantly",
            "- 🖱️ **Drag & Drop** - Reposition nodes",
            "- 🔎 **Zoom & Pan** - Navigate the graph",
            "- 📊 **Live Stats** - See reference counts",
            "- 💡 **Hover Tooltips** - View schema details",
            "- 🎯 **Click to Navigate** - Jump to documentation",
            "",
            "The interactive graph uses a force-directed layout algorithm to automatically position schemas "
            "based on their relationships, making it easy to understand the API structure at a glance.",
            "",
            "---",
            "",
            "## Schema Dependency Diagram",
            "",
            "This diagram shows how API objects (blue rectangles) reference supporting types (purple rounded boxes):",
            "",
            schema_graph,
            "",
            "**Legend:**",
            "- 🔵 **Blue rectangles (larger, bold)** = Primary API objects (with endpoints)",
            "- 🟣 **Purple rounded boxes** = Supporting types",
            "- ⭐ **Yellow highlighted with dashed border** = Highly-used schemas (10+ references)",
            "- ➡️ **Arrows** = \"uses\" or \"references\" relationship",
            "",
            "---",
            "",
            reference_stats,
            "",
            "---",
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

        print(f"✓ Generated index with schema graph: {readme_path}")


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
