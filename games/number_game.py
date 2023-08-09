import pygame
import sys
import random

from utils.constants import BLOCK_SIZE, SW, SH
from classes.snake import Snake
from classes.number import Number
from classes.equation import Equation
from classes.score import Score

def drawGrid(screen):
    for x in range(0, SW, BLOCK_SIZE):
        for y in range(0, SH, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, "#3c3c3b", rect, 1)


# Gets a new number in an unoccupied position
def get_new_number(num, numbers):
    new_num = Number(num)
    while is_position_occupied(new_num, numbers):
        new_num = Number(num)

    return new_num


# Function to check if a number is already occupied in the position
def is_position_occupied(new_number, numbers):
    for num_class in numbers:
        if new_number.rect.x == num_class.rect.x and new_number.rect.y == num_class.rect.y:
            # print(f'Inside function')
            return True
    return False


def set_numbers(equation):
    numbers = []        

    equation_answer = equation.result           # Gets the answer for the equation
    numbers.append(Number(equation_answer))     # Adds the answer to the list of numbers to be displayed

    possible_values = list(range(0, 21))
    possible_values.remove(int(equation_answer))     # Removes the answer from the possible values

    # Generates 7 random numbers from the possible values.
    for i in range(7):
        random_number = random.choice(possible_values)
        possible_values.remove(random_number)
        numbers.append(get_new_number(random_number, numbers))
    
    return numbers, possible_values


def run_number_game(screen, clock, FONT):

    snake = Snake()
    equation = Equation()
    score = Score()
    numbers, possible_values = set_numbers(equation)

    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
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

        snake.update()
        if snake.dead:
            snake.reset_snake()
            score = Score()
        screen.fill("black")
        drawGrid(screen)
        equation.display(screen, FONT)
        score.display(screen, FONT)

        for num in numbers:
            num.update(screen, FONT)

        pygame.draw.rect(screen, "green", snake.head)
        for square in snake.body:
            pygame.draw.rect(screen, "green", square)

        for num in numbers:
            if snake.head.x == num.x and snake.head.y == num.y:
                if str(num.value) == str(equation.result):
                    snake.body.append(pygame.Rect(square.x, square.y, BLOCK_SIZE, BLOCK_SIZE))
                    equation = Equation()  # Generate a new equation
                    score.increase()
                    numbers, possible_values = set_numbers(equation)
                
                else:
                    numbers.remove(num)
                    possible_values.append(num.value)
                    random_number = random.choice(possible_values)
                    possible_values.remove(random_number)
                    #numbers.append(Number(random_number))  # Generate a new number
                    numbers.append(get_new_number(random_number, numbers))  # Generate a new number

        pygame.display.update()
        clock.tick(4)

        pygame.display.flip()
    
    pygame.quit()
    sys.exit()