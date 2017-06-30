#! coding: utf-8
"""Calculator lexer example."""
import ply.lex as lex

"""
Lista de tokens

El analizador léxico de PLY (al llamar al método lex.lex()) va a buscar
para cada uno de estos tokens una variable "t_TOKEN" en el módulo actual.

Sí, es súper nigromántico pero es lo que hay.

t_TOKEN puede ser:

- Una expresión regular
- Una función cuyo docstring sea una expresión regular (bizarro).

En el segundo caso, podemos hacer algunas cosas "extras", como se
muestra aquí abajo.

"""

tokens = (
    'TWOPOINTS',
    'VARIABLE',
    'TRUE',
    'FALSE',
    'ZERO',
    'LAMBDA',
    'IF',
    'THEN',
    'ELSE',
    'XTYPE',
    'T',
    'POINT',
    'SUCC',
    'OPENPAREN',
    'CLOSEPAREN',
    'PRED',
    'ISZERO',
    'BOOL',
    'NAT',
    'ARROW',
)

t_VARIABLE = r'\d'
t_TRUE = r'true'
t_FALSE = r'false'
t_IF = r'if'
t_ELSE = r'else'
t_THEN = r'then'
t_ignore = ' '
t_TWOPOINTS = r':'
t_LAMBDA = r'/'
t_SUCC = r'succ'
t_OPENPAREN = r'\('
t_CLOSEPAREN = r'\)'
# t_POINT = r'\.'
# t_PRED = r'pred'
# t_ISZERO = r'iszero'
# t_ARROW = r'\->'

def t_ZERO(t):
    r'\d'
    t.value = int(t.value)
    return t

# Build the lexer
lexer = lex.lex()

def apply_lexer(string):
    """Aplica el lexer al string dado."""
    lexer.input(string)

    return list(lexer)

