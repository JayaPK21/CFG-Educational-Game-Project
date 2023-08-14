import pygame
import random
from utils.constants import BLOCK_SIZE, SW, SH

class Value:
    def __init__(self, value):
        self.value = value
        self.color = self.generate_bright_color()
        self.x = int(random.randint(0, SW / BLOCK_SIZE - 1)) * BLOCK_SIZE
        self.y = int(random.randint(1, SH / BLOCK_SIZE - 1)) * BLOCK_SIZE
        self.rect = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)  # Value rectangle

    def generate_bright_color(self):
        while True:
            color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
            #print("Generated color:", color)
            if sum(color) / 3 > 150:
                return color

class Number(Value):
    def __init__(self, number_value):
        super().__init__(str(number_value))
        
    def update(self, screen, FONT):
        text_color = self.color
        if sum(text_color) / 3 < 128:
            text_color=(0,0,0)

        value_text = FONT.render(self.value, True, text_color)
        text_rect = value_text.get_rect(center = self.rect.center)
        screen.blit(value_text, text_rect.topleft)


class Letter(Value):
    def __init__(self, letter_value):
        super().__init__(letter_value)