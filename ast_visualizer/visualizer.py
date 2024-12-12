import ast
from graphviz import Digraph


class ASTVisualizer:
    def __init__(self):
        """
        Initializes the AST visualizer with a directed graph.
        """
        self.graph = Digraph("AST", node_attr={"shape": "box", "fontname": "Arial"})
        self.node_count = 0  # Counter to assign unique IDs to each node

    def add_node(self, label):
        """
        Adds a new node to the graph with a unique ID.

        :param label: The label for the node (e.g., the type of AST node).
        :return: The unique ID for the node.
        """
        node_id = f"node{self.node_count}"
        self.graph.node(node_id, label)
        self.node_count += 1
        return node_id

    def build_graph(self, node, parent_id=None):
        """
        Recursively builds the graph by traversing the AST.

        :param node: The current AST node.
        :param parent_id: The ID of the parent node (if any).
        """
        # Add the current node to the graph
        node_label = type(node).__name__
        node_id = self.add_node(node_label)

        # Connect the current node to its parent, if applicable
        if parent_id is not None:
            self.graph.edge(parent_id, node_id)

        # Traverse all child nodes recursively
        for child in ast.iter_child_nodes(node):
            self.build_graph(child, node_id)

    def render(self, output_file="ast_graph", view=False):
        """
        Renders the graph to a file and optionally opens it.

        :param output_file: The name of the output file (without extension).
        :param view: Whether to open the output file after rendering.
        """
        self.graph.render(output_file, format="png", cleanup=True)
        if view:
            self.graph.view()


if __name__ == "__main__":
    import sys
    from parser import read_file, parse_to_ast

    # Example usage
    if len(sys.argv) != 2:
        print("Usage: python visualizer.py <path_to_python_file>")
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        # Step 1: Read and parse the Python file
        code = read_file(file_path)
        tree = parse_to_ast(code)

        # Step 2: Visualize the AST
        visualizer = ASTVisualizer()
        visualizer.build_graph(tree)  # Build the graph
        visualizer.render(output_file="ast_graph", view=True)  # Render and view

        print("AST visualization saved as 'ast_graph.png'.")

    except Exception as e:
        print(f"Error: {e}")
