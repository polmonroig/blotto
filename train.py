# Blotto game is a simple game where you assing
# troops to battlefields
from random import random
import numpy as np

# global constants
MAX_TROOPS = 100

# define actions
# Action -> number of troops to assign

class State:
    def __init__(self, size, available_troops=MAX_TROOPS):
        self.parent = None
        self.battlefields = np.array(size)
        self.available_troops = available_troops

    def apply_action(self, action):
        self.parent = self.copy()
        for battlefield in self.battlefields:
            if battlefield == 0:
                battlefield = action.troops
                break
        self.available_troops -= action.troops

    def is_terminal(self):
        return self.available_troops == 0

class Agent:
    def __init__(self, n_states, e=0.2):
        self.value_state = np.array(n_states)
        self.e_greedy = e

    def update(self, state):
        if state.is_terminal():
            return False

    def update_values(self, state_a, state_b):
        pass 


n_episodes = input("Enter number of episodes")
n_battlefields = input("Enter number of battlefields")
agent = Agent(n_battlefields)
for episode in range(n_episodes):
    print("Episode:", episode)
    # double update
    initial_state_a = State(n_battlefields)
    initial_state_b = State(n_battlefields)
    while agent.update(initial_state_a):
        pass
    while agent.update(initial_state_b):
        pass
    agent.update_values(initial_state_a, initial_state_b)
