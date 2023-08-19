import pygame
import sys
import random

from utils.constants import BLOCK_SIZE
from utils.function_utility import draw_grid, is_position_occupied, snake_movements
from classes.snake import Snake
from classes.value import Letter
from classes.equation import Equation
from classes.words import Word
from classes.score import Score


# Gets a new letter in an unoccupied position
def get_new_letter(character, letters):
    new_char = Letter(character)
    while is_position_occupied(new_char, letters):
        new_char = Letter(character)

    return new_char


def set_letters(word):
    letters = []

    for character in list(word.selected_word):
        letters.append(get_new_letter(character, letters))
    
    return letters


def run_word_game(screen, clock, FONT):

    snake = Snake()
    word = Word()
    score = Score()

    letters = set_letters(word)

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
        word.display(screen, FONT)
        score.display(screen, FONT)

        for letter in letters:
            letter.update(screen, FONT)

        pygame.draw.rect(screen, "green", snake.head)
        for square in snake.body:
            pygame.draw.rect(screen, "green", square)
        
        for letter in letters:

            # For each letter that is picked by the snake, the corresponding word is displayed at the top of the game.
            if snake.head.x == letter.x and snake.head.y == letter.y:
                snake.body.append(pygame.Rect(square.x, square.y, BLOCK_SIZE, BLOCK_SIZE))
                letters.remove(letter)
                word.update(letter.value)

        if len(letters) == 0:

            if word.selected_word == word.snake_word:
                # Increase score for forming the right word
                score.increase()

            else:
                # Total lives has to decrease as the word formed is wrong
                snake.lives -= 1
            
            previous_word = word.selected_word  # Stores the previous word
            if len(word.words_list) > 1:
                # Generates a new word after removing the word that has already been played from list
                word.reset_word(previous_word)

            else:
                # The word_list has been reset after all the words have been exhausted from the list
                # The last played word is then removed from the list so that it is not immediately seleced as the next word
                word = Word()
                word.words_list.remove(previous_word)
            
            letters = set_letters(word)     # Sets the letters for the new word
            snake.reset_snake()     # Reset the snake length and position

        pygame.display.update()
        clock.tick(4)

        pygame.display.flip()
    
    pygame.quit()
    sys.exit()