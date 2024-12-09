import pygame
from constants import NUM_ROW, NUM_COL, GRID_SIZE
from utils import init_utilities, init_policy
from value_iteration import perform_value_iteration
from policy_iteration import perform_policy_iteration
from draw import draw_grid

# Main display loop
def display():
    pygame.init()
    screen = pygame.display.set_mode((NUM_COL * GRID_SIZE, NUM_ROW * GRID_SIZE))
    font = pygame.font.SysFont(None, 24)
    clock = pygame.time.Clock()
    running = True

    # Initialize utilities and policy
    U = init_utilities()
    policy = init_policy()

    current_iteration = 0
    policy_stable = False

    while running:
        screen.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_v:
                    U = perform_value_iteration(U)
                    print(f"Value Iteration: Iteration {current_iteration}")
                    current_iteration += 1
                if event.key == pygame.K_p:
                    U, policy, policy_stable = perform_policy_iteration(U, policy)
                    print(f"Policy Iteration: Iteration {current_iteration}, is stable {policy_stable}")
                    current_iteration += 1
        draw_grid(screen, font, U, policy)
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    display()