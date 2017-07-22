"""Archivo principal de calculo Lambda."""
from Calculo_Lambda import parse
from Calculo_Lambda.expressions import Error, Result, VariableExpression

while True:
    try:
        exp_str = raw_input('CLambda> ')
    except EOFError:
        break

    result = parse(exp_str).calculate()
    if isinstance(result, Error):
      print 'ERROR: ' + result.value
    else:
      if len(result.dic):
          print 'ERROR: ' + 'el termino no es cerrado'
      else:
          print 'OK: ' + result.value.toString() + ':' + result.type.value()
