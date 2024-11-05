import re

class CodeGoLexer:
    def __init__(self, source):
        self.source = source
        self.tokens = []
        self.line_number = 1
        self.tokenize()

    def tokenize(self):
        token_specification = [
            ('BASIC_TYPE', r'Numero|Desimal|Teksto|Tsek|Lista|Bagay'),  # Basic types
            ('NUMERO',    r'\d+(\.\d+)?'),  # Numeric literals
            ('TEKSTO',    r'"[^"]*"'),      # String literals
            ('TSEK',   r'Tama|Mali'),     # Boolean literals
            
            # Conditional Statements
            ('KUNG', r'Kung'),
            ('KAPAG', r'Kapag'),
            ('KASO', r'Kaso'),
            ('HINTO', r'Hinto'),
            
            # Loop Statements
            ('HABANG',    r'Habang'),
            ('BAWAT',     r'Bawat'),
            ('SA',        r'Sa'),
            
            # Function declaration keyword
            ('GAWA', r'Gawa'),        
            
            ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),  # Identifiers

            ('NEWLINE',   r'\n'),            # New line
            ('COMMENT',   r'#.*'),           # Comments
            ('WHITESPACE', r'\s+'),          # Skip whitespace
            ('DOT',       r'\.'),
            ('PLUS',      r'\+'),            # Addition
            ('MINUS',     r'-'),             # Subtraction
            ('TIMES',     r'\*'),            # Multiplication
            ('DIVIDE',    r'/'),             # Division
            ('LPAREN',    r'\('),            # Left parenthesis
            ('RPAREN',    r'\)'),            # Right parenthesis
            ('LBRACE',    r'\{'),            # Left brace
            ('RBRACE',    r'\}'),            # Right brace
            ('LBRACKET',  r'\['),            # Left square bracket (for lists)
            ('RBRACKET',  r'\]'),            # Right square bracket (for lists)
            ('COMMA',     r','),             # Comma
            ('SEMICOLON', r';'),             # Semicolon
            ('COLON',     r':'),              # Colon
            ('EQUALS',    r'='),              # Equals
            ('GREATER',   r'>'),              # Greater than
            ('LESS',      r'<'),              # Less than
            ('GREATER_EQUAL', r'>='),         # Greater than or equal to
            ('LESS_EQUAL', r'<='),            # Less than or equal to
            ('ERROR',     r'.'),              # Any other character
        ]

        tok_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_specification)
        for mo in re.finditer(tok_regex, self.source):
            kind = mo.lastgroup
            value = mo.group()
            if kind == 'NEWLINE':
                # self.tokens.append(('NEWLINE', None, self.line_number)) 
                self.line_number += 1
            elif kind == 'NUMERO':
                self.tokens.append(('NUMERO', float(value) if '.' in value else int(value), self.line_number))
            elif kind == 'TEKSTO':
                self.tokens.append(('TEKSTO', value[1:-1], self.line_number))  # Strip the quotes
            elif kind == 'TSEK':
                self.tokens.append(('TSEK', value, self.line_number))
            elif kind == 'IDENTIFIER':
                self.tokens.append(('IDENTIFIER', value, self.line_number))
            elif kind == 'COMMENT':
                continue  # Skip comments
            elif kind == 'WHITESPACE':
                continue  
            elif kind == 'ERROR':
                raise RuntimeError(f'Unexpected character: {value} on line {self.line_number}')
            else:
                self.tokens.append((kind, value, self.line_number))

        self.tokens.append(('EOF', None, self.line_number))  # End of file token
