class Error(object):

    def __init__(self, value):
      self.value = value

class NotFound(object):

    def __init__(self, value):
      self.value = value

class Result(object):

    def __init__(self, value, typeOf):
      self.value = value
      self.type = typeOf

class BoolExpression(object):

    def __init__(self, value):
      self.value = True if value == 'true' else False
      self.type = BoolType('Bool')

    def evaluate(self, variable, value):
        return Result(self, self.type)

    def calculate(self, dicc):
        return Result(self, self.type)

    def toString(self):
        return 'true' if self.value == True else 'false'

class ZeroExpression(object):

    def __init__(self, value):
        self.value = int(value)
        self.type = NatType('Nat')

    def evaluate(self, variable, value):
        return Result(self, self.type)

    def calculate(self, dicc):
        return Result(self, self.type)

    def toString(self):
        return '0'

class VariableExpression(object):

    def __init__(self, variable):
        self.variable = variable
        self.type = None

    def evaluate(self, variable, value):
        if (self.variable != variable):
            return Result(self, self.type)
        else:
            return Result(value, self.type)

    def calculate(self, dicc):
        if self.variable in dicc.keys():
            self.type = dicc[self.variable]
            return Result(self, self.type)
        else:
            return Error('ERROR: El termino no es cerrado')

    def toString(self):
        return str(self.variable)

class LambdaExpression(object):

    def __init__(self, variable, typeOf, expression):
        self.variable = variable
        self.type = typeOf
        self.expression = expression

    def evaluate(self, value):
        #agregar cuando da error primero
        expression_result = self.expression.evaluate(self.variable, value)
        return expression_result

    def calculate(self, dicc):
        dicc[self.variable] = self.type
        expression_result = self.expression.calculate(dicc)
        if isinstance(expression_result, Error):
            return expression_result

        if isinstance(expression_result, NotFound):
            return Error("Error no esta declarado el tipo")

        self.expression = expression_result.value
        return Result(self, TypeAndType(self.type, expression_result.type))

    def toString(self):
        return "\\" + self.variable + ":" + self.type.value() + "." + self.expression.toString()

class IfExpression(object):

    def __init__(self, condition, true_condition, false_condition):
        self.condition = condition
        self.true_condition = true_condition
        self.false_condition = false_condition

    def evaluate(self, variable, value):
        true_condition_result = self.true_condition.evaluate(variable, value)
        false_condition_result = self.false_condition.evaluate(variable, value)
        if true_condition_result.type != false_condition_result.type:
            return Error('ERROR: Las dos opciones del if deben tener el mismo tipo')
        else:
            if self.condition.evaluate(variable, value):
                return Result(true_condition_result, true_condition_result.type)
            else:
                return Result(false_condition_result, false_condition_results.type)

    def calculate(self, dicc):
        true_condition_result = self.true_condition.calculate(dicc)
        false_condition_result = self.false_condition.calculate(dicc)
        if isinstance(true_condition_result, Error):
            return true_condition_result

        if isinstance(false_condition_result, Error):
            return false_condition_result

        if true_condition_result.type.value() != false_condition_result.type.value():
            return Error('ERROR: Las dos opciones del if deben tener el mismo tipo')
        else:
            self.true_condition = true_condition_result.value
            self.false_condition = false_condition_result.value
            self.condition = self.condition.calculate(dicc).value
            return Result(self, true_condition_result.type)

    def toString(self):
        return 'if ' + self.condition.toString() + ' then ' + self.true_condition.toString() + ' else ' + self.false_condition.toString()

class SuccExpression(object):

    def __init__(self, expression):
        self.expression = expression
        self.type = NatType('Nat')

    def evaluate(self, variable, value):
        if isinstance(value, NatType):
            return Result(self.expression.evaluate(variable, value).value + 1, self.type)
        else:
            return Error("ERROR: succ espera un valor de tipo Nat")

    def calculate(self, dicc):
        if isinstance(self.expression, PredExpression):
            subexpression_result = self.expression.expression.calculate(dicc)
            return Result(subexpression_result.value, subexpression_result.type )
        else:
            self.expression = self.expression.calculate(dicc).value
        return Result(self, self.type)

    def toString(self):
        return 'succ(' + self.expression.toString() + ')'

class PredExpression(object):

    def __init__(self, expression):
        self.expression = expression
        self.type = NatType('Nat')

    def evaluate(self, variable, value):
      if isinstance(value, NatType):
          return Result(self.expression.evaluate(variable, value) - 1, self.type)
      else:
          return Error("ERROR: pred espera un valor de tipo Nat")

    def calculate(self, dicc):
        self.expression = self.expression.calculate(dicc).value
        return Result(self, self.type)

    def toString(self):
        return 'pred(' + self.expression.toString() + ')'

class iszeroExpression(object):

    def __init__(self, expression):
        self.expression = expression
        self.type = BoolType('Bool')

    def evaluate(self, variable, value):
        if isinstance(value, NatType):
            return Result(self.expression.evaluate(variable, value) == 0, self.type)
        else:
            return Error("ERROR: iszero espera un valor de tipo Nat")


    def calculate(self, dicc):
        self.expression = self.expression.calculate(dicc).value
        return Result(self, self.type)

    def toString(self):
        return 'iszero(' + self.expression.toString() + ')'

class ExpressionAndExpression(object):

    def __init__(self, expression1, expression2):
        self.expression1 = expression1
        self.expression2 = expression2

    def calculate(self, dicc):
        expression1_result = self.expression1.calculate(dicc)
        expression2_result = self.expression2.calculate(dicc)
        if isinstance(expression1_result.type, TypeAndType):
            if expression1_result.type.type1.value() == expression2_result.type.value():
                return self.expression1.evaluate(expression2_result.value)
            else:
                Error("ERROR: La parte izquierda de la aplicacion no es una funcion con dominio en " + expression2_result.type.value())
        else:
          return Error("ERROR: La parte izquierda de la aplicacion no es una funcion con dominio en " + expression2_result.type.value())
            # if expression1_result.type.value() == expression2_result.type.value():
            #     return self.expression1.evaluate(expression2_result.value)
            # else:

class BoolType(object):

    def __init__(self, typeOf):
        self.type = typeOf

    def value(self):
        return self.type

class NatType(object):

    def __init__(self, typeOf):
        self.type = typeOf

    def value(self):
        return self.type

class TypeAndType(object):

    def __init__(self, typeOf1, typeOf2):
        self.type1 = typeOf1
        self.type2 = typeOf2

    def value(self):
        return self.type1.value() + '->' + self.type2.value()
