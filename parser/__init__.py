from .bawat import bawat_statement
from .habang import habang_statement
from .kapag import kapag_statement
from .kung import kung_statement
from .lista import parse_list

class CodeGoParser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def parse(self):
        stmts = self.statements()
        if len(stmts) == 0:
            raise RuntimeError('File is empty. There is nothing to parse.')
        return stmts

    def statements(self):
        statements = []
        while self.current_token()[0] not in ['EOF', 'RBRACE', 'HINTO']:
            stmt = self.statement()
            if stmt is not None:
                statements.append(stmt)
        return statements

    def statement(self):
        current_token = self.current_token()
        token_type = current_token[0]
        line_number = current_token[2]
        
        # For variable declaration
        if token_type == 'BASIC_TYPE':
            return self.var_declaration()
        
        # For Comments
        elif token_type == 'COMMENT':
            return self.comment()
        
        # For New Lines
        elif token_type == 'NEWLINE':
            self.eat('NEWLINE')
            return None
        
        # For invoking functions
        elif token_type == 'IDENTIFIER':
            # Look ahead for function invocation
            next_token = self.peek()  # Check the next token
            if next_token[0] == 'LPAREN':
                return self.function_invocation()
            else:
                return self.expression_statement()
        
        # Kung statement
        elif token_type == 'KUNG':
            return kung_statement(self)
        
        # Kapag statement
        elif token_type == 'KAPAG':
            return kapag_statement(self)
        
        # Habang statement
        elif token_type == 'HABANG':
            return habang_statement(self)

        elif token_type == 'BAWAT':
            return bawat_statement(self)

        else:
            raise RuntimeError(f'Unexpected token: {self.current_token()} on line {line_number}')

    def var_declaration(self):
        basic_type = self.eat('BASIC_TYPE')
        identifier = self.eat('IDENTIFIER')
        expression = None
        if self.current_token()[0] == 'EQUALS':
            self.eat('EQUALS')
            if basic_type[1] == 'Lista' and self.current_token()[0] == 'LBRACKET':
                expression = parse_list(self)
            else:
                expression = self.expression()
        return {
            'type': 'var_declaration',
            'basic_type': basic_type[1],
            'identifier': identifier[1],
            'expression': expression
        }
        
    def function_invocation(self):
        identifier = self.eat('IDENTIFIER')
        self.eat('LPAREN')
        arguments = self.arguments()
        self.eat('RPAREN')
        return {
            'type': 'function_invocation',
            'function_name': identifier[1],
            'arguments': arguments
        }

    def arguments(self):
        args = []
        while self.current_token()[0] != 'RPAREN':
            if self.current_token()[0] == 'IDENTIFIER':
                identifier = self.eat('IDENTIFIER')
                result = identifier

                # Check for property access (e.g., luto.ulam)
                while self.current_token()[0] == 'DOT':
                    self.eat('DOT')
                    property_name = self.eat('IDENTIFIER')
                    result = {
                        'type': 'property_access',
                        'object': result,
                        'property': property_name[1]
                    }
                args.append(result)
            if self.current_token()[0] in ('NUMERO', 'TEKSTO', 'TSEK'):
                args.append(self.eat(self.current_token()[0]))
            if self.current_token()[0] == 'NEWLINE':
                self.eat('NEWLINE')
            if self.current_token()[0] != 'RPAREN':
                self.eat('COMMA')
        return args

    def expression(self):
        term = self.term()
        while self.current_token()[0] in ('PLUS', 'MINUS', 'GREATER', 'LESS', 'GREATER_EQUAL', 'LESS_EQUAL'):
            operator = self.eat(self.current_token()[0])
            term2 = self.term()
            term = {'type': 'binary_op', 'operator': operator[1], 'left': term, 'right': term2}
        return term
    
    def expression_statement(self):
        # Handle assignments or simple expressions
        if self.current_token()[0] == 'IDENTIFIER':
            identifier = self.eat('IDENTIFIER')
        
            # Check if the next token is an assignment
            if self.current_token()[0] == 'EQUALS':
                self.eat('EQUALS')
                expr = self.expression()
                return {
                    'type': 'assignment',
                    'identifier': identifier[1],
                    'expression': expr
                }
            else:
                # If no assignment, it can be a simple expression
                return {
                    'type': 'expression',
                    'expression': identifier[1]
                }
        else:
            # Handle other cases as expressions directly
            expr = self.expression()
            return {
                'type': 'expression',
                'expression': expr
            }

    def term(self):
        current_token = self.current_token()[0]
        if current_token == 'IDENTIFIER':
            identifier = self.eat('IDENTIFIER')
            result = identifier

            # Check for property access (e.g., luto.ulam)
            while self.current_token()[0] == 'DOT':
                self.eat('DOT')
                property_name = self.eat('IDENTIFIER')
                result = {
                    'type': 'property_access',
                    'object': result,
                    'property': property_name[1]
                }

            return result
        elif current_token in ['NUMERO', 'TSEK', 'TEKSTO']:
            return self.eat(current_token)
        elif current_token == 'LPAREN':
            self.eat('LPAREN')
            expr = self.expression()
            self.eat('RPAREN')
            return expr
        elif current_token == 'LBRACE':
            self.eat('LBRACE')
            expr = self.statements()
            self.eat('RBRACE')
            return expr
        raise RuntimeError(f'Unexpected token in term: {self.current_token()}')

    def comment(self):
        comment = self.eat('COMMENT')
        return {'type': 'comment', 'text': comment[1]}

    def eat(self, token_type):
        current = self.current_token()
        if current[0] == token_type:
            token = current
            self.pos += 1
            return token
        else:
            raise RuntimeError(f'Expected {token_type}, got {current} on line {current[2]}')

    def current_token(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return ('EOF', None, self.tokens[-1][2] if self.tokens else 1)
    
    def peek(self):
        if self.pos + 1 < len(self.tokens):
            return self.tokens[self.pos + 1]
        return ('EOF', None, self.tokens[-1][2] if self.tokens else 1)
