import pygame
import math
from constants import NUM_ROW, NUM_COL, GRID_SIZE, WALL, TERMINALS, ACTIONS

# Draw the grid and policy
def draw_grid(screen, font, U, policy):
    for r in range(NUM_ROW):
        for c in range(NUM_COL):
            rect = pygame.Rect(c * GRID_SIZE, r * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(screen, (200, 200, 200), rect)
            pygame.draw.rect(screen, (0, 0, 0), rect, 1)

            if (r, c) == WALL:
                pygame.draw.rect(screen, (50, 50, 50), rect)
            elif (r, c) in TERMINALS:
                color = (0, 255, 0) if TERMINALS[(r, c)] > 0 else (255, 0, 0)
                pygame.draw.rect(screen, color, rect)

            # Draw the utility value
            text = font.render(f"{U[r][c]:.2f}", True, (0, 0, 0))
            screen.blit(text, (c * GRID_SIZE + 5, r * GRID_SIZE + 5))

            # Draw the policy arrow
            if policy[r][c] != -1:
                center = (c * GRID_SIZE + GRID_SIZE // 2, r * GRID_SIZE + GRID_SIZE // 2)
                dr, dc = ACTIONS[policy[r][c]]
                end = (center[0] + dc * GRID_SIZE // 3, center[1] + dr * GRID_SIZE // 3)

                # Draw the line
                pygame.draw.line(screen, (0, 0, 255), center, end, 2)

                # Calculate arrowhead points
                arrow_size = 10
                arrow_angle = 30  # degrees
                angle_rad = math.atan2(dr, dc)  # Angle of the arrow direction
                left_wing = (
                    end[0] - arrow_size * math.cos(angle_rad - math.radians(arrow_angle)),
                    end[1] - arrow_size * math.sin(angle_rad - math.radians(arrow_angle))
                )
                right_wing = (
                    end[0] - arrow_size * math.cos(angle_rad + math.radians(arrow_angle)),
                    end[1] - arrow_size * math.sin(angle_rad + math.radians(arrow_angle))
                )

                # Draw the arrowhead
                pygame.draw.polygon(screen, (0, 0, 255), [end, left_wing, right_wing])