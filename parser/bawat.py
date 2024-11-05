def bawat_statement(parser):
    parser.eat('BAWAT')
    parser.eat('LPAREN')
    iterator = parser.eat('IDENTIFIER')
    parser.eat('SA')
    iterable = parser.eat('IDENTIFIER')
    parser.eat('RPAREN')
    parser.eat('LBRACE')
    body = parser.statements()
    parser.eat('RBRACE')
    return {
        'type': 'bawat_statement',
        'iterator': iterator[1],
        'iterable': iterable[1],
        'body': body
    }