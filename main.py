"""Archivo principal de calculadora."""
from Calculo_Lambda import parse
from Calculo_Lambda.expressions import Error, Result

while True:
    try:
        exp_str = raw_input('calc> ')
    except EOFError:
        break

    result = parse(exp_str).calculate(dict())
    if isinstance(result, Error):
      print result.value
    else:
      print result.value.toString() + ':' + result.type.value()
