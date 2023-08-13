import pygame
import sys
import random

from utils.constants import BLOCK_SIZE
from utils.function_utility import draw_grid, is_position_occupied, snake_movements
from classes.snake import Snake
from classes.value import Letter
from classes.equation import Equation
from classes.score import Score


# Gets a new letter in an unoccupied position
def get_new_letter(character, letters):
    new_char = Letter(character)
    while is_position_occupied(new_char, letters):
        new_char = Letter(character)

    return new_char


def set_letters():
    print("Inside Set Letters")



def run_word_game(screen, clock, FONT):

    snake = Snake()
    equation = Equation()
    score = Score()
    # numbers, possible_values = set_numbers(equation)

    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                snake_movements(event, snake)

        snake.update()
        if snake.dead:
            snake.reset_snake()
            score = Score()
        screen.fill("black")
        draw_grid(screen)
        # equation.display(screen, FONT)
        # score.display(screen, FONT)

        # for num in numbers:
        #     num.update(screen, FONT)

        pygame.draw.rect(screen, "green", snake.head)
        for square in snake.body:
            pygame.draw.rect(screen, "green", square)

        pygame.display.update()
        clock.tick(4)

        pygame.display.flip()
    
    pygame.quit()
    sys.exit()