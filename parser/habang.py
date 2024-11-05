def habang_statement(parser):
    """
    Parses a 'HABANG' statement, which represents a while-loop that executes as long as
    a specified condition evaluates to true.
    
    Returns:
        dict: A dictionary representing the parsed 'habang' statement, containing:
            - 'type': 'habang_statement'
            - 'condition': The expression to be evaluated as the loop's condition
            - 'statements': A list of statements within the loop body that execute each iteration
    """

    # Consume the 'HABANG' keyword to indicate the start of a while-loop
    parser.eat('HABANG')
    
    # Parse the condition within parentheses
    parser.eat('LPAREN')
    
    # Parse the expression serving as the loop's condition
    condition = parser.expression()
    parser.eat('RPAREN')
    
    # Parse the loop body enclosed in braces
    parser.eat('LBRACE')

    # Gather all statements within the loop body
    statements = parser.statements()
    parser.eat('RBRACE')
    
    # Return the parsed 'habang' statement as a structured dictionary
    return {
        'type': 'habang_statement',
        'condition': condition,
        'statements': statements
    }
