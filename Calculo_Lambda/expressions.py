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
        self.type = NoneType(variable)

    def calculate(self):
      dic = dict()
      dic[self.variable] = self.type
      return Result(self, self.type, dic)

    def replace(self, variable, value):
        return value if variable == self.variable else self

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

        self.expression = result.value
        # si la variable que se declara es usada en la expression entonces tenemos
        # que hacer chequeo de tipos.
        if self.variable in result.dic.keys():
            # si no sabemos el tipo de la expression es porque hay una o varias
            # variables de las cuales no se sabe su tipo.
            if isinstance(result.dic[self.variable], NoneType):
                # podemos actualizar el tipo de la expression ya que ahora
                # sabemos el tipo de la variable que se esta declarando ahora.
                result.type = result.type.updateType(self.variable, self.type)
            # si sabemos el tipo que tiene que ser la variable, chequeamos que
            # se corresponda con lo que se declaro
            else:
                # si los tipos son distintos entonces es un error
                if result.dic[self.variable].value() != self.type.value():
                    return Error('La expresion esperaba un valor de tipo ' + result.type.value())
            # si pasaron los chequeos de tipo entonces ya puedo eliminar del diccionario
            del result.dic[self.variable]
        else:
            self
            # si la variable no se usa es porque no se usa nunca la variable o
            # porque fue dos veces declarada la variable y se la elimino por un declaracion
            # mas interna. Eso es error tambien?

        return Result(self, TypeAndType(self.type, result.type), result.dic)

    def replaceVariable(self, value):
        return self.expression.replace(self.variable, value)

    def replace(self, variable, value):
        self.expression.replace(variable, value)
        return self

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

        if isinstance(condition_result, Error): return condition_result
        if isinstance(true_condition_result, Error): return true_condition_result
        if isinstance(false_condition_result, Error): return false_condition_result

        # los tipos de los resultados del if tienen que ser del mismo tipos
        # si no sabemos el de alguno, entnces sabemos que debe ser igual
        # al tipo de la otra condicion. Pero si el tipo de alguno es de tipo
        # TypeAndType, nada mas nos interesa el tipo de la salida.
        outputType_true = true_condition_result.type.outputType()
        outputType_false = false_condition_result.type.outputType()
        if isinstance(outputType_true, NoneType):
            # el noneType lleva asociada una variable entonces actualizamos
            # el tipo de la expresion y el de la variable
            true_condition_result.dic[outputType_true.variable] = outputType_false
            true_condition_result.type = outputType_false
            outputType_true = outputType_false

        if isinstance(outputType_false, NoneType):
            # el noneType lleva asociada una variable entonces actualizamos
            # el tipo de la expresion y el de la variable
            false_condition_result.dic[outputType_false.variable] = outputType_true
            false_condition_result.type = outputType_true
            outputType_false = outputType_true

        if outputType_true.value() != outputType_false.value():
            return Error('Las dos opciones del if deben tener el mismo tipo')

        # Si no sabemos el tipo del output de la condicion, entonces actualizamos
        # esa variable con un bolean.
        outputType_condition = condition_result.type.outputType()
        if isinstance(outputType_condition, NoneType):
            condition_result.dic[outputType_condition.variable] = BoolType()
            condition_result.type = BoolType()
        else:
            # si el tipo no es un boolean entonces error
            if not isinstance(outputType_condition, BoolType):
                return Error('La condicion debe ser un boolean')

            # si la condicion es una BoolExpression entonces retorno el resultado adecuado
            if isinstance(condition_result.value, BoolExpression):
                return true_condition_result if condition_result.value.value else false_condition_result

        # si no cumple ninguna de las anteriores entonces junto todos los diccionarios y continuo
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
        if isinstance(expression_result, Error): return expression_result

        # si la expression tiene como output un tipo None
        outputType_expression = expression_result.type.outputType()
        if isinstance(outputType_expression, NoneType):
            # le asignamos Nat a la variable asociada a ese NoneType
            expression_result.dic[outputType_expression.variable] = NatType()
        else:
            # si la expresion no es de tipo Nat
            if not isinstance(outputType_expression, NatType): return Error('succ espera un valor de tipo Nat')
        #si la expression es de tipo pred cancelo el suc con el pred
        if isinstance(expression_result.value, PredExpression):
            return Result(expression_result.value.expression, self.type, expression_result.dic)

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
        if isinstance(expression_result, Error): return expression_result

        # si la expression tiene como output un tipo None
        outputType_expression = expression_result.type.outputType()
        if isinstance(outputType_expression, NoneType):
            # le asignamos Nat a la variable asociada a ese NoneType
            expression_result.dic[outputType_expression.variable] = NatType()

        # si la expresion es de tipo Bool
        if isinstance(outputType_expression, BoolType): return Error('pred espera un valor de tipo Nat')

        if isinstance(expression_result.value, ZeroExpression):
            return Result(ZeroExpression('0'), self.type, expression_result.dic)

        #si la expression es de tipo succ cancelo el pred con el succ
        if isinstance(expression_result.value, SuccExpression): return Result(expression_result.value.expression, self.type, expression_result.dic)

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
        if isinstance(expression_result, Error): return expression_result

        if isinstance(expression_result.type.outputType(), NoneType):
            return Result(self, self.type, expression_result.dic)

        if isinstance(expression_result.type.outputType(), BoolType):
            return Result(BoolExpression('false'), self.type, expression_result.dic)

        if isinstance(expression_result.type.outputType(), NatType):
            if isinstance(expression_result.value, ZeroExpression):
                return Result(BoolExpression('true'), self.type, expression_result.dic)

            return Result(BoolExpression('false'), self.type, expression_result.dic)

    def replace(self, variable, value):
        self.expression = self.expression.replace(variable, value)
        return self

    def toString(self):
        return 'iszero(' + self.expression.toString() + ')'

