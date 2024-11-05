from .bawat import bawat_statement
from .expression import expression_statement
from .gawa import gawa_declaration, gawa_invocation
from .habang import habang_statement
from .kapag import kapag_statement
from .komento import komento_statement
from .kung import kung_statement
from .variable import var_declaration

class CodeGoParser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def parse(self):
        """
        Parses the input tokens into statements.

        This method serves as the entry point for parsing the entire code structure.
        It gathers all statements from the input token stream and returns them.

        Returns:
            list: A list of parsed statements.

        Raises:
            RuntimeError: If no statements are found in the input.
        """
        
        # Gather all statements from the token stream
        stmts = self.statements()
        if len(stmts) == 0:
            raise RuntimeError('File is empty. There is nothing to parse.')
        
        return stmts


    def statements(self):
        """
        Parses a sequence of statements from the current token stream.

        This method continues to parse statements until an end condition is met,
        which can be either the end of the file (EOF), a closing brace (RBRACE),
        or the HINTO token (break statement).

        Returns:
            list: A list of parsed statements.
        """
        
        # Initialize an empty list to hold parsed statements
        statements = []
        while self.current_token()[0] not in ['EOF', 'RBRACE', 'HINTO']:
            stmt = self.statement()
            
            # If a statement was successfully parsed, 
            # add it to the list of statements
            if stmt is not None:
                statements.append(stmt)
        return statements


    def statement(self):
        """
        Parses a single statement from the current token stream based on the current token type.

        This method identifies the type of statement to parse and delegates to the appropriate 
        parsing function based on the token type. It handles variable declarations, comments, 
        control flow statements, function invocations, and other statement types.

        Returns:
            dict: A parsed representation of the statement, or None for newlines.
        
        Raises:
            RuntimeError: If an unexpected token is encountered.
        """
        
        # Get the current token from the token stream
        current_token = self.current_token()
        token_type = current_token[0]
        line_number = current_token[2]
        
        # For variable declaration
        if token_type == 'BASIC_TYPE':
            return var_declaration(self)
        
        # For comments
        elif token_type == 'COMMENT':
            return komento_statement(self)
        
        # For new lines
        elif token_type == 'NEWLINE':
            self.eat('NEWLINE')
            return None
        
        # For invoking functions
        elif token_type == 'IDENTIFIER':
            # Look ahead for function invocation
            next_token = self.peek()  # Check the next token
            if next_token[0] == 'LPAREN':
                return gawa_invocation(self)
            else:
                return expression_statement(self)
        
        # Kung statement
        elif token_type == 'KUNG':
            return kung_statement(self)
        
        # Kapag statement
        elif token_type == 'KAPAG':
            return kapag_statement(self)
        
        # Habang statement
        elif token_type == 'HABANG':
            return habang_statement(self)

        # Bawat statement
        elif token_type == 'BAWAT':
            return bawat_statement(self)

        # Gawa declaration
        elif token_type == 'GAWA':
            return gawa_declaration(self)

        else:
            raise RuntimeError(f'Unexpected token: {self.current_token()} on line {line_number}')


    def arguments(self):
        """
        Parses the arguments within a function call.

        Returns:
            list: A list of parsed arguments, which can include:
                - Identifiers, potentially with property access (e.g., object.property).
                - Numeric literals.
                - String literals.
                - Boolean literals.
        """
    
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
        """
        Parses an expression which can include binary operations (addition, subtraction, 
        comparisons, etc.) and terms.

        Returns:
            dict: A structured representation of the parsed expression, including:
                - 'type': The type of operation ('binary_op' for binary operations).
                - 'operator': The operator used in the operation (e.g., '+', '-', '>', etc.).
                - 'left': The left operand of the operation.
                - 'right': The right operand of the operation.
        """
    
        term = self.term()
        while self.current_token()[0] in ('PLUS', 'MINUS', 'GREATER', 'LESS', 'GREATER_EQUAL', 'LESS_EQUAL'):
            operator = self.eat(self.current_token()[0])
            term2 = self.term()
            term = {'type': 'binary_op', 'operator': operator[1], 'left': term, 'right': term2}
        return term


    def term(self):
        """
        Parses a term in an expression.

        Returns:
            dict or any: A parsed term, which can include:
                        - An identifier, potentially with property access.
                        - A numeric literal.
                        - A boolean literal.
                        - A string literal.
                        - An expression enclosed in parentheses.
                        - A block of statements enclosed in braces.
        """

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


    def parameters(self):
        """
        Parses parameters in a function declaration, where each parameter can optionally 
        have a type (e.g., 'Desimal bayad' or just 'bayad').

        Returns:
            list: A list of dictionaries, each representing a parameter with the following keys:
                - 'type': The type of the parameter as a string, or None if untyped.
                - 'name': The name of the parameter as a string.
        """

        parameters = []

        while self.current_token()[0] != 'RPAREN':
            # Check if there is an optional BASIC_TYPE
            param_type = None
            if self.current_token()[0] == 'BASIC_TYPE':
                param_type = self.eat('BASIC_TYPE')[1]  # Consume the type if present

            # Next, we expect an identifier for the parameter name
            param_name = self.eat('IDENTIFIER')[1]

            parameters.append({
                'type': param_type,  # This will be None if no type was provided
                'name': param_name
            })

            # If the next token is a comma, consume it to proceed to the next parameter
            if self.current_token()[0] == 'COMMA':
                self.eat('COMMA')
            else:
                break  # Exit loop if no comma (and we assume we're at the end of the parameter list)

        return parameters


    def eat(self, token_type):
        """
        Consumes the current token if it matches the expected type.

        Args:
            token_type (str): The type of the token expected (e.g., 'IDENTIFIER', 'NUMERO').

        Returns:
            tuple: The consumed token, which includes its type, value, and line number.

        Raises:
            RuntimeError: If the current token does not match the expected type, indicating an error.
        """
        current = self.current_token()
        
        # Check if the token type matches the expected type
        if current[0] == token_type:
            token = current
            self.pos += 1
            return token
        else:
            # Raise an error if the current token does not match the expected type
            raise RuntimeError(f'Expected {token_type}, got {current} on line {current[2]}')


    def current_token(self):
        """
        Retrieves the current token based on the current position.

        Returns:
            tuple: The current token, which is a tuple containing the token type,
                its value, and the line number.
        
        If the current position is beyond the end of the tokens list,
        returns an 'EOF' token, indicating the end of the input.

        If there are no tokens, returns an 'EOF' token with line number 1.
        """
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return ('EOF', None, self.tokens[-1][2] if self.tokens else 1)


    def peek(self):
        """
        Looks ahead to the next token in the token stream without advancing the current position.

        Returns:
            tuple: The next token if available, otherwise an 'EOF' token.

        The 'EOF' token indicates that there are no more tokens to process.
        """
        if self.pos + 1 < len(self.tokens):
            return self.tokens[self.pos + 1]
        return ('EOF', None, self.tokens[-1][2] if self.tokens else 1)
