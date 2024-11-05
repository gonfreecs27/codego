from .lista import parse_list

def var_declaration(parser):
    """
    Parses a variable declaration statement from the token stream.

    A variable declaration consists of a basic type, an identifier, and an optional 
    assignment of a value or expression. This function handles both direct value assignments 
    and initializations of lists.

    Args:
        parser (Parser): The parser instance to read from the token stream.

    Returns:
        dict: A parsed representation of the variable declaration, including:
              - 'type': The type of declaration ('var_declaration').
              - 'basic_type': The data type of the variable (e.g., 'Numero', 'Desimal', etc.).
              - 'identifier': The name of the variable being declared.
              - 'expression': The assigned value or expression, if any (None if not assigned).
    """
    
    # Expect and consume a BASIC_TYPE token
    basic_type = parser.eat('BASIC_TYPE')
    
    # Expect and consume an IDENTIFIER token
    identifier = parser.eat('IDENTIFIER')
    
    # Initialize the expression to None
    expression = None
    
    # Check if the next token is an equals sign, indicating an assignment
    if parser.current_token()[0] == 'EQUALS':
        parser.eat('EQUALS')
        if basic_type[1] == 'Lista' and parser.current_token()[0] == 'LBRACKET':
            expression = parse_list(parser)
        else:
            expression = parser.expression()

    return {
        'type': 'var_declaration',
        'basic_type': basic_type[1],
        'identifier': identifier[1],
        'expression': expression
    }