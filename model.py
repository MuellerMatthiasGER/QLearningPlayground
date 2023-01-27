import numpy as np

class Model:
    def __init__(self, agent) -> None:
        self.env = Environment()
        self.agent = agent

class Environment:
    def __init__(self, n_rows=3, n_cols=5) -> None:
        self.n_rows = n_rows
        self.n_cols = n_cols

        # There are different kind of tiles:
        # empty (-), ground (#), goal (G), apple (A) 
        self.tiles = np.full((n_rows, n_cols), '-')
        self.tiles[0, 1:self.n_cols - 1] = '#'
        self.tiles[0, n_cols - 1] = 'G'
        self.rewards = {'-': -1, '#': -100, 'G': 100, 'A': 50}