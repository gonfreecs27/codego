def parse_list(parser):
    """
    Parses a list structure enclosed in brackets [].

    Args:
        parser (CodeGoParser): The parser instance used for parsing tokens.

    Returns:
        dict: A dictionary representing the parsed list, containing:
            - 'type': 'list'
            - 'items': A list of parsed items within the brackets
    """
    
    # Consume the opening bracket for the list
    parser.eat('LBRACKET')

    # Initialize an empty list to hold the items
    items = []

    while parser.current_token()[0] != 'RBRACKET':
        if parser.current_token()[0] == 'LBRACE':
            items.append(parse_object(parser))
        elif parser.current_token()[0] in ('NUMERO', 'TEKSTO', 'TSEK', 'IDENTIFIER'):
            # Consume the current token if it's a valid item
            items.append(parser.eat(parser.current_token()[0]))

        # Consume the comma if found
        if parser.current_token()[0] == 'COMMA':
            parser.eat('COMMA')
    
    # Consume the closing bracket for the list
    parser.eat('RBRACKET')
    return {'type': 'list', 'items': items}


def parse_object(parser):
    """
    Parses an object structure enclosed in braces {}.

    Args:
        parser (CodeGoParser): The parser instance used for parsing tokens.

    Returns:
        dict: A dictionary representing the parsed object, containing:
            - 'type': 'object'
            - 'properties': A dictionary of key-value pairs within the object
    """

    # Consume the opening brace for the object
    parser.eat('LBRACE')
    
    # Initialize an empty dictionary to hold the properties
    obj = {}

    # Continue until the closing brace is found
    while parser.current_token()[0] != 'RBRACE':
        key = parser.eat('IDENTIFIER')
        parser.eat('COLON')
        value = parser.expression()
        obj[key[1]] = value

        # If there's a comma, consume it to continue to the next key-value pair
        if parser.current_token()[0] == 'COMMA':
            parser.eat('COMMA')
    parser.eat('RBRACE')
    return {'type': 'object', 'properties': obj}