import mysql.connector 


class Player:
        def __init__(self, player_id=-1, player_name=" "):
            self.player_id = player_id
            self.player_name = player_name
            self.connection = mysql.connector.connect('snake_db')
            self.cursor = self.connection.cursor()


        def update_score_to_database(self, player_id ):
             self.cursor.execute(
              
              )