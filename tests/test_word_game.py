import unittest
   
from classes.value import Letter
from classes.words import Word
from games.word_game import get_new_letter, set_letters  # Importing functions to be tested

class TestCaseGetNewLetter(unittest.TestCase):

    # Tests if the value of position is changed when the current position is already occupied.
    def test_get_new_letter_with_new_position(self):
        new_char = Letter('D')
        new_char.rect.x = 1
        new_char.rect.y = 2

        letters = [Letter('G'), Letter('L'), Letter('A')]
        letters[0].rect.x = 3
        letters[0].rect.y = 4

        letters[1].rect.x = 1
        letters[1].rect.y = 2

        letters[2].rect.x = 5
        letters[2].rect.y = 6

        result_character = get_new_letter(new_char, letters)

        # Since the position for new_character is already occupied, the value of position is changed.
        self.assertNotEqual((result_character.rect.x, result_character.rect.y), (1,2))


class TestCaseSetLetters(unittest.TestCase):

    # Tests if the given word is split into individual letters and instances of 
    # 'Letter' class for the corresponding letters is stored in a list.
    def test_set_letters_SAMPLE(self):
        word = Word()
        word.selected_word = "SAMPLE"
        result = set_letters(word)

        # Checks if each letter in the word is an instance of the 'Letter' class
        self.assertTrue(
            isinstance(result[0], Letter) and
            isinstance(result[1], Letter) and
            isinstance(result[2], Letter) and
            isinstance(result[3], Letter) and
            isinstance(result[4], Letter) and
            isinstance(result[5], Letter)
        )
        