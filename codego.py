import sys
import traceback
from parser import CodeGoParser
from parser.lexer import CodeGoLexer

def main():
    if len(sys.argv) != 2:
        print("Usage: python codego.py <filename.cg>")
        sys.exit(1)

    filename = sys.argv[1]

    # Check if the filename ends with .cg
    if not filename.endswith('.cg'):
        print("Error: The file must have a .cg extension.")
        sys.exit(1)

    try:
        with open(filename, 'r') as file:
            source_code = file.read()

        print("Running CodeGo compiler...")
        print("Source Code:")
        print(source_code)
        print("\n------------------------------")
        
        # Tokenization
        print("Tokens:")
        lexer = CodeGoLexer(source_code)
        tokens = lexer.tokens
        for token in tokens:
            print(token)

        print("\n-----------------------------")
        
        # Parsing
        print("Syntax Tree:")
        parser = CodeGoParser(tokens)
        ast = parser.parse()
        
        # Pretty print the AST
        print_ast(ast)

        print("\n-----------------------------")
        print("Result: Valid Syntax!")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"Invalid Syntax: {e}")
        traceback.print_exc()  # For debugging purposes

def print_ast(ast, level=0):
    """ Pretty print the Abstract Syntax Tree (AST) """
    indent = '  ' * level
    if isinstance(ast, dict):
        for key, value in ast.items():
            print(f"{indent}{key}:")
            print_ast(value, level + 1)
    elif isinstance(ast, list):
        for item in ast:
            print_ast(item, level)
    else:
        print(f"{indent}{ast}")

if __name__ == "__main__":
    main()
