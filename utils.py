import random
import math
from constants import REWARD, DISCOUNT, NUM_ACTIONS, ACTIONS, WALL, TERMINALS, NUM_COL, NUM_ROW

# Initialize utilities and policy
def init_utilities():
    U = [[0 if (r, c) not in TERMINALS and (r, c) != WALL else TERMINALS.get((r, c), 0)
          for c in range(NUM_COL)] for r in range(NUM_ROW)]
    return U

def init_policy():
    policy = [[random.randint(0, 3) if (r, c) not in TERMINALS and (r, c) != WALL else -1
               for c in range(NUM_COL)] for r in range(NUM_ROW)]
    return policy

# Get the utility for a given state after taking an action
def getU(U, r, c, action):
    dr, dc = ACTIONS[action]
    newR, newC = r + dr, c + dc
    if newR < 0 or newC < 0 or newR >= NUM_ROW or newC >= NUM_COL or (newR, newC) == WALL:
        return U[r][c]
    return U[newR][newC]

# Calculate utility after taking an action at a state
def calculateU(U, r, c, action):
    u = REWARD
    u += 0.1 * DISCOUNT * getU(U, r, c, (action - 1) % 4)
    u += 0.8 * DISCOUNT * getU(U, r, c, action)
    u += 0.1 * DISCOUNT * getU(U, r, c, (action + 1) % 4)
    return u