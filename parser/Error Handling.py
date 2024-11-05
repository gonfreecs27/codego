#Error Handling Parser

import ply.lex as lex
import ply.yacc as yacc

# Tokens for Error Handling
tokens = [
    'SUBUKAN', 'SALO', 'KUNG', 'BAGONG', 'LBRACE', 'RBRACE', 'LPAREN', 'RPAREN',
    'IDENTIFIER', 'STRING'
]

# Reserved words for Error Handling
reserved = {
    'Subukan': 'SUBUKAN',
    'Salo': 'SALO',
    'Kung': 'KUNG',
    'Bagong': 'BAGONG'
}

# Token specifications for Error Handling
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LPAREN = r'\('
t_RPAREN = r'\)'

# Ignoring whitespace
t_ignore = ' \t'

# Handling strings
def t_STRING(t):
    r'"[^"]*"'
    t.value = t.value.strip('"')
    return t

# Identifiers (Variable names)
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

# Error handling in the lexer
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Parsing rules for Error Handling
def p_error_handling(p):
    '''error_handling : SUBUKAN LBRACE statements RBRACE SALO LBRACE statements RBRACE'''
    print("Parsed an error-handling block")

def p_statements(p):
    '''statements : statement
                  | statements statement'''
    print("Parsed statements")

def p_statement(p):
    '''statement : KUNG LPAREN IDENTIFIER RPAREN LBRACE BAGONG IDENTIFIER LPAREN STRING RPAREN RBRACE
                 | IDENTIFIER LPAREN STRING RPAREN'''
    print("Parsed a statement")

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

# Example code to parse for Error Handling
code_error_handling = """
Subukan {
    Kung (diMahal) {
        Bagong Kamalian("Di ka pogi")
    }
} Salo (Kamalian e) {
    print("Eto mali sayo: ", e.mensahe)
}
"""

# Parsing the Error Handling code
parser.parse(code_error_handling)
