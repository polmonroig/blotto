# Blotto game is a simple game where you assing
# troops to battlefields
from enum import Enum
import numpy as np

# global constants
MAX_TROOPS = 100

# define actions
ActionType = Enum("ActionType", "Resign AssignTroops")

class Action:
    def __init__(self, action_type):
        self.type = action_type
        self.troops = 0
        self.battlefield = 0

    def add_troops(self, battlefield, troops):
        self.troops = troops
        self.battlefield = battlefield

class State:
    def __init__(self, size):
        self.battlefields = np.array(size)
        self.terminal = False

    def apply_action(self, action):
        if action.type == Actions.Resign:
            self.terminal = True
        else:
            self.battlefields[action.battlefield] = action.troops

    def is_terminal(self):
        return self.terminal

class Agent:
    def __init__(self, n_states):
        self.policy = np.array(n_states)

n_battlefields = input("Enter number of #battlefields")

# number of states equals n_battlefields
states = np.array(n_battlefields)
# n_actioned
