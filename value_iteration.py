from utils import calculateU, getU
from constants import NUM_ACTIONS, TERMINALS, WALL, NUM_ROW, NUM_COL

# Perform Value Iteration and return updated utilities
def perform_value_iteration(U):
    nextU = [[u for u in row] for row in U]
    error = 0
    for r in range(NUM_ROW):
        for c in range(NUM_COL):
            if (r, c) in TERMINALS or (r, c) == WALL:
                continue
            nextU[r][c] = max(calculateU(U, r, c, action) for action in range(NUM_ACTIONS))
            error = max(error, abs(nextU[r][c] - U[r][c]))
    U = nextU
    return U