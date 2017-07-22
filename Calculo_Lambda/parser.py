"""Parser LR(1) de calculadora."""
import ply.yacc as yacc
from .lexer import tokens
from expressions import BoolExpression, IfExpression, ZeroExpression, VariableExpression, LambdaExpression, ExpressionAndExpression, SuccExpression, PredExpression, iszeroExpression, BoolType, NatType, TypeAndType, ExpressionWithParen

start = 'expression'

def p_expression_lambda(p):
    'expression : LAMBDA VARIABLE TWOPOINTS type POINT expression'
    p[0] = LambdaExpression(p[2], p[4], p[6])

def p_expression_expression2(p):
    'expression : expression2'
    p[0] = p[1]

def p_expression2_if(p):
    'expression2 : IF expression THEN expression ELSE expression'
    p[0] = IfExpression(p[2], p[4], p[6])

def p_expression2_expression3(p):
    'expression2 : expression3'
    p[0] = p[1]

def p_expression3_expression4_expression5(p):
    'expression3 : expression4 expression5'
    p[0] = p[1] if p[2] == None else ExpressionAndExpression(p[1], p[2])

def p_expression5_expression(p):
    'expression5 : expression'
    p[0] = p[1]

def p_expression5_none(p):
    'expression5 :'
    p[0] = None

def p_expression4_succ(p):
    'expression4 : SUCC OPENPAREN expression CLOSEPAREN'
    p[0] = SuccExpression(p[3])

def p_expression4_pred(p):
    'expression4 : PRED OPENPAREN expression CLOSEPAREN'
    p[0] = PredExpression(p[3])

def p_expression4_izsero(p):
    'expression4 : ISZERO OPENPAREN expression CLOSEPAREN'
    p[0] = iszeroExpression(p[3])

def p_expression4_expression6(p):
    'expression4 : expression6'
    p[0] = p[1]

def p_expression6_true(p):
    'expression6 : TRUE'
    p[0] = BoolExpression(p[1])

def p_expression6_false(p):
    'expression6 : FALSE'
    p[0] = BoolExpression(p[1])

def p_expression6_zero(p):
    'expression6 : ZERO'
    p[0] = ZeroExpression(p[1])

def p_expression6_variable(p):
    'expression6 : VARIABLE'
    p[0] = VariableExpression(p[1])

def p_expression6_expression(p):
    'expression6 : OPENPAREN expression CLOSEPAREN'
    p[0] = ExpressionWithParen(p[2])

def p_type_bool(p):
    'type : BOOL T'
    p[0] = BoolType() if p[2] == None else TypeAndType(BoolType(), p[2])

def p_type_nat(p):
    'type : NAT T'
    p[0] = NatType() if p[2] == None else TypeAndType(NatType(), p[2])

def p_T_type(p):
    'T : ARROW type'
    p[0] = p[2]

def p_T_none(p):
    'T :'
    p[0] = None

def p_error(p):
    print("Hubo un error en el parseo.")
    parser.restart()

# Build the parser
parser = yacc.yacc(debug=True)

def apply_parser(str):
    return parser.parse(str)
