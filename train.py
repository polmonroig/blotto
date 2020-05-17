# Blotto game is a simple game where you assing
# troops to battlefields
from random import random, randint
import numpy as np
import copy

# global constants
MAX_TROOPS = 100

# define actions
# Action -> number of troops to assign

class State:
    def __init__(self, size, available_troops=MAX_TROOPS):
        self.parent = None
        self.battlefields = [0] * size
        self.available_troops = available_troops

    def apply_action(self, troops):
        self.parent = copy.copy(self)
        for battlefield in self.battlefields:
            if battlefield == 0:
                battlefield = troops
                break
        self.available_troops -= troops

    def is_terminal(self):
        return self.available_troops == 0

class Agent:
    def __init__(self, n_states, e=0.2):
        self.value_state = [0] * n_states
        self.e_greedy = e

    def update(self, state):
        if state.is_terminal():
            return False
        troops = randint(1, state.available_troops)
        state.apply_action(troops)

        return True

    def update_values(self, state_a, state_b):
        pass


n_episodes = int(input("Enter number of episodes "))
n_battlefields = int(input("Enter number of battlefields "))
agent = Agent(n_battlefields)
for episode in range(n_episodes):
    print("Episode:", episode)
    # double update
    initial_state_a = State(n_battlefields)
    initial_state_b = State(n_battlefields)
    while agent.update(initial_state_a):
        pass
    print("Battlefields A:", initial_state_a.battlefields)
    while agent.update(initial_state_b):
        pass
    print("Battlefields B:", initial_state_b.battlefields)
    agent.update_values(initial_state_a, initial_state_b)
