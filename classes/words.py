import random
from utils.constants import SW, SH

class Word:
    def __init__(self):
        self.words_list = ["choice", "state", "resort", "point", "vague", "depart"]
        self.list_index = random.randint(0, len(self.words_list))
        self.selected_word = self.words_list[self.list_index]
        # self.num1 = random.randint(1, 9)
        # self.num2 = random.randint(1, 9)
        # self.operator = random.choice(['+', '-'])
        # if self.operator == '-':
        #     self.num1, self.num2 = max(self.num1, self.num2), min(self.num1, self.num2)  # Ensure positive result
        # self.result = str(eval(str(self.num1) + self.operator + str(self.num2)))
        # self.text = f"{self.num1} {self.operator} {self.num2}"

    def display(self, screen, FONT, snake_word=''):
        if snake_word == '':
            snake_word = '_' * len(self.selected_word)
        word_text = FONT.render(snake_word, True, "white")
        word_rect = word_text.get_rect(center=(SW / 2, SH / 25))
        screen.blit(word_text, word_rect.topleft)