def expression_statement(parser):
    """
    Parses an expression statement, which can be either an assignment 
    (e.g., x = 5) or a simple expression (e.g., just x).

    Returns:
        dict: A structured representation of the statement, including:
              - 'type': The type of the statement ('assignment' or 'expression').
              - 'identifier': The name of the variable (if it's an assignment).
              - 'expression': The evaluated expression (if it's an assignment or a simple expression).
    """

    # Handle assignments or simple expressions
    if parser.current_token()[0] == 'IDENTIFIER':
        identifier = parser.eat('IDENTIFIER')
    
        # Check if the next token is an assignment
        if parser.current_token()[0] == 'EQUALS':
            parser.eat('EQUALS')
            expr = parser.expression()
            return {
                'type': 'assignment',
                'identifier': identifier[1],
                'expression': expr
            }
        else:
            # If no assignment, treat it as a simple expression
            return {
                'type': 'expression',
                'expression': identifier[1]
            }
    else:
        # If the current token is not an identifier, handle other expressions directly
        expr = parser.expression()
        return {
            'type': 'expression',
            'expression': expr
        }
