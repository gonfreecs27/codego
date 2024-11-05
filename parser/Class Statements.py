#Class Statements Parser

import ply.lex as lex
import ply.yacc as yacc

# Tokens for Class Statements
tokens = [
    'KLASE', 'GAWA', 'TEXT', 'NUMBER', 'DECIMAL', 'LBRACE', 'RBRACE',
    'LPAREN', 'RPAREN', 'IDENTIFIER', 'COMMA'
]

# Reserved words for Class Statements
reserved = {
    'Klase': 'KLASE',
    'Gawa': 'GAWA',
    'Teksto': 'TEXT',
    'Numero': 'NUMBER',
    'Desimal': 'DECIMAL'
}

# Token specifications for Class Statements
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','

# Ignoring whitespace
t_ignore = ' \t'

# Identifiers (Variable and function names)
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

# Parsing rules for Class Statements
def p_class_statement(p):
    '''class_statement : KLASE IDENTIFIER LBRACE class_props class_methods RBRACE'''
    print(f"Parsed a class named {p[2]}")

def p_class_props(p):
    '''class_props : TEXT IDENTIFIER
                   | NUMBER IDENTIFIER
                   | DECIMAL IDENTIFIER
                   | empty'''
    print("Parsed class properties")

def p_class_methods(p):
    '''class_methods : GAWA IDENTIFIER LPAREN RPAREN LBRACE RBRACE
                     | empty'''
    print("Parsed class methods")

def p_empty(p):
    'empty :'
    pass

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

# Example code to parse for Class Statements
code_class_statements = """
Klase Customer {
    Teksto pangalan
    Numero edad
    Desimal dalangPera

    Gawa init() {}

    Gawa bumili(Lista order) {
        print("Eto ang mga binili ni ", ako.pangalan)
    }
}
"""

# Parsing the Class Statements code
parser.parse(code_class_statements)
