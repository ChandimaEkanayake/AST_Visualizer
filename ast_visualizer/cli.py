from parser import read_file, parse_to_ast
from visualizer import ASTVisualizer
import os


def generate_ast_graph(file_path, output_file, view=False):
    """
    Reads a Python file, parses it into an AST, and generates a graphical visualization.

    :param file_path: Path to the Python script to analyze.
    :param output_file: Name of the output file (without extension).
    :param view: Whether to open the graph after rendering.
    """
    try:
        # Step 1: Read and parse the file
        code = read_file(file_path)
        ast_tree = parse_to_ast(code)

        # Step 2: Visualize the AST
        visualizer = ASTVisualizer()
        visualizer.build_graph(ast_tree)
        visualizer.render(output_file=output_file, view=view)

        print(f"AST graph successfully generated as '{output_file}.png'.")
    except Exception as e:
        print(f"Error: {e}")


def main():
    print("Welcome to the AST Graph Generator!")
    
    # Prompt user for the name of the Python file
    filename = input("Enter the name of the Python file (e.g., 'example1.py'): ").strip()
    input_file_path = os.path.join("examples", filename)
    
    # Check if file exists
    if not os.path.isfile(input_file_path):
        print(f"Error: File '{input_file_path}' not found. Please ensure it exists in the 'examples' folder.")
        return

    # Prompt user for the output file name
    output_file_name = input("Enter the output file name (without extension, e.g., 'example_ast'): ").strip()
    if not output_file_name:
        output_file_name = os.path.splitext(filename)[0] + "_ast"
    
    # Prompt user whether to view the generated graph
    view_input = input("Would you like to view the graph after it is generated? (yes/no): ").strip().lower()
    view = view_input in ("yes", "y")

    # Generate the AST graph
    generate_ast_graph(input_file_path, output_file_name, view)


if __name__ == "__main__":
    main()
