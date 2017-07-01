"""Archivo principal de calculadora."""
from Calculo_Lambda import parse
from Calculo_Lambda.expressions import Error, Result

while True:
    try:
        exp_str = raw_input('calc> ')
    except EOFError:
        break

    result = parse(exp_str).calculate()
    if isinstance(result, Error):
      print result.value
    else:
      print(str(result.value) + ':' + str(parse(exp_str).typeOf()))
