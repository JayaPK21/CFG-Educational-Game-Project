import pygame
from utils.constants import BLOCK_SIZE, SW, SH

def draw_grid(screen):
    # The first row in the grid contains the score and equation
    top_rect = pygame.Rect(0, 0, SW, BLOCK_SIZE)
    pygame.draw.rect(screen, "#328ca8", top_rect)

    for x in range(0, SW, BLOCK_SIZE):
        for y in range(BLOCK_SIZE, SH, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, "#3c3c3b", rect, 1)


# Function to check if a value is already occupying the position
def is_position_occupied(new_value, values):
    for value_class in values:
        if new_value.rect.x == value_class.rect.x and new_value.rect.y == value_class.rect.y:
            # print(f'Inside function')
            return True
    return False


def snake_movements(event, snake):
    if event.key == pygame.K_DOWN:
        snake.ydir = 1
        snake.xdir = 0
    elif event.key == pygame.K_UP:
        snake.ydir = -1
        snake.xdir = 0
    elif event.key == pygame.K_RIGHT:
        snake.ydir = 0
        snake.xdir = 1
    elif event.key == pygame.K_LEFT:
        snake.ydir = 0
        snake.xdir = -1
        