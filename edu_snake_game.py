import pygame
import sys

from utils.constants import BLOCK_SIZE, SW, SH

from classes.button import Button

from games.number_game import run_number_game
from games.word_game import run_word_game


pygame.init()

FONT = pygame.font.Font(None, BLOCK_SIZE)  # Font for displaying numbers

screen = pygame.display.set_mode((SW, SH))  # Create the game window
pygame.display.set_caption("Snake!")  # Set window title
clock = pygame.time.Clock()  # Create a clock object to control frame rate

start_button = Button(SW / 6, SH / 4, SW / 3, SH / 8, "Word Game", lambda: start_word_game())
start_number_button = Button(SW / 1.75, SH / 4, SW / 3, SH / 8, "Number Game", lambda: start_number_game())
quit_button = Button(SW / 4, SH / 4 + SH / 4, SW / 2, SH / 8, "Quit", sys.exit)
buttons = [start_button, start_number_button, quit_button]
# game_started = False


def start_word_game():
    run_word_game(screen, clock, FONT)


def start_number_game():
    run_number_game(screen, clock, FONT)


def draw_buttons():
    for button in buttons:
        button.draw(screen)
        
# def draw_pause_text():
#     pause_text= FONT.render("Pauseddddddd", True, "white")
#     text_rect = pause_text.get_rect(center=(SW/2, SH/2))
#     screen.blit(pause_text,text_rect.topleft)


def main():
    paused = False
    run = True
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            
            if not paused:
                if event.type == pygame.MOUSEBUTTONDOWN:
                # Loops through the buttons to check which button is being clicked and calls the corresponding call back function
                    for button in buttons:
                        if button.is_clicked(event.pos):
                            button.callback()
                            
                            

        screen.fill("black")
        # if paused:
        #     # draw_pause_text()
        # else:
        draw_buttons()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()  # Start the main game loop
