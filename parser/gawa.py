def gawa_declaration(parser):
    """
    Parses a function declaration in the syntax using the keyword 'GAWA'.

    The function declaration starts with 'GAWA', followed by the function name
    (an identifier), a list of parameters enclosed in parentheses, and the function 
    body enclosed in braces. For example:

        Gawa pangalan (param1, param2) {
            // statements in the function body
        }

    Parameters:
        parser (CodeGoParser): The parser instance calling this function.

    Returns:
        dict: A dictionary representing the parsed function with the following keys:
            - 'type': A string ('gawa_declaration') indicating the node type.
            - 'name': The name of the function as a string.
            - 'parameters': A list of parsed parameter tokens.
            - 'body': A list of parsed statements in the function body.

    Raises:
        RuntimeError: If any expected token is missing (e.g., 'IDENTIFIER', 'LPAREN',
                      'RPAREN', 'LBRACE', or 'RBRACE').
    """

    parser.eat('GAWA')
    # Expect an identifier (function name)
    function_name = parser.eat('IDENTIFIER')
    # Expect parameters
    parser.eat('LPAREN')
    parameters = parser.parameters()
    parser.eat('RPAREN')
    # Expect function body in braces
    parser.eat('LBRACE')
    body = parser.statements()
    parser.eat('RBRACE')
    
    return {
        'type': 'gawa_declaration',
        'name': function_name[1],
        'parameters': parameters,
        'body': body
    }