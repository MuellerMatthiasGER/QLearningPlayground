import numpy as np
from agents import Agent

class Model:
    def __init__(self) -> None:
        self.env = Environment()
        self.agent = Agent(self.env)

    def next_step(self):
        self.agent.next_step()

    def next_iteration(self):
        terminated = False
        while not terminated:
            terminated = self.agent.next_step()

    def reset(self):
        self.agent = Agent(self.env)

class Environment:
    def __init__(self, n_rows=5, n_cols=5) -> None:
        self.n_rows = n_rows
        self.n_cols = n_cols

        # There are different kind of tiles:
        # empty (-), ground (#), goal (G), apple (A) 
        self.tiles = np.full((n_rows, n_cols), '-')
        self.tiles[0, 1:self.n_cols - 1] = '#'
        self.tiles[0, n_cols - 1] = 'G'
        self.tiles[n_rows - 1, n_cols - 1] = 'G'
        self.rewards = {'-': -1, '#': -10, 'G': 10, 'A': 0}
        self.termination_tiles = ['#', 'G']

    def get_reward(self, y, x):
        return self.rewards[self.tiles[y, x]]
    
    def is_termination_state(self, y, x):
        return self.tiles[y, x] in self.termination_tiles