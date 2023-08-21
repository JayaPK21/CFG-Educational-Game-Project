import pygame
import sys
import random

from utils.constants import BLOCK_SIZE, SW, SH
from utils.function_utility import draw_grid, is_position_occupied, snake_movements
from classes.snake import Snake
from classes.value import Number
from classes.equation import Equation
from classes.score import Score


# Gets a new number in an unoccupied position
def get_new_number(num, numbers):
    new_num = Number(num)
    while is_position_occupied(new_num, numbers):
        new_num = Number(num)

    return new_num


def set_numbers(equation):
    numbers = []

    equation_answer = equation.result
    numbers.append(Number(equation_answer))

    possible_values = list(range(0, 21))
    possible_values.remove(int(equation_answer))

    for i in range(7):
        random_number = random.choice(possible_values)
        possible_values.remove(random_number)
        numbers.append(get_new_number(random_number, numbers))

    return numbers, possible_values

def run_number_game(screen, clock, FONT, score):
    pygame.init()

    snake = Snake()
    equation = Equation()
    numbers, possible_values = set_numbers(equation)

    run = True
    paused = False

    lives = 3

    show_game_over_message = False
    game_over_message_timer = 2000

    user_name = ""
    user_name_input = False

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused
                else:
                    snake_movements(event, snake)

                    if show_game_over_message and not user_name_input:
                        if event.key == pygame.K_RETURN:
                            user_name_input = True
                        elif event.key == pygame.K_BACKSPACE:
                            user_name = user_name[:-1]
                        else:
                            user_name += event.unicode

        if not paused:
            snake.update()
            screen.fill("black")
            draw_grid(screen)
            equation.display(screen, FONT)
            score.display(screen, FONT)

        if snake.lives <= 0:
            show_game_over_message = True

        if snake.dead:
            snake.reset_snake()

        screen.fill("black")
        draw_grid(screen)
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
                    equation = Equation()
                    score.increase()
                    numbers, possible_values = set_numbers(equation)
                else:
                    numbers.remove(num)
                    possible_values.append(num.value)
                    random_number = random.choice(possible_values)
                    possible_values.remove(random_number)
                    numbers.append(get_new_number(random_number, numbers))
                    if snake.lives > 0:
                        snake.lives -= 1

        if show_game_over_message:
            screen.fill("black")
            game_over_text = FONT.render("Game Over", True, "red")
            game_over_rect = game_over_text.get_rect(center=(SW / 2, SH / 2 - 20))
            score_text = FONT.render(f"Score: {score.value}", True, "white")
            score_rect = score_text.get_rect(center=(SW / 2, SH / 2 + 20))
            screen.blit(game_over_text, game_over_rect.topleft)
            screen.blit(score_text, score_rect.topleft)

            if not user_name_input:
                user_name_text = FONT.render("Enter your name: " + user_name, True, "white")
                user_name_rect = user_name_text.get_rect(center=(SW / 2, SH / 3 + 60))
                screen.blit(user_name_text, user_name_rect.topleft)

        if user_name_input:
            user_name_text = FONT.render("Enter your name: " + user_name, True, "white")
            user_name_rect = user_name_text.get_rect(center=(SW / 2, SH / 3 + 60))
            screen.blit(user_name_text, user_name_rect.topleft)

        if paused:
            pause_text = FONT.render("Paused", True, "white")
            text_rect = pause_text.get_rect(center=(SW / 2, SH / 2))
            screen.blit(pause_text, text_rect.topleft)

        pygame.display.update()
        clock.tick(6)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    pygame.init()
   
