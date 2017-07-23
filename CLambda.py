#!/usr/bin/env python
"""Archivo principal de calculo Lambda."""
import sys
from Calculo_Lambda import parse
from Calculo_Lambda.expressions import Error, Result


if len(sys.argv) == 1:
    while(True):
        try:
            exp_str = raw_input('CLambda: ')
            result = parse(str(exp_str))
            if result != None:
                result = result.calculate()
                if isinstance(result, Error):
                    sys.stderr.write('ERROR: ' + result.value + '\n')
                else:
                    if len(result.dic):
                        sys.stderr.write('ERROR: El termino no es cerrado' + '\n')
                    else:
                        sys.stdout.write('OK: ' + result.value.toString() + ':' + result.type.value() + '\n')
        except EOFError:
            sys.stderr.write('1')
            break
else:
    exp_str = ''
    for exp in sys.argv[1:]:
        exp_str = exp_str + exp

result = parse(str(exp_str))
if result == None:
    sys.stderr.write('1 | Error en el parseo \n')
else:
    result = result.calculate()
    if isinstance(result, Error):
        sys.stderr.write('ERROR: ' + result.value + '\n')
    else:
        if len(result.dic):
            sys.stderr.write('ERROR: El termino no es cerrado' + '\n')
        else:
            sys.stdout.write('OK: ' + result.value.toString() + ':' + result.type.value() + '\n')
