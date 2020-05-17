from utils import MAX_TROOPS
from random import randint
import copy

class State:
    def __init__(self, size, available_troops=MAX_TROOPS, train=True):
        self.parent = None
        self.battlefields = [0] * size
        if train:
            self.battlefields[0] = randint(0, 50)
        else:
            self.battlefields[0] = 0
        self.available_troops = available_troops-self.battlefields[0]
        self.action = None

    def apply_action(self, troops):
        self.parent = copy.deepcopy(self)
        for i in range(0, len(self.battlefields)):
            if self.battlefields[i] == 0:
                self.battlefields[i] = troops
                break
        self.parent.action = troops - 1
        self.available_troops -= troops

    def not_empty(self):
        for value in self.battlefields:
            if value == 0:
                return False
        return True

    def fill_empty(self):
        m = 500
        arg = 0
        for i, value in enumerate(self.battlefields):
            if value < m:
                m = value
                arg = i
        self.battlefields[arg]+= self.available_troops

    def is_terminal(self):
        return self.available_troops == 0 or self.not_empty()

    def is_initial(self):
        return self.parent == None
