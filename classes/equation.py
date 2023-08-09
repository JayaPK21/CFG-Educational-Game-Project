import random
from utils.constants import SW, SH

class Equation:
    def __init__(self):
        self.num1 = random.randint(1, 9)
        self.num2 = random.randint(1, 9)
        self.operator = random.choice(['+', '-'])
        if self.operator == '-':
            self.num1, self.num2 = max(self.num1, self.num2), min(self.num1, self.num2)  # Ensure positive result
        self.result = str(eval(str(self.num1) + self.operator + str(self.num2)))
        self.text = f"{self.num1} {self.operator} {self.num2}"

    def display(self, screen, FONT):
        equation_text = FONT.render(self.text, True, "white")
        equation_rect = equation_text.get_rect(center=(SW / 2, SH / 20))
        screen.blit(equation_text, equation_rect.topleft)
