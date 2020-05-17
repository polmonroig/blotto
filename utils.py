from random import randint


# global constants
MAX_TROOPS = 100

class Container:
    def __init__(self, n_battlefields, default=None, incremental=MAX_TROOPS+1):
        self.level = n_battlefields
        self.min_level = 1
        self.incremental = incremental
        self.values = []
        if self.is_leaf():
            if default is not None:
                self.values = [default] * incremental
            else:
                self.values = [randint(0, incremental-1)] * incremental
        else:
            for i in range(incremental):
                self.values.append(Container(n_battlefields - 1, default, incremental - i))

    def get(self, i):
        return self.values[i]

    def set(self, i, value):
        self.values[i] = value

    def is_leaf(self):
        return self.level == self.min_level
