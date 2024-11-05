def kung_statement(parser):
    """
    Parses a 'KUNG' statement, which represents a conditional statement similar to an if statement.

    Returns:
        dict: A dictionary representing the parsed 'kung' statement, containing:
            - 'type': 'kung_statement'
            - 'condition': The expression that determines whether the statements are executed
            - 'statements': A list of statements to execute if the condition is true
    """

    # Consume the 'KUNG' keyword, marking the start of the conditional statement
    parser.eat('KUNG')
    
    # Parse the condition expression within parentheses
    parser.eat('LPAREN')
    condition = parser.expression()
    parser.eat('RPAREN')
    
    # Parse the statements within braces
    parser.eat('LBRACE')

    # Collect the statements to execute if the condition is true
    statements = parser.statements()
    
    # Consume the closing brace to end the 'KUNG' statement
    parser.eat('RBRACE')
    
    # Return the parsed 'kung' statement as a structured dictionary
    return {
        'type': 'kung_statement',
        'condition': condition,
        'statements': statements
    }
