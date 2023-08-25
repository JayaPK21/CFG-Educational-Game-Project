from utils.constants import SW, SH
from classes.player import Player
from datetime import date 
import mysql.connector 


class Score: 
    def __init__(self, score_id=-1):
      # self.player = player
        self.score_id = score_id
        self.player_id = Player 
        self.sc_date = date.today()
        self.value = 0
        self.connection = mysql.connector.connect('snake_db')
        self.cursor = self.connection.cursor()

    def increase(self):
        self.value += 1

    def display(self, screen, FONT):
        score_text = FONT.render(f"Score: {self.value}", True, "grey")
        score_rect = score_text.get_rect(center=(SW / 1.25, SH / 25))
        screen.blit(score_text, score_rect)

    def update_score_to_database(self, score_id ):
        self.cursor.execute(

        )

 
