import ast
import os

def read_file(file_path):
    """
    Reads the content of a Python file and validates it.

    :param file_path: Path to the Python file.
    :return: The content of the file as a string.
    :raises FileNotFoundError: If the file does not exist.
    :raises ValueError: If the file is not a Python file.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    if not file_path.endswith(".py"):
        raise ValueError(f"Invalid file type. Only Python files (.py) are supported: {file_path}")
    
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def parse_to_ast(file_content):
    """
    Parses the Python code into an Abstract Syntax Tree (AST).

    :param file_content: The source code as a string.
    :return: The root node of the AST.
    :raises SyntaxError: If the source code is invalid.
    """
    try:
        return ast.parse(file_content)
    except SyntaxError as e:
        raise SyntaxError(f"Failed to parse the file. Syntax error: {e}")

def get_ast_info(node, indent=0):
    """
    Recursively prints a summary of the AST nodes (for debugging or analysis).

    :param node: The current AST node.
    :param indent: Current indentation level for pretty printing.
    """
    print("  " * indent + f"{type(node).__name__}")
    for child in ast.iter_child_nodes(node):
        get_ast_info(child, indent + 1)

if __name__ == "__main__":
    # Example usage
    file_path = "examples/example.py"  # Replace with your test file
    try:
        # Step 1: Read the file
        code = read_file(file_path)

        # Step 2: Parse it into an AST
        tree = parse_to_ast(code)

        # Step 3: Print a basic structure of the AST (for debugging)
        print("Abstract Syntax Tree (AST):")
        get_ast_info(tree)

    except (FileNotFoundError, ValueError, SyntaxError) as e:
        print(f"Error: {e}")
