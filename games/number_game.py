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
    numbers = [] #List to store the generated number values

    equation_answer = equation.result
    numbers.append(Number(equation_answer)) #Add the correct equation answer as a Number object

    possible_values = list(range(0, 21))#List of possible values (0 to 20)
    possible_values.remove(int(equation_answer))#Remove the correct answer from possible values

    for i in range(7):
        random_number = random.choice(possible_values)#Choose a random value from possible_values
        possible_values.remove(random_number)#Remove the chosen value from possible_values
        numbers.append(get_new_number(random_number, numbers))#Create a new Number object and add it to the list

    return numbers, possible_values #Return the list of generated numbers and the updated possible_values

def run_number_game(screen, clock, FONT):
    score = Score()
    snake = Snake()
    equation = Equation()
    numbers, possible_values = set_numbers(equation)

    run = True
    paused = False

    show_game_over_message = False

    user_name = ""
    user_name_input = False

    #Main game loop
    while run: 
        for event in pygame.event.get():# Handle events like quitting the game or key press
            if event.type == pygame.QUIT:
                run = False #Exit the game loop and end the game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: #Toggle the paused state when the spacebar is pressed
                    paused = not paused
                else:
                    snake_movements(event, snake) #Handle snake movements based on key presses
                    #If the game over message is being shown and user_name_input is False
                    if show_game_over_message and not user_name_input:
                        if event.key == pygame.K_RETURN:
                            user_name_input = True #Start capturing the user's name
                        elif event.key == pygame.K_BACKSPACE:
                            user_name = user_name[:-1]#Remove the last character from the name
                        else:
                            user_name += event.unicode #Add the pressed key's character to the name
        #Update the game elements and logic if the game is not paused
        if not paused:
            snake.update()
            lives_text = FONT.render(f"Lives: {snake.lives}", True, "red")
            lives_rect = lives_text.get_rect(topleft=(10, 10))
            screen.blit(lives_text, lives_rect)
            screen.fill("black")
            draw_grid(screen, snake)                                      
            equation.display(screen, FONT)
            score.display(screen, FONT)
          
            

        #Check if the snake's lives have run out, and if so, show the game over message
        if snake.lives <= 0:
            show_game_over_message = True

            # Stops the snake from moving in any direction.
            snake.xdir = 0
            snake.ydir = 0

        #Check if the snake has died, and if so, reset its state
        if snake.dead:
            snake.reset_snake()

        screen.fill("black")
        draw_grid(screen, snake)
    
        equation.display(screen, FONT)
        score.display(screen, FONT)
    

        #Update the positions and appearance of each number on the screen
        for num in numbers:
            num.update(screen, FONT)
            
        #Draw a green rectangle to represent the head of the snake
        pygame.draw.rect(screen, "green", snake.head)
        
        #Iterate over each segment of the snake's body and draw a green rectangle for each segment
        for square in snake.body:
            pygame.draw.rect(screen, "green", square)

        #Check collision between the snake's head and the numbers on the screen
        for num in numbers:
            if snake.head.x == num.x and snake.head.y == num.y:
                #If the value of the number matches the current equation result, add a new segment to the snake
                #at the position of the collided number, update the equation, increase the score, and refresh
                #the numbers on the screen
                if str(num.value) == str(equation.result):
                    snake.body.append(pygame.Rect(square.x, square.y, BLOCK_SIZE, BLOCK_SIZE))
                    equation = Equation() #Get a new equation
                    score.increase() #Increase the player's score
                    numbers, possible_values = set_numbers(equation) #Refresh the numbers on the screen
                else:
                    # If the collided number's value doesn't match the equation result, remove the number from
                    # the list, add its value back to the possible values, select a new random number from
                    # the possible values, update the list of numbers, and decrease the snake's lives
                    numbers.remove(num)
                    possible_values.append(num.value)
                    random_number = random.choice(possible_values)
                    possible_values.remove(random_number)
                    numbers.append(get_new_number(random_number, numbers))
                    if snake.lives > 0:
                        snake.lives -= 1 #Decrease the snake's lives (if lives are remaining)
                        print(f'lives: {snake.lives}')
                        

        if show_game_over_message:
            screen.fill("black")
            game_over_text = FONT.render("Game Over", True, "red")
            game_over_rect = game_over_text.get_rect(center=(SW / 2, SH / 2 - 20))
            score_text = FONT.render(f"Score: {score.value}", True, "white")
            score_rect = score_text.get_rect(center=(SW / 2, SH / 2 + 20))
            #Display the game over text and the player's score on the screen
            screen.blit(game_over_text, game_over_rect.topleft)
            screen.blit(score_text, score_rect.topleft)
            #If the user has not entered their name yet, display the name input prompt
            if not user_name_input:
                user_name_text = FONT.render("Enter your name: " + user_name, True, "white")
                user_name_rect = user_name_text.get_rect(center=(SW / 2, SH / 3 + 60))
                screen.blit(user_name_text, user_name_rect.topleft)
        #If the user is entering their name, display the input prompt and capture the input
        if user_name_input:
            user_name_text = FONT.render("Enter your name: " + user_name, True, "white")
            user_name_rect = user_name_text.get_rect(center=(SW / 2, SH / 3 + 60))
            screen.blit(user_name_text, user_name_rect.topleft)

        if paused and (not show_game_over_message):
            pause_text = FONT.render("Paused", True, "white")
            text_rect = pause_text.get_rect(center=(SW / 2, SH / 2))
            screen.blit(pause_text, text_rect.topleft)

        pygame.display.update() #Update the display to reflect changes
        clock.tick(4) #Limit the frame rate to control game speed

        pygame.display.flip() #Update the full display surface

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    pygame.init()
   
