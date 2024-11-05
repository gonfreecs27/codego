def kapag_statement(self):
    """
    Parses a 'KAPAG' statement, which represents a conditional switch-like statement.
    Each 'KASO' block acts as a case with specific expressions and statements.
    
    Returns:
        dict: A dictionary representing the parsed 'kapag' statement, containing:
            - 'type': 'kapag_statement'
            - 'condition': The expression evaluated to determine case matching
            - 'cases': A list of case dictionaries, each with:
                - 'case_expr': The case's expression
                - 'case_statements': The list of statements within the case
    """

    # Consume the 'KAPAG' keyword, marking the start of the switch-like structure
    self.eat('KAPAG')
    
    # Parse the condition expression within parentheses
    self.eat('LPAREN')
    condition = self.expression()
    self.eat('RPAREN')
    
    # Parse the cases within braces
    self.eat('LBRACE')

    cases = []
    while self.current_token()[0] == 'KASO':
        # Consume the 'KASO' keyword, indicating a new case
        self.eat('KASO')
        
        # Parse the case expression
        case_expr = self.expression()
        self.eat('COLON')
        
        # Collect the statements in the case block
        case_statements = self.statements()
        cases.append({
            'case_expr': case_expr,
            'case_statements': case_statements
        })
        
        # Consume 'HINTO' to end the current case
        self.eat('HINTO')
    
    # Consume the closing brace to end the 'KAPAG' statement
    self.eat('RBRACE')
    
    # Return the parsed 'kapag' statement as a structured dictionary
    return {
        'type': 'kapag_statement',
        'condition': condition,
        'cases': cases
    }
