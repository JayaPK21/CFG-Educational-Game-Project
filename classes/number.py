import pygame
import random
from utils.constants import BLOCK_SIZE, SW, SH

class Number:
    def __init__(self, number_value):
        self.value = number_value
        self.color = self.generate_bright_color()
        self.x = int(random.randint(0, SW / BLOCK_SIZE - 1)) * BLOCK_SIZE
        self.y = int(random.randint(1, SH / BLOCK_SIZE - 1)) * BLOCK_SIZE
        self.rect = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)  # Number rectangle

    def generate_bright_color(self):
        while True:
            color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
            if sum(color) / 3 > 150:
                return color

    def update(self, screen, FONT):
        text_color = (255, 255, 255)  # Default to white
        if sum(self.color) / 3 < 128:
            text_color = (0, 0, 0)  # Use black text on dark background

        number_text = FONT.render(str(self.value), True, text_color)
        text_rect = number_text.get_rect(center=self.rect.center)
        screen.blit(number_text, text_rect.topleft)