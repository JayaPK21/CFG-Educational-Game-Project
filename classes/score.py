from constants import SW, SH

class Score:
    def __init__(self):
        self.value = 0
    
    def increase(self):
        self.value += 1

    def display(self, screen, FONT):
        score_text = FONT.render(f"Score: {self.value}", True, "grey")
        score_rect = score_text.get_rect(center=(SW / 1.25, SH / 20))
        screen.blit(score_text, score_rect)