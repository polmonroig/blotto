# Blotto game is a simple game where you assing
# troops to battlefields
from agent import Agent
from state import State
import sys



n_wins_a = 0
n_wins_b = 0
sys.setrecursionlimit(10000)
# define actions
# Action -> number of troops to assign






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
    #initial_state_a.fill_empty()
    #initial_state_b.fill_empty()
    print("Battlefields A:", initial_state_a.battlefields)
    while agent.update(initial_state_b):
        pass
    print("Battlefields B:", initial_state_b.battlefields)
    agent.update_values(initial_state_a, initial_state_b)

print("Training done!")
while True:
    initial_state = State(n_battlefields, train=False)
    while agent.update(initial_state, train=True):
        pass
    player_battlefields = [0] * n_battlefields
    total = 100
    for i in range(len(player_battlefields)):
        player_battlefields[i] = int(input("Enter troops for battlefield " + str(i) + " "))
        total -= player_battlefields[i]
        print("Remaining soldiers:", total)

    player_state = State(n_battlefields)
    player_state.battlefields = player_battlefields
    initial_state.fill_empty()
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
