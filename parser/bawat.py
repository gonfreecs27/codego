def bawat_statement(parser):
    """
    Parses a 'BAWAT' statement, which represents a for-each loop over an iterable.
    
    Returns:
        dict: A dictionary representing the parsed 'bawat' statement, containing:
            - 'type': 'bawat_statement'
            - 'iterator': The name of the variable that will represent each item in the loop
            - 'iterable': The name of the iterable object being looped over
            - 'body': A list of statements within the loop body
    """
    # Consume the 'BAWAT' keyword to start the loop
    parser.eat('BAWAT')
    
    # Parse the loop structure within parentheses
    parser.eat('LPAREN')
    
    # Variable to represent each item in the iterable
    iterator = parser.eat('IDENTIFIER')
    # 'SA' keyword indicating 'in' (as in "for each item in iterable")
    parser.eat('SA')
    
    # The iterable being looped over
    iterable = parser.eat('IDENTIFIER')
    parser.eat('RPAREN')
    
    # Parse the loop body enclosed within braces
    parser.eat('LBRACE')
    body = parser.statements()
    parser.eat('RBRACE')
    
    # Return the parsed 'bawat' statement as a structured dictionary
    return {
        'type': 'bawat_statement',
        'iterator': iterator[1],
        'iterable': iterable[1],
        'body': body
    }
