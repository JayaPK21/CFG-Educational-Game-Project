import pygame
import sys
import random

from constants import BLOCK_SIZE, SW, SH

from classes.snake import Snake
from classes.number import Number
from classes.equation import Equation
from classes.score import Score
from classes.button import Button

pygame.init()

FONT = pygame.font.Font(None, BLOCK_SIZE)  # Font for displaying numbers

screen = pygame.display.set_mode((800, 800))  # Create the game window
pygame.display.set_caption("Snake!")  # Set window title
clock = pygame.time.Clock()  # Create a clock object to control frame rate

start_button = Button(SW / 4, SH / 4, SW / 2, SH / 8, "Start", lambda: start_game())
quit_button = Button(SW / 4, SH / 4 + SH / 4, SW / 2, SH / 8, "Quit", sys.exit)
buttons = [start_button, quit_button]
game_started = False


def start_game():
    global game_started
    game_started = True


def draw_buttons():
    for button in buttons:
        button.draw(screen)


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
    # print(f'possible values: {possible_values}')
    # print(f'equation Answer {equation_answer}')
    possible_values.remove(int(equation_answer))     # Removes the answer from the possible values

    # Generates 7 random numbers from the possible values.
    for i in range(7):
        random_number = random.choice(possible_values)
        possible_values.remove(random_number)
        # new_num = Number(random_number)
        # while is_position_occupied(new_num, numbers):
        #     new_num = Number(random_number)
        numbers.append(get_new_number(random_number, numbers))
    
    return numbers, possible_values


def main():
    snake = Snake()
    equation = Equation()
    score = Score()
    #numbers = [Number() for _ in range(8)]  # Generate 8 random numbers
   
    numbers, possible_values = set_numbers(equation)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if not game_started:
                    for button in buttons:
                        if button.is_clicked(event.pos):
                            button.callback()

            if game_started and event.type == pygame.KEYDOWN:
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

        if game_started:
            snake.update()
            if snake.dead:
                snake.reset_snake()
                score = Score()
            screen.fill("black")
            drawGrid()
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

        else:
            screen.fill("black")
            draw_buttons()

        pygame.display.flip()


def drawGrid():
    for x in range(0, SW, BLOCK_SIZE):
        for y in range(0, SH, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, "#3c3c3b", rect, 1)


if __name__ == "__main__":
    drawGrid()
    main()  # Start the main game loop
