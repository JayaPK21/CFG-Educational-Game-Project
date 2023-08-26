from games.number_game import run_number_game
from utils.constants import SH
from utils.constants import SW
import unittest
import pygame



#python -m unittest discover tests


class TestGameOver(unittest.TestCase):
    def test_game_over(self):
        snake = run_number_game.snake
        snake.lives.value = 0  #Verify that the snake lives are at 0 when game ends
    
        #Check that when the number game is running, game over is not showing
        run_number_game.run = True 
        run_number_game.show_game_over = False

        run_number_game.main()

        self.assertTrue(run_number_game.show_game_over)


class TestUserInput(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 700)) #mock screen 
        self.FONT = pygame.font.Font(None, 36)
        self.user_name = "CFG" #mock user input 
        self.user_name_input = True #user name has been added
    
    def test_user_input_shows(self):
        screen = self.screen
        FONT = self.FONT
        user_name = self.user_name
        user_name_input = self.user_name_input

        #Simulate the code that renders the user name input section
        if user_name_input:
            user_name_text = FONT.render("Enter your name: " + user_name, True, "white")
            user_name_rect = user_name_text.get_rect(center=(SW / 2, SH / 3 + 60))
            screen.blit(user_name_text, user_name_rect.topleft)
    
        pygame.display.update()

        #Check if the user's name is correctly displayed when user_name_input is True
        if user_name_input:
            expected_user_name_text = "Enter your name: " + user_name
            self.assertEqual(user_name_text.get_text(), expected_user_name_text)