import pygame
import sys
import random

from utils.constants import BLOCK_SIZE, SW, SH
from classes.snake import Snake
from classes.value import Letter
from classes.score import Score

def drawGrid(screen):
    for x in range(0, SW, BLOCK_SIZE):
        for y in range(0, SH, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, "#3c3c3b", rect, 1)


# Gets a new letter in an unoccupied position
def get_new_letter(char, letters):
    new_char = Letter(char)
    while is_position_occupied(new_char, letters):
        new_char = Letter(char)

    return new_char


# Function to check if a letter is already occupied in the position
def is_position_occupied(new_char, letters):
    for char_class in letters:
        if new_char.rect.x == char_class.rect.x and new_char.rect.y == char_class.rect.y:
            return True
    return False


def run_word_game(screen, clock, FONT):
    print("This is word game!")