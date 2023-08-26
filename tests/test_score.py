from classes.score import Score
from utils.constants import SH
from utils.constants import SW
import pygame
import unittest
from unittest.mock import Mock
from unittest import TestCase, main


#python -m unittest discover tests


class TestScore(unittest.TestCase):
    def setUp(self):
        self.score = Score()  #Create an instance of Score for testing
    
    def test_initial_value(self):
        #Verify that the initial score value is 0
        self.assertEqual(self.score.value, 0, "Initial score value should be 0")
    
    def test_increase(self):
        initial_value = self.score.value  #Get the initial value of the score
        self.score.increase()  #Call the increase method to increase the score by 1
        #Verify that the score value has increased by 1
        self.assertEqual(self.score.value, initial_value + 1, "Score value should increase by 1")
    
    def test_display(self):
        screen = Mock()  #Mock the screen object for testing
        FONT = Mock()  #Create a mock font for testing
        self.score.value = 5  #Set an example score value
        self.score.display(screen, FONT)  #Call the display method to render the score
        #Verify that the FONT.render method was called with the correct arguments
        FONT.render.assert_called_once_with(f"Score: {self.score.value}", True, "grey")
        
        #Verify that the get_rect method was called on the score_text object
        score_text = FONT.render.return_value
        score_text.get_rect.assert_called_once()
        
        #Verify that the screen.blit method was called with the expected arguments
        expected_score_rect = score_text.get_rect.return_value
        expected_score_rect.center = (SW / 1.25, SH / 25)
        screen.blit.assert_called_once_with(score_text, expected_score_rect)