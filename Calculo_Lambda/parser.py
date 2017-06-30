"""Parser LR(1) de calculadora."""
import ply.yacc as yacc
from .lexer import tokens
from expressions import BoolExpression, IfExpression, ZeroExpression

start = 'expression'
# precedence = [
#     ('left', 'MINUS'),
#     ('left', 'PLUS'),
#     ('left', 'TIMES'),
#     ('right', 'UMINUS')
# ]

def p_expression_true(p):
    'expression : TRUE'
    p[0] = BoolExpression(p[1])

def p_expresion_false(p):
    'expression : FALSE'
    p[0] = BoolExpression(p[1])

def p_expresion_zero(p):
    'expression : ZERO'
    p[0] = ZeroExpression(p[1])

def p_expression_variable(p):
    'expression : VARIABLE'
    p[0] = VariableExpression(p[1])

def p_expression_lambda(p):
    'expression : LAMBDA VARIABLE TWOPOINTS'
    p[0] = LambdaExpression(p[2])

def p_expression_if(p):
    'expression : IF expression THEN expression ELSE expression'
    p[0] = IfExpression(p[2], p[4], p[6])

def p_expression_succ(p):
  'expression : SUCC OPENPAREN expression CLOSEPAREN'
  p[0] = SuccExpression(p[3])

def p_expression_pred(p):
  'expression : PRED OPENPAREN expression CLOSEPAREN'
  p[0] = PredExpression(p[3])

def p_expression_izsero(p):
  'expression : ISZERO OPENPAREN expression CLOSEPAREN'
  p[0] = IszeroExpression(p[3])

def p_error(p):
    print("Hubo un error en el parseo.")

    parser.restart()


# Build the parser
parser = yacc.yacc(debug=True)

def apply_parser(str):
    return parser.parse(str)

