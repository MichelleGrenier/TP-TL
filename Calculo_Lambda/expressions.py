class BoolExpression(object):

    def __init__(self, val):
        if val == 'true':
            self.val = True
        else:
            self.val = False

    def evaluate(self):
        return self.val

class ZeroExpression(object):

    def __init__(self, val):
        self.val = val

    def evaluate(self):
        return self.val

class VariableExpression(object):

    def __init__(self, val):
        self.val = val

class LambdaExpression(object):

    def __init__(self, variable):
        self.variable = variable

class IfExpression(object):

    def __init__(self, condition, true_condition, false_condition):
        self.cond = condition
        self.true_cond = true_condition
        self.false_cond = false_condition

    def evaluate(self):
        if self.cond.evaluate():
          return self.true_cond.evaluate()
        else:
          return self.false_cond.evaluate()

class SuccExpression(object):

    def __init__(self, expression):
        self.exp = expression

    def evaluate(self):
      return self.exp.evaluate() + 1

class PredExpression(object):

    def __init__(self, expression):
        self.exp = expression

    def evaluate(self):
      return self.exp.evaluate() - 1

class IszeroExpression(object):

    def __init__(self, expression):
        self.exp = expression

    def evaluate(self):
      return self.exp.evaluate() == 0
