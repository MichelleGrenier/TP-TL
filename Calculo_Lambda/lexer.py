#! coding: utf-8
"""Calculator lexer example."""
import ply.lex as lex

tokens = (
    'VARIABLE',
    'TRUE',
    'FALSE',
    'IF',
    'THEN',
    'ELSE',
    'LAMBDA',
    'TWOPOINTS',
    'POINT',
    'ZERO',
    'SUCC',
    'OPENPAREN',
    'CLOSEPAREN',
    'PRED',
    'ISZERO',
    'BOOL',
    'NAT',
    'ARROW',
)

t_ignore = ' '
t_VARIABLE = r'x'
t_TRUE = r'true'
t_FALSE = r'false'
t_IF = r'if'
t_THEN = r'then'
t_ELSE = r'else'
t_LAMBDA = r'\\'
t_TWOPOINTS = r':'
t_POINT = r'\.'
t_ZERO = r'\d'
t_SUCC = r'succ'
t_OPENPAREN = r'\('
t_CLOSEPAREN = r'\)'
t_PRED = r'pred'
t_ISZERO = r'iszero'
t_BOOL = r'Bool'
t_NAT = r'Nat'
t_ARROW = r'->'

# Build the lexer
lexer = lex.lex()

def apply_lexer(string):
    """Aplica el lexer al string dado."""
    lexer.input(string)

    return list(lexer)
