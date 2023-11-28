import numpy as np

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

class Agent:
    def __init__(self, env) -> None:
        self.env = env

        self.x = 0
        self.y = 0
        self.prev_x = -1
        self.prev_y = -1
        self.qtable = np.full((env.n_rows, env.n_cols, 4), 0, dtype='f')
        self.qtable[0, :, UP] = np.nan
        self.qtable[:, -1, RIGHT] = np.nan
        self.qtable[-1, :, DOWN] = np.nan
        self.qtable[:, 0, LEFT] = np.nan

        self.alpha = 0.5
        self.gamma = 0.5
        self.epsilon = 0.2

        self.policy_fn = self.softmax_direction

    def next_step(self) -> bool:
        """ 
        Executes one q-learning step

        Returns 
        -------
        bool:
            True if termination state has been reached
        """
        if self.env.is_termination_state(self.y, self.x):
            self.x = 0
            self.y = 0
            self.prev_x = -1
            self.prev_y = -1
            return True

        direction = self.policy_fn()
        self.move(direction)
        self.update_qvalue(direction)

        return False

    def epsilon_greedy_direction(self) -> int:
        direction = -1

        # epsilon greedy
        if np.random.random() < self.epsilon:
            # pick random move
            direction = np.random.choice(4)
            while np.isnan(self.qtable[self.y, self.x, direction]):
                direction = np.random.choice(4)
        else:
            # pick best move
            direction = np.nanargmax(self.qtable[self.y, self.x, :])

        return direction
    
    def softmax_direction(self) -> int:
        q_values = self.qtable[self.y, self.x, :].copy()
        
        # Normalize
        q_values -= np.nanmin(q_values)
        if np.nanmax(q_values) != 0:
            q_values /= np.nanmax(q_values)

        # Softmax
        q_values = np.exp(q_values)
        q_values = np.nan_to_num(q_values)
        probs = q_values / sum(q_values)

        return np.random.choice(4, p=probs)


    def move(self, direction: int) -> None:
        self.prev_x = self.x
        self.prev_y = self.y

        if direction == UP:
            self.y -= 1
        elif direction == RIGHT:
            self.x += 1
        elif direction == DOWN:
            self.y += 1
        elif direction == LEFT:
            self.x -= 1
        else:
            print("ERROR: Invalid direction")

    def update_qvalue(self, direction: int) -> None:
        reward = self.env.get_reward(self.y, self.x)
        old_qvalue = self.qtable[self.prev_y, self.prev_x, direction]
        best_next_qvalue = np.nanmax(self.qtable[self.y, self.x, :])

        new_qvalue = (1 - self.alpha) * old_qvalue + self.alpha * (reward + self.gamma * best_next_qvalue)
        self.qtable[self.prev_y, self.prev_x, direction] = new_qvalue

