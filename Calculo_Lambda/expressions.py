class Error(object):

    def __init__(self, value):
      self.value = value

class Result(object):

    def __init__(self, value, typeOf, dic):
      self.value = value
      self.type = typeOf
      self.dic = dic

class BoolExpression(object):

    def __init__(self, value):
      self.value = True if value == 'true' else False
      self.type = BoolType()

    def calculate(self):
        return Result(self, self.type, dict())

    def replace(self, variable, value):
        return self

    def toString(self):
        return 'true' if self.value else 'false'

class ZeroExpression(object):

    def __init__(self, value):
        self.value = int(value)
        self.type = NatType()

    def calculate(self):
        return Result(self, self.type, dict())

    def replace(self, variable, value):
        return self

    def toString(self):
        return '0'

class VariableExpression(object):

    def __init__(self, variable):
        self.variable = variable
        self.type = None

    def calculate(self):
      dic = dict()
      dic[self.variable] = self.type
      return Result(self, self.type, dic)

    def replace(self, variable, value):
        if variable == self.variable:
            return value
        else:
            return self

    def toString(self):
        return str(self.variable)

class LambdaExpression(object):

    def __init__(self, variable, typeOf, expression):
        self.variable = variable
        self.type = typeOf
        self.expression = expression

    def calculate(self):
        result = self.expression.calculate()
        if isinstance(result, Error):
            return result
        else:
            self.expression = result.value
            if self.variable in result.dic.keys():
                if result.dic[self.variable] == None:
                    return Result(self, TypeAndType(self.type, self.type), result.dic)
                else:
                    if self.type == result.dic[self.variable].value():
                        del result.dic[self.variable]
                        return Result(self, TypeAndType(self.type, result.type), result.dic)
                    else:
                        return Error('La variable tiene un tipo invalido')

            return Result(self, TypeAndType(self.type, result.type), result.dic)

    def replaceVariable(self, value):
        return self.expression.replace(self.variable, value)

    def replace(self, variable, value):
        return self.expression.replace(variable, value)

    def toString(self):
        return "\\" + self.variable + ":" + self.type.value() + "." + self.expression.toString()

class IfExpression(object):

    def __init__(self, condition, true_condition, false_condition):
        self.condition = condition
        self.true_condition = true_condition
        self.false_condition = false_condition

    def calculate(self):
        condition_result = self.condition.calculate()
        self.condition = condition_result.value
        true_condition_result = self.true_condition.calculate()
        self.true_condition = true_condition_result.value
        false_condition_result = self.false_condition.calculate()
        self.false_condition = false_condition_result.value

        if isinstance(condition_result, Error):
            return condition_result

        if isinstance(true_condition_result, Error):
            return true_condition_result

        if isinstance(false_condition_result, Error):
            return false_condition_result

        if true_condition_result.type == None:
            true_condition_result.type = false_condition_result.type
        else:
            if false_condition_result.type == None:
                false_condition_result.type = true_condition_result.type
            else:
                if true_condition_result.type.value() != false_condition_result.type.value():
                    return Error('Los dos resultados posibles del if tienen que ser del mismo tipo')
        # Si el type es None entonces es porque hay una variable que tiene que ser boolean
        # De las unicas que no sabemos el output type es cuando es una variable o un if
        if condition_result.type == None:
            condition_result.type = BoolType()
            for key in condition_result.dic.keys():
                if condition_result.dic[key] == None:
                    condition_result.dic[key] == BoolType()
        else:
            # si es None entonces es un TypeAndType
            outputType = condition_result.type.outputType()
            if outputType == None:
                condition_result.type.updateType(BoolType())
                for key in condition_result.dic.keys():
                    if condition_result.dic[key] == None:
                        condition_result.dic[key] == BoolType()
            else:
                if not isinstance(outputType, BoolType):
                    return Error('La condicion debe ser un boolean')

                if isinstance(condition_result, BoolExpression):
                    return true_condition_result if condition_result.value.value else false_condition_result

        newDic = dict()
        newDic.update(condition_result.dic)
        newDic.update(false_condition_result.dic)
        newDic.update(true_condition_result.dic)
        return Result(self, true_condition_result.type, newDic)

    def replace(self, variable, value):
        self.condition = self.condition.replace(variable, value)
        self.true_condition = self.true_condition.replace(variable, value)
        self.false_condition = self.false_condition.replace(variable, value)
        return self

    def toString(self):
        return 'if ' + self.condition.toString() + ' then ' + self.true_condition.toString() + ' else ' + self.false_condition.toString()

