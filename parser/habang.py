def habang_statement(parser):
    parser.eat('HABANG')
    parser.eat('LPAREN')
    condition = parser.expression()
    parser.eat('RPAREN')
    parser.eat('LBRACE')

    # Collect the statements within the while loop
    statements = parser.statements()  
    parser.eat('RBRACE')

    return {
        'type': 'habang_statement',
        'condition': condition,
        'statements': statements
    }
