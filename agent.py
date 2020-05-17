from utils import Container
from state import State
from random import random, randint

class Agent:
    def __init__(self, n_battlefields, e=0.05):
        self.policy = Container(n_battlefields)# OK
        self.returns = Container(n_battlefields + 1, [])
        self.action_value = Container(n_battlefields + 1, 0)
        self.e_greedy = e
        self.discount = 0.1

    def update(self, state, train=True):
        if state.is_terminal():
            return False
        policy = self.policy
        i = 0
        while not policy.is_leaf():
            policy = policy.get(state.battlefields[i])
            i += 1
        p_greedy = random()
        if p_greedy < self.e_greedy and train:
            state.apply_action(randint(0, state.available_troops))
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
    def argmax(array):
        m = array[0]
        arg = 0
        for i, value in enumerate(array):
            if value > m:
                arg = i
                m = value
        return arg

    def change_state(self, state, episode_return):
        policy = self.policy
        action_value = self.action_value
        returns = self.returns
        i = 0


        while not policy.is_leaf():
            policy = policy.get(state.battlefields[i])
            action_value = action_value.get(state.battlefields[i])
            returns = returns.get(state.battlefields[i])
            i += 1

        action_value = action_value.get(state.action)
        returns = returns.get(state.action)


        new_returns = returns.get(state.battlefields[i]) + [episode_return]
        returns.set(state.battlefields[i], new_returns)
        action_value.set(state.battlefields[i], Agent.mean(new_returns))
        policy.set(state.battlefields[i], Agent.argmax(action_value.values))


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
        # start at T - 1
        state_a = state_a.parent
        state_b = state_b.parent
        while not state_a.is_initial() and not state_b.is_initial():
            returns_a = reward_a * self.discount + reward_a
            returns_b = reward_b * self.discount + reward_b
            self.change_state(state_a, returns_a)
            self.change_state(state_b, returns_b)
            state_a = state_a.parent
            state_b = state_b.parent
