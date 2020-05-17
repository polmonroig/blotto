# Blotto game is a simple game where you assing
# troops to battlefields
from random import random, randint
import copy

# global constants
MAX_TROOPS = 100
n_wins_a = 0
n_wins_b = 0

# define actions
# Action -> number of troops to assign

class State:
    def __init__(self, size, available_troops=MAX_TROOPS):
        self.parent = None
        self.battlefields = [0] * size
        self.available_troops = available_troops
        self.action = None

    def apply_action(self, troops):
        self.parent = copy.copy(self)
        for i in range(0, len(self.battlefields)):
            if self.battlefields[i] == 0:
                self.battlefields[i] = troops
                break
        self.action = troops - 1
        self.available_troops -= troops

    def is_terminal(self):
        return self.available_troops == 0

    def is_initial(self):
        return self.action == None

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
        self.policy = StateContainer(n_battlefields, randint(1, MAX_TROOPS))
        self.returns = StateContainer(n_battlefields + 1, [])
        self.action_value = StateContainer(n_battlefields + 1, 0)
        self.e_greedy = e
        self.discount = 0.1

    def update(self, state, train=True):
        if state.is_terminal():
            return False
        policy = self.policy
        while not policy.is_leaf():
            policy = policy.get(state.battlefields[i])

        p_greedy = random()
        if p_greedy < e_greedy and train:
            state.apply_action(randint(1, state.available_troops))
        else:
            state.apply_action(policy.get(state.battlefields[i]))


        return True

    @staticmethod
    def mean(array):
        m = 0
        for value in array:
            m += value
        return m / float(len(array))

    @staticmethod
    def max(array):
        m = array[0]
        for value in array:
            if value > m:
                m = value
        return m

    def change_state(self, state, episode_return):
        policy = self.policy
        action_value = self.action_value
        returns = self.returns
        i = 0
        while not policy.is_leaf():
            policy = policy.get(state.battlefields[i])
            action_value = action_value.get(state.battlefields[i])
            returns = returns.get(state.battlefields[i])

        action_value = action_value.get(state.action)
        returns = returns.get(state.action)
        new_returns = returns.get(state.battlefields[i]) + [episode_return]
        returns.set(state.battlefields[i], new_returns)
        action_value.set(state.battlefields[i], Agent.mean(new_returns))
        policy.set(state.battlefields[i], Agent.max(new_returns))


    @staticmethod
    def get_winner(state_a, state_b):
        wins = 0
        for b1, b2 in zip(state_a.battlefields, state_b.battlefields):
            if b1 > b2:
                wins += 1
            elif b1 < b2:
                wins -= 1
        return wins

    def update_values(self, state_a, state_b):
        wins = Agent.get_winner(state_a, state_b)

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
        while not state_a.is_initial() and not state_b.is_initial():
            returns_a = reward_a * self.discount + reward_a
            returns_b = reward_b * self.discount + reward_b
            self.change_state(state_a, returns_a)
            self.change_state(state_b, returns_b)
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

print("Training done!")
while True:
    initial_state = State(n_battlefields)
    while agent.update(initial_state):
        pass
    player_battlefields = [0] * n_battlefields
    for i in range(len(player_battlefields)):
        player_battlefields[i] = int(input("Enter troops for battlefield " + str(i) + " "))


    player_state = State(n_battlefields)
    player_state.battlefields = player_battlefields
    wins = Agent.get_winner(initial_state, player_state)
    print("Player:", player_battlefields)
    print("AI:", initial_state.battlefields)
    if wins > 0:
        print("AI wins")
    elif wins < 0:
        wins = -wins
        print("Alan wins")
    else:
        print("There was a tie")
