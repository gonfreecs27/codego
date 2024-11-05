import sys
import traceback
from parser import CodeGoParser
from parser.lexer import CodeGoLexer

if (len(sys.argv) != 2):
    print("Feed the script to our compiler using: python codego.py <filename.cg>")
    sys.exit(1)

filename = sys.argv[1]

# Check if the filename ends with .go
if not filename.endswith('.cg'):
    print("Error: The file must have a .cg extension.")
    sys.exit(1)
    
try:
    with open(filename, 'r') as file:
        source_code = file.read()
    
    print("Running CodeGo compiler...")
    print("Source:")
    print(source_code)
    
    print()
    print("------------------------------")
    print("Tokens:")
    lexer = CodeGoLexer(source_code)
    tokens = lexer.tokens
    for token in tokens:
        print(token)
    
    print()
    print("-----------------------------")
    print("Syntax Tree:")
    parser = CodeGoParser(tokens)
    ast = parser.parse()
    print(ast)
            
    print("Valid Syntax!")
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except Exception as e:
    print(f"Invalid Syntax: {e}")
    # traceback.print_exc()
    