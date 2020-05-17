# Blotto game is a simple game where you assing
# troops to battlefields
from random import random, randint
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
        for i in range(0, len(self.battlefields)):
            if self.battlefields[i] == 0:
                self.battlefields[i] = troops
                break
        self.available_troops -= troops

    def is_terminal(self):
        return self.available_troops == 0

# MAX_TROOPS == level width
class StateContainer:
    def __init__(self, n_battlefields, default):
        self.level = n_battlefields
        self.min_level = 1
        if self.is_leaf():
            self.values = [default] * MAX_TROOPS
        else:
            self.values = [StateContainer(n_battlefields - 1, default)] * MAX_TROOPS

    def get(self, i):
        return self.values[i- 1]

    def set(self, i, value):
        self.values[i - 1] = value

    def is_leaf(self):
        return self.level == self.min_level

class Agent:
    def __init__(self, n_battlefields, e=0.2):
        self.value_state = StateContainer(n_battlefields, 0)
        self.returns = StateContainer(n_battlefields, [])
        self.e_greedy = e
        self.discount = 0.1

    def update(self, state):
        if state.is_terminal():
            return False
        troops = randint(1, state.available_troops)
        state.apply_action(troops)

        return True

    @staticmethod
    def mean(array):
        m = 0
        for value in array:
            m += value
        return m / float(len(array))

    def change_state(self, state, episode_return):
        values = self.value_state
        returns = self.returns
        i = 0
        while not values.is_leaf():
            values = values.get(state.battlefields[i])
            returns = returns.get(state.battlefields[i])
        new_returns = returns.get(state.battlefields[i]) + [episode_return]
        returns.set(state.battlefields[i], new_returns)
        values.set(state.battlefields[i], Agent.mean(new_returns))



    def update_values(self, state_a, state_b):
        wins = 0
        for b1, b2 in zip(state_a.battlefields, state_b.battlefields):
            if b1 > b2:
                wins += 1
            elif b1 < b2:
                wins -= 1

        if wins > 0:
            print("Player A wins")
        elif wins < 0:
            wins = -wins
            print("Player B wins")
        else:
            print("There was a tie")
        reward_a = wins
        reward_b = -wins
        returns_a = 0
        returns_b = 0
        while state_a and state_b:
            returns_a = reward_a * self.discount + reward_a
            returns_b = reward_b * self.discount + reward_b
            self.change_state(state_a, returns_a)

            #self.change_state(state_b, returns_b)
            state_a = state_a.parent
            state_b = state_b.parent


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
