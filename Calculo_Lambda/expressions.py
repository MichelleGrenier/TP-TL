class Error(object):

    def __init__(self, value):
      self.value = value

class NotFound(object):

    def __init__(self, value):
      self.value = value

class Result(object):

    def __init__(self, value):
      self.value = value

class BoolExpression(object):

    def __init__(self, value):
      self.value = value
      self.type = 'Bool'

    def evaluate(self):
        return Result(True if value == 'true' else False)

    def calculate(self):
        return Result(self.value)

    def typeOf(self):
        return self.type

class ZeroExpression(object):

    def __init__(self, value):
        self.value = int(value)
        self.type = 'Nat'

    def evaluate(self):
        return Result(self.value)

    def calculate(self):
        return self.evaluate()

    def typeOf(self):
        return self.type

class VariableExpression(object):

    def __init__(self, variable):
        self.variable = variable

    def typeOf(self):
        return NotFound(self.variable)

    def evaluate(self, value):
        return Result(value)

    def calculate(self):
        return Result(self.variable)

class LambdaExpression(object):

    def __init__(self, variable, typeOf, expression):
        self.variable = variable
        self.type = typeOf
        self.expression = expression

    def evaluate(self, value):
        return self.expression.evaluate(value)

    def typeOf(self):
        if isinstance(self.expression.typeOf(), NotFound):
            return self.type.value() + '->' + self.type.value()
        else:
            return self.type.value() + '->' + self.expression.typeOf()

    def calculate(self):
        return Result('\\' + self.variable.calculate().value + ':' + self.type.value() + '.' + self.expression.calculate().value)

class IfExpression(object):

    def __init__(self, condition, true_condition, false_condition):
        self.condition = condition
        self.true_condition = true_condition
        self.false_condition = false_condition

    def evaluate(self, value):
        if self.true_condition.typeOf() != self.false_condition.typeOf():
          return Error('ERROR: Las dos opciones del if deben tener el mismo tipo')
        else:
          if self.condition.evaluate(value):
            return Result(self.true_condition.evaluate(value))
          else:
            return Result(self.false_condition.evaluate(value))

    def typeOf(self):
        return self.false_condition.typeOf()

    def calculate(self):
        if self.true_condition.typeOf() != self.false_condition.typeOf():
            return Error('ERROR: Las dos opciones del if deben tener el mismo tipo')
        else:
            return Result('if ' + str(self.condition.calculate().value) + ' then ' + str(self.true_condition.calculate().value) + ' else ' + str(self.false_condition.calculate().value))

class SuccExpression(object):

    def __init__(self, expression):
        self.expression = expression
        self.type = 'Nat'

    def calculate(self):
        return Result('succ(' + str(self.expression.calculate().value) + ')')

    def evaluate(self, value):
        if isinstance(value, int):
            return Result(self.expression.evaluate(value).value + 1)
        else:
            return Error('ERROR: succ espera un valor de tipo Nat')

    def typeOf(self):
        return self.type

class PredExpression(object):

    def __init__(self, expression):
        self.expression = expression
        self.type = 'Nat'

    def evaluate(self, value):
        return Result(self.expression.evaluate(value) - 1)

    def typeOf(self):
        return self.type

    def calculate(self):
        return Result('pred(' + str(self.expression.calculate().value) + ')')

class IszeroExpression(object):

    def __init__(self, expression):
        self.expression = expression
        self.type = 'Bool'

    def evaluate(self, value):
        return Result(self.expression.evaluate(value) == 0)

    def typeOf(self):
        return self.type

    def calculate(self):
        return 'iszero(' + self.expression.calculate().value + ')'

class ExpressionAndExpression(object):

    def __init__(self, expression1, expression2):
        self.expression1 = expression1
        self.expression2 = expression2

    def calculate(self):
        return self.expression1.evaluate(self.expression2.calculate().value)

    def typeOf(self):
        return self.expression1.typeOf()

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
        return self.type
