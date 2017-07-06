#! coding: utf-8
"""Calculator lexer example."""
import ply.lex as lex

LOCALE = False

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
t_VARIABLE = r'\w'
t_TRUE = r'true'
t_FALSE = r'false'
t_THEN = r'then'
t_ELSE = r'else'
t_LAMBDA = r'\\'
t_TWOPOINTS = r':'
t_POINT = r'\.'
t_SUCC = r'succ'
t_OPENPAREN = r'\('
t_CLOSEPAREN = r'\)'
t_PRED = r'pred'
t_ISZERO = r'iszero'
t_BOOL = r'Bool'
t_NAT = r'Nat'
t_ARROW = r'->'

def t_ZERO(t):
  r'\d'
  t.value = int(t.value)
  return t

def t_IF(t):
  r'if'
  t.value = t.value
  return t

# Build the lexer
lexer = lex.lex()


def apply_lexer(string):
    """Aplica el lexer al string dado."""
    lexer.input(string)

    return list(lexer)
