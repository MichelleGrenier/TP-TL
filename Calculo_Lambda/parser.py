"""Parser LR(1) de calculadora."""
import ply.yacc as yacc
from .lexer import tokens
from expressions import BoolExpression, IfExpression, ZeroExpression, VariableExpression, LambdaExpression, ExpressionAndExpression, SuccExpression, PredExpression, iszeroExpression, BoolType, NatType, TypeAndType

precedence = [
    ('right', 'LAMBDA', 'VARIABLE', 'TWOPOINTS', 'POINT'),
    ('right', 'IF', 'THEN', 'ELSE'),
    # ('left', 'expression', 'expression'),
    ('right', 'SUCC', 'OPENPAREN', 'CLOSEPAREN'),
    ('right', 'ISZERO', 'OPENPAREN', 'CLOSEPAREN'),
    ('right', 'ZERO'),
    ('right', 'TRUE'),
    ('right', 'FALSE')
]

start = 'expression'

def p_expression_variable(p):
    'expression : VARIABLE'
    p[0] = VariableExpression(p[1])

def p_expression_true(p):
    'expression : TRUE'
    p[0] = BoolExpression(p[1])

def p_expresion_false(p):
    'expression : FALSE'
    p[0] = BoolExpression(p[1])

def p_expression_if(p):
    'expression : IF expression THEN expression ELSE expression'
    p[0] = IfExpression(p[2], p[4], p[6])

def p_expression_lambda(p):
    'expression : LAMBDA VARIABLE TWOPOINTS type POINT expression'
    p[0] = LambdaExpression(p[2], p[4], p[6])

def p_expression_lambda_with_paren(p):
    'expression : LAMBDA VARIABLE TWOPOINTS type POINT OPENPAREN expression CLOSEPAREN'
    p[0] = LambdaExpression(p[2], p[4], p[7])

def p_expression_lambda_with_paren2(p):
    'expression : OPENPAREN LAMBDA VARIABLE TWOPOINTS type POINT expression CLOSEPAREN'
    p[0] = LambdaExpression(p[3], p[5], p[7])

def p_expression_expression_expression(p):
    'expression : expression expression'
    p[0] = ExpressionAndExpression(p[1], p[2])

def p_expression_expression_expression_with_paren(p):
    'expression : OPENPAREN expression CLOSEPAREN expression'
    p[0] = ExpressionAndExpression(p[2], p[4])

def p_expression_expression_expression_with_paren(p):
    'expression : OPENPAREN expression CLOSEPAREN expression'
    p[0] = ExpressionAndExpression(p[2], p[4])

def p_expresion_zero(p):
    'expression : ZERO'
    p[0] = ZeroExpression(p[1])

def p_expression_succ(p):
    'expression : SUCC OPENPAREN expression CLOSEPAREN'
    p[0] = SuccExpression(p[3])

def p_expression_pred(p):
    'expression : PRED OPENPAREN expression CLOSEPAREN'
    p[0] = PredExpression(p[3])

def p_expression_izsero(p):
    'expression : ISZERO OPENPAREN expression CLOSEPAREN'
    p[0] = iszeroExpression(p[3])

def p_type_bool(p):
    'type : BOOL'
    p[0] = BoolType(p[1])

def p_type_nat(p):
    'type : NAT'
    p[0] = NatType(p[1])

def p_type_type_type(p):
    'type : type ARROW type'
    p[0] = TypeAndType(p[1], p[3])

def p_error(p):
    print("Hubo un error en el parseo.")
    parser.restart()

# Build the parser
parser = yacc.yacc(debug=True)

def apply_parser(str):
    return parser.parse(str)
