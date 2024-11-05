def kapag_statement(self):
    self.eat('KAPAG')
    self.eat('LPAREN')
    condition = self.expression()
    self.eat('RPAREN')
    self.eat('LBRACE')

    cases = []
    while self.current_token()[0] == 'KASO':
        self.eat('KASO')
        case_expr = self.expression()
        self.eat('COLON')
    
        case_statements = self.statements()
        cases.append({
            'case_expr': case_expr,
            'case_statements': case_statements
        })

        self.eat('HINTO')

    self.eat('RBRACE')
    return {
        'type': 'kapag_statement',
        'condition': condition,
        'cases': cases
    }
