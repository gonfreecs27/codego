def kung_statement(parser):
    parser.eat('KUNG')
    parser.eat('LPAREN')
    condition = parser.expression()
    parser.eat('RPAREN')
    parser.eat('LBRACE')
    statements = parser.statements()
    parser.eat('RBRACE')
    return {
        'type': 'kung_statement',
        'condition': condition,
        'statements': statements
    }