# Grid World Value and Policy Iteration

### Overview
This project simulates a **Grid World** where an agent navigates the environment to maximize its expected rewards using **Value Iteration** and **Policy Iteration** algorithms. The agent's goal is to learn the optimal policy that dictates the best action to take in each state to maximize the long-term reward. The code also includes a graphical interface to visualize the grid, utilities, and policies.

### Project Collaborators
- Sohitha Sonalika 22110151
- Chinthala Shivamani 22110062
- Banavath Diraj 22110044
- Labish Bardiya 24120011
- Ishika Jain 24120009
- Prateek Goswami 24120016

---

### Project Setup

Before running the project, ensure you have Python and the necessary libraries installed.

#### Prerequisites
- Python 3.x
- Pygame library (`pip install pygame`)

---

### Core Concepts

#### Grid World
The agent operates in a **3x4 grid**, where each cell represents a state in the environment. The grid is designed as follows:

- **WALL**: Cells that are not accessible by the agent. These cells are static and cannot be visited.
- **TERMINALS**: Special cells with a terminal reward:
  - `(0, 3)` has a positive reward of `+1` (Goal state).
  - `(1, 3)` has a negative reward of `-1` (Obstacle state).

#### Value Iteration
Value Iteration is an algorithm to compute the optimal utilities (values) for each state in the grid. It uses the Bellman equation to iteratively update the utility values of all states until the difference between successive iterations is below a predefined threshold (error tolerance).

- Each state's utility is computed by considering all possible actions the agent can take from that state.
- The new utility value for a state is the maximum expected utility considering the reward and the discounted future utilities from neighboring states.

The Value Iteration process repeats until the **maximum error** between successive iterations is small enough (i.e., below `10^-5`).

#### Policy Iteration
Policy Iteration is an alternative to Value Iteration, which alternates between two phases:

1. **Policy Evaluation**: Given a policy, evaluate the utilities of each state based on the current policy.
2. **Policy Improvement**: Update the policy by selecting the action that maximizes the utility for each state.

The process continues until the policy stabilizes (i.e., no changes occur in the policy between iterations).

---

### Code Structure

1. **Constants**: Define essential parameters for the grid size, rewards, discount factor, and actions the agent can take.
    - `REWARD`: The reward for transitioning between states.
    - `DISCOUNT`: The discount factor applied to future rewards.
    - `NUM_ACTIONS`: Number of possible actions (4: Down, Left, Up, Right).
    - `ACTIONS`: List of possible movements (Down, Left, Up, Right).
    - `NUM_ROW`, `NUM_COL`: Grid dimensions.
    - `TERMINALS`: Positions of terminal states with their respective rewards.

2. **Utility Functions**:
    - `getU`: Returns the utility of a neighboring state based on the selected action.
    - `calculateU`: Calculates the utility of a state based on a specific action considering the rewards and future utilities of neighboring states.

3. **Core Functions**:
    - `perform_value_iteration`: Performs one iteration of value iteration.
    - `perform_policy_iteration`: Performs one iteration of policy iteration.
  
4. **Drawing and Visualization**:
    - `draw_grid`: Draws the grid environment using Pygame, visualizing:
        - The walls (gray cells).
        - The terminal states (green for positive reward, red for negative reward).
        - The utilities of each state (displayed numerically).
        - The agent's policy (arrows indicating the best action).

---

### Visualizing the Grid

The grid is drawn using the **Pygame** library. It shows:
- **Grid Cells**: Rectangular cells representing states.
- **Walls**: Cells where the agent cannot move.
- **Terminal States**: Green (positive reward) and red (negative reward) cells indicating special states.
- **Utilities**: Each cell shows its computed utility value (i.e., how valuable the state is in terms of long-term reward).
- **Policy**: Blue arrows indicate the best action from each state, based on the learned policy.

### Key Features:
- Press **`V`** to perform **Value Iteration** and update the utilities of all states.
- Press **`P`** to perform **Policy Iteration**, updating both the utilities and the policy.

---

### Usage

1. **Running the Code**:
    - Ensure Python and Pygame are installed.
    - Run the script in a terminal or IDE.
    - A Pygame window showing the grid and its current utilities and policies will open.
    
2. **Interacting with the Simulation**:
    - Press **`V`** to perform value iteration.
    - Press **`P`** to perform policy iteration.
    - Observe the changes in the grid as the agent's understanding of the environment improves.

---

### Acknowledgements

Special thanks to the following mentors for their support and guidance throughout this project:

- **Neeldhara Mishra** - For her invaluable mentorship and guidance.
- **Manisha Padala** - For her constant support and expertise.
