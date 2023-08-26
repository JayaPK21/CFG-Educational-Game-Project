import mysql.connector 


class Player:
        def __init__(self, player_id=-1, player_name=" "):
            self.player_id = player_id
            self.player_name = player_name
            self.connection = mysql.connector.connect('snake_db')
            self.cursor = self.connection.cursor()


        def existing_player(self, Player):
            self.cursor.execute(""" SELECT * FROM player
            WHERE player_name ={} is {}""").format(self.player_name  ) # the player name input need here to compare 
     