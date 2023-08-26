from classes.words import Word
from utils.constants import SH
from utils.constants import SW
import pygame
import random
import unittest
from unittest.mock import Mock, patch
from unittest import TestCase, main
     

#python -m unittest discover tests

class TestWord(unittest.TestCase):
    def setUp(self):
        self.word = Word()

    @patch('random.randint')  #Mocking the random.randint function
    def test_init(self, mock_randint):
        mock_randint.return_value = 2  #Set a fixed value for random.randint
        self.word.__init__()
        self.assertEqual(self.word.list_index, 2)  #Ensure list_index is set to the mocked value
        self.assertEqual(self.word.selected_word, "resort")  #Check if selected_word is set correctly
        self.assertEqual(self.word.snake_word, "")  #Snake word should be initially empty

    def test_display_initial(self):
        screen = Mock()
        FONT = Mock()
        self.word.display(screen, FONT)
        word_text = FONT.render('_', True, "white")  #Expected rendering for initial snake_word
        word_rect = word_text.get_rect(center=(SW / 2, SH / 25))
        screen.blit.assert_called_with(word_text, word_rect.topleft)

    def test_display_updated(self):
        self.word.snake_word = "r___rt"  #Set snake_word to a partially filled word
        screen = Mock()
        FONT = Mock()
        self.word.display(screen, FONT)
        word_text = FONT.render("r___rt", True, "white")
        word_rect = word_text.get_rect(center=(SW / 2, SH / 25))
        screen.blit.assert_called_with(word_text, word_rect.topleft)

    def test_update(self):
        self.word.snake_word = "r___rt"
        self.word.update("e")
        self.assertEqual(self.word.snake_word, "re__rt")  #Check if snake_word is updated correctly

    @patch('random.randint')  #Mocking the random.randint function
    def test_reset_word(self, mock_randint):
        mock_randint.return_value = 1  #Fixed value for random.randint to make sure that the same word is selected after resetting
        self.word.reset_word("resort")
        self.assertNotIn("resort", self.word.words_list)  #Check if previous word is removed
        self.assertEqual(self.word.list_index, 1)  #Ensure list_index is updated after reset
        self.assertEqual(self.word.selected_word, "desk")  #Check if selected_word is updated after reset
        self.assertEqual(self.word.snake_word, "")  #Snake word should be reset
