import pygame

class Button:
    def __init__(self, x, y, width, height, text, callback):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.callback = callback

    def draw(self, surface):
        pygame.draw.rect(surface, "gray", self.rect)  # Draw the button rectangle
        font = pygame.font.Font(None, 36)
        text = font.render(self.text, True, "black")
        text_rect = text.get_rect(center=self.rect.center)
        surface.blit(text, text_rect)  # Draw the button text

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)  # Check if the button is clicked