class ExpressionWithParen(object):

    def __init__(self, expression):
        self.expression = expression

    def calculate(self):
        result = self.expression.calculate()
        self.expression = result.value
        if isinstance(result, Error):
            return result

        return Result(self, result.type, result.dic)

    def toString(self):
        return '(' + self.expression.toString() + ')'

    def replace(self, variable, value):
        self.expression = self.expression.replace(variable, value)
        return self

class ExpressionAndExpression(object):

    def __init__(self, expression1, expression2):
        self.expression1 = expression1
        self.expression2 = expression2

    def calculate(self):
        if isinstance(self.expression2, ExpressionAndExpression):
            expression_result = ExpressionAndExpression(self.expression1, self.expression2.expression1).calculate()
            if isinstance(expression_result, Error):
                return expression_result
            return ExpressionAndExpression(expression_result.value, self.expression2.expression2).calculate()

        expression1_result = self.expression1.calculate()
        self.expression1 = expression1_result.value
        expression2_result = self.expression2.calculate()
        self.expression2 = expression2_result.value

        if isinstance(expression1_result, Error): return expression1_result
        if isinstance(expression2_result, Error): return expression2_result

        # # la parte de la izquiera tiene que ser una funciona lambda o una variable
        # # que en el futuro va a tomar una funcion lambda
        if isinstance(expression1_result.value, VariableExpression):
            # junto los diccionarios y contnuo ya que no tenemos mas informacion
            newDic = dict()
            newDic.update(expression1_result.dic)
            newDic.update(expression2_result.dic)
            return Result(self, expression2_result.type, newDic)

        if isinstance(expression1_result.value, ExpressionWithParen):
            return ExpressionAndExpression(expression1_result.value.expression, expression2_result.value).calculate()

        if not isinstance(expression1_result.value, LambdaExpression):
            return Error('La parte izquierda de la aplicacion no es una funcion con dominio en ' + expression2_result.type.value())

        # el inputType de una lambda expression siempre lo conocemos
        inputType_expression1 = expression1_result.type.inputType()
        outputType_expression2 = expression2_result.type.inputType()

        if isinstance(outputType_expression2, NoneType):
            expression2_result.dic[outputType_expression2.variable] = inputType_expression1
        else:
            if inputType_expression1.value() != outputType_expression2.value():
                return Error("La parte izquierda de la aplicacion no es una funcion con dominio en " + expression2_result.type.value())

        return expression1_result.value.replaceVariable(expression2_result.value).calculate()

    def toString(self):
        return self.expression1.toString() + ' ' + self.expression2.toString()

    def replace(self, variable, value):
        self.expression1 = self.expression1.replace(variable, value)
        self.expression2 = self.expression2.replace(variable, value)
        return self

class BoolType(object):

    def __init__(self):
        self.type = 'Bool'

    def value(self):
        return self.type

    def outputType(self):
        return self

    def updateType(self, variable, type):
        return self

    def inputType(self):
        return self

class NatType(object):

    def __init__(self):
        self.type = 'Nat'

    def value(self):
        return self.type

    def outputType(self):
        return self

    def updateType(self, variable, type):
        return self

    def inputType(self):
        return self

class TypeAndType(object):

    def __init__(self, typeOf1, typeOf2):
        self.type1 = typeOf1
        self.type2 = typeOf2

    def value(self):
        type1 = self.type1.value()
        type2 = self.type2.value()

        if isinstance(self.type1, TypeAndType):
            type1 = '(' + type1 + ')'

        if isinstance(self.type2, TypeAndType):
            type2 = '(' + type2 + ')'

        return type1 + '->' + type2

    def outputType(self):
        return self.type2.outputType()

    def inputType(self):
        return self.type1.inputType()

    def updateType(self, variable, typeOf):
        self.type1 = self.type1.updateType(variable, typeOf)
        self.type2 = self.type2.updateType(variable, typeOf)
        return self

class NoneType(object):

    def __init__(self, variable):
        self.variable = variable

    def updateType(self, variable, typeOf):
        return typeOf if variable == self.variable else self

    def value(self):
        return None

    def outputType(self):
        return self

    def inputType(self):
        return self
