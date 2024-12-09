from utils import calculateU
from constants import NUM_ACTIONS, WALL, TERMINALS, NUM_ROW, NUM_COL

# Perform Policy Iteration and return updated utilities and policy
def perform_policy_iteration(U, policy):
    policy_stable = True
    nextU = [[u for u in row] for row in U]

    # Policy Evaluation
    for r in range(NUM_ROW):
        for c in range(NUM_COL):
            if (r, c) in TERMINALS or (r, c) == WALL:
                continue
            nextU[r][c] = calculateU(U, r, c, policy[r][c])
    U = nextU

    # Policy Improvement
    for r in range(NUM_ROW):
        for c in range(NUM_COL):
            if (r, c) in TERMINALS or (r, c) == WALL:
                continue
            maxAction, maxU = max(
                ((action, calculateU(U, r, c, action)) for action in range(NUM_ACTIONS)),
                key=lambda x: x[1])
            if maxU > calculateU(U, r, c, policy[r][c]):
                policy[r][c] = maxAction
                policy_stable = False

    return U, policy, policy_stable