def parse_list(parser):
    parser.eat('LBRACKET')
    items = []
    while parser.current_token()[0] != 'RBRACKET':
        if parser.current_token()[0] == 'LBRACE':
            items.append(parse_object(parser))
        if parser.current_token()[0] == 'COMMA':
            parser.eat('COMMA')
    parser.eat('RBRACKET')
    return {'type': 'list', 'items': items}

def parse_object(parser):
    parser.eat('LBRACE')
    obj = {}
    while parser.current_token()[0] != 'RBRACE':
        key = parser.eat('IDENTIFIER')
        parser.eat('COLON')
        value = parser.expression()
        obj[key[1]] = value
        if parser.current_token()[0] == 'COMMA':
            parser.eat('COMMA')
    parser.eat('RBRACE')
    return {'type': 'object', 'properties': obj}