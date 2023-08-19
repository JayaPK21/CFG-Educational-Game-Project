import random
from utils.constants import SW, SH

class Word:
    def __init__(self):
        self.words_list = ["choice", "desk", "resort", "point", "vague", "depart"]
        self.list_index = random.randint(0, len(self.words_list)-1)
        self.selected_word = self.words_list[self.list_index]
        self.snake_word = ''

    def display(self, screen, FONT):
        if self.snake_word == '':
            self.snake_word = '_' * len(self.selected_word)
        word_text = FONT.render(self.snake_word, True, "white")
        word_rect = word_text.get_rect(center=(SW / 2, SH / 25))
        screen.blit(word_text, word_rect.topleft)
    
    def update(self, letter):
        self.snake_word = self.snake_word.replace('_', letter, 1)
    
    def reset_word(self, previous_word):
        self.words_list.remove(previous_word)   # Removing previous word that has been played
        self.list_index = random.randint(0, len(self.words_list)-1)
        self.selected_word = self.words_list[self.list_index]
        self.snake_word = ''