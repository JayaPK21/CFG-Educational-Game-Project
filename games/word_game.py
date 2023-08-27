import pygame
import sys

from utils.constants import BLOCK_SIZE, SW, SH
from utils.function_utility import draw_grid, is_position_occupied, snake_movements
from classes.snake import Snake
from classes.value import Letter
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
    paused = False
    is_game_over = False
    
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
                    #If the game over message is being shown and user_name_input is False
                    if (not user_name_input) and is_game_over:
                        #if event.key == pygame.K_RETURN:
                            #Implement feature for writing the result to database.
                        if event.key == pygame.K_BACKSPACE:
                            user_name = user_name[:-1]#Remove the last character from the name
                        else:
                            user_name += event.unicode #Add the pressed key's character to the name
                    
        if not paused:
            snake.update()

            if snake.dead:
                snake.reset_snake()

        screen.fill("black")
        draw_grid(screen, snake)
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
                if snake.lives > 0:
                    snake.lives -= 1
                    print(f'lives: {snake.lives}')
            
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
        
        # Display the game over window
        if snake.lives <= 0:
            # Stops the snake from moving in any direction.
            snake.xdir = 0
            snake.ydir = 0

            # Set game over to True
            is_game_over = True

            screen.fill("black")
            game_over_text = FONT.render("Game Over", True, "red")
            game_over_rect = game_over_text.get_rect(center=(SW / 2, SH / 2 - 20))
            score_text = FONT.render(f"Score: {score.value}", True, "white")
            score_rect = score_text.get_rect(center=(SW / 2, SH / 2 + 20))
            
            screen.blit(game_over_text, game_over_rect.topleft)
            screen.blit(score_text, score_rect.topleft)

            # #If the user has not entered their name yet, display the name input prompt
            # if not user_name_input:
            #     user_name_text = FONT.render("Enter your name: " + user_name, True, "white")
            #     user_name_rect = user_name_text.get_rect(center=(SW / 2, SH / 3 + 60))
            #     screen.blit(user_name_text, user_name_rect.topleft)

        if paused and (not is_game_over): 
            pause_text = FONT.render("Paused", True, "white")
            text_rect = pause_text.get_rect(center=(SW/2, SH/2))
            screen.blit(pause_text, text_rect.topleft)

        pygame.display.update()
        clock.tick(4)
        
    pygame.quit()
    sys.exit()

