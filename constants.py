# Constants for the grid world
REWARD = -0.2
DISCOUNT = 0.99
MAX_ERROR = 10**(-5)
NUM_ACTIONS = 4
ACTIONS = [(1, 0), (0, -1), (-1, 0), (0, 1)]  # Down, Left, Up, Right
NUM_ROW, NUM_COL = 3, 4
GRID_SIZE = 100
WALL = (1, 1)
TERMINALS = {(0, 3): 1, (1, 3): -1}