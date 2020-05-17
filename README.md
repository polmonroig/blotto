# Colonel Blotto Monte Carlo Control
Colonel Blotto is a famous game introduced in 1921, two colonels simultaneously distribute troops 
between different battlefields. To approach this game a simple Reinforcement Learning AI has been 
implemented using an **On-Policy Monte Carlo Control with Exploring Starts**. 

# Implementation 
To train the **agent**, a number of **episodes** are generated,  for each **step** in every episode the 
agent plays with it self, thus it creates a positive and negative reward at the same time. The reward is 
only known after the end games, since you can only know it when the battlefield is full. To force the exploration 
on most states, the initial state of each episode is choosed randomly. The policy used at training is an 
e-greedy policy with e=0.1. Finally an improvement has been added, when after the episode ends if the 
battlefields are not full, they are filled. 

  
