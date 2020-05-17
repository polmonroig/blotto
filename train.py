# Blotto game is a simple game where you assing
# troops to battlefields
from enum import Enum
import numpy as np

# global constants
MAX_TROOPS = 100

# define actions
actions = Enum("Resign", "AssignTroops")

class Action:
    def __init__(self, action_type):
        self.type = action_type

class State:
    def __init__(self, size):
        self.battlefields = np.array(size)

    def apply_action(self, action):


n_battlefields = input("Enter number of #battlefields")

# number of states equals n_battlefields
states = np.array(n_battlefields)
# n_actioned