class SuccExpression(object):

    def __init__(self, expression):
        self.expression = expression
        self.type = NatType()

    def calculate(self):
        expression_result = self.expression.calculate()
        self.expression = expression_result.value
        if isinstance(expression_result, Error):
            return expression_result

        # si la expression tiene tipo None entonces hay una variable de la cual
        # no sabemos el tipo
        if expression_result.type == None:
            expression_result.type = NatType()
            for key in expression_result.dic.keys():
                if expression_result.dic[key] == None:
                    expression_result.dic[key] == NatType()
            return Result(self, NatType(), expression_result.dic)
        else:
            outputType = expression_result.type.outputType()
            if outputType == None:
                condition_result.type.updateType(NatType())
                for key in expression_result.dic.keys():
                    if expression_result.dic[key] == None:
                        expression_result.dic[key] == NatType()
            else:
                if not isinstance(outputType, NatType):
                    return Error('La expression dentro de suc debe ser un Nat')
                else:
                    if isinstance(expression_result.value, PredExpression):
                        return expression_result.value.expression.calculate()
                    else:
                        return Result(self, self.type, expression_result.dic)

    def replace(self, variable, value):
        self.expression = self.expression.replace(variable, value)
        return self

    def toString(self):
        return 'succ(' + self.expression.toString() + ')'

class PredExpression(object):

    def __init__(self, expression):
        self.expression = expression
        self.type = NatType()

    def calculate(self):
        expression_result = self.expression.calculate()
        self.expression = expression_result.value
        if isinstance(expression_result, Error):
            return expression_result

        # si la expression tiene tipo None entonces hay una variable de la cual
        # no sabemos el tipo
        if expression_result.type == None:
            expression_result.type = NatType()
            for key in expression_result.dic.keys():
                if expression_result.dic[key] == None:
                    expression_result.dic[key] == NatType()
        else:
            outputType = expression_result.type.outputType()
            if outputType == None:
                condition_result.type.updateType(NatType())
                for key in expression_result.dic.keys():
                    if expression_result.dic[key] == None:
                        expression_result.dic[key] == NatType()
            else:
                if not isinstance(outputType, NatType):
                    return Error('La expression dentro de suc debe ser un Nat')
                else:
                    if isinstance(expression_result.value, SuccExpression):
                        return expression_result.value.expression
                    else:
                        return Result(self, self.type, expression_result.dic)

    def replace(self, variable, value):
        self.expression = self.expression.replace(variable, value)
        return self

    def toString(self):
        return 'pred(' + self.expression.toString() + ')'

class iszeroExpression(object):

    def __init__(self, expression):
        self.expression = expression
        self.type = BoolType()

    def calculate(self):
        expression_result = self.expression.calculate()
        self.expression = expression_result.value
        if isinstance(expression_result, Error):
            return expression_result

        # si la expression tiene tipo None entonces hay una variable de la cual
        # no sabemos el tipo
        if isinstance(expression_result, ZeroExpression):
            return Result(BoolExpression('True'), BoolType(), expression_result.dic)
        else:
            if expression_result.type != None:
                return Result(BoolExpression('False'), BoolType(), expression_result.dic)

            return Result(self, self.type, expression_result.dic)

    def replace(self, variable, value):
        self.expression = self.expression.replace(variable, value)
        return self

    def toString(self):
        return 'iszero(' + self.expression.toString() + ')'

class ExpressionAndExpression(object):

    def __init__(self, expression1, expression2):
        self.expression1 = expression1
        self.expression2 = expression2

    def calculate(self):
        expression1_result = self.expression1.calculate()
        expression2_result = self.expression2.calculate()

        if isinstance(expression1_result, Error):
            return expression1_result

        if isinstance(expression2_result, Error):
            return expression2_result

        if not isinstance(expression1_result.value, LambdaExpression):
            return Error('La primera expression no tiene como dominio al tipo de la segunda')

        if expression1_result.type.type1.value() == expression2_result.type.value():
            return expression1_result.value.replaceVariable(expression2_result.value).calculate()
        else:
            return Error("ERROR: La parte izquierda de la aplicacion no es una funcion con dominio en " + expression2_result.type.value())

class BoolType(object):

    def __init__(self):
        self.type = 'Bool'

    def value(self):
        return self.type

    def outputType(self):
        return self

class NatType(object):

    def __init__(self):
        self.type = 'Nat'

    def value(self):
        return self.type

    def outputType(self):
        return self

class TypeAndType(object):

    def __init__(self, typeOf1, typeOf2):
        self.type1 = typeOf1
        self.type2 = typeOf2

    def value(self):
        return self.type1.value() + '->' + self.type2.value()

    def outputType(self):
        return self.type2.outputType()

    def updateType(self, typeOf):
        if self.type2 == None:
            return TypeAndType(self.type1, typeOf)
        else:
            return TypeAndType(self.type1, self.type2.updateType(typeOf))
