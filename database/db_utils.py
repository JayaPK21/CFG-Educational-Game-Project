import mysql.connector 
from config import USER, PASSWORD, HOST
from classes.player import Player
from classes.score import Score





def connect_to_db(snake_db):
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_password',
        database=snake_db
    )
    return cnx 

# creating a the tables with the inserts into the tables
def create_player_table():
    db_connection = connect_to_db()
    cursor = db_connection.cursor()
    query = """ CREATE TABLE  IF NOT EXISTS player (
                 player_id INT NOT NULL,
                 player_name VARCHAR(45) NULL,
                 PRIMARY KEY (player_id)
                 );"""
    #input data into the player table 
    insert_data = """
                    INSERT INTO player(player_id, player_name)VALUES
                        (1, "Alice"),
                        (2, "Belen"),
                        (3, "Ciara"),
                        (4, "Delia"),
                        (5, "Everly"),
                        (6, "Fabia"),
                        (7, "Grace");"""
    cursor.execute(query, insert_data)
    row = cursor.fetchall()  # creating the player table, record is a tuple
    for i in row:
        print(i)
        cursor.close()

def create__game_table():
    db_connection = connect_to_db()
    cursor = db_connection.cursor()
    query = """ CREATE TABLE  IF NOT EXISTS game(
                game_id int NOT NULL,
                player_id int,
                primary key (Game_id),
                FOREIGN KEY (player_id) REFERENCES player(player_id));"""
    #input data into the player table 
    insert_data_two = """INSERT INTO game (game_id, player_id)VALUES
   (101,  1),(102,  2),(103,  3),(104,  4),
   (105,  5),(106,  6),(107,  7),(108,  7),
   (109,  7),(110,  7),(111,  1),(112,  2),
   (113,  3),(114,  4),(115,  5),(116,  6),
   (117,  7),(118,  7),(119,  7),(120,  7),
   (121,  1),(122,  2),(123,  3),(124,  4),
   (125,  5),(126,  6),(127,  7),(128,  7),
   (129,  7),(130,  7);"""
    cursor.execute(query, insert_data_two)
    row = cursor.fetchall()  # creating the player table, record is a tuple
    for i in row:
        print(i)
        cursor.close()

def create_score_table():
    db_connection = connect_to_db()
    cursor = db_connection.cursor()
    query = """ CREATE TABLE  IF NOT EXISTS score (
                score_id int NOT NULL,player_id int,
                sc_date date NOT NULL, score int NOT NULL, 
                primary key (Score_id),
                FOREIGN KEY (player_id) REFERENCES player(player_id);"""
    #input data into the score table 
    insert_data_three = """ INSERT INTO score (score_id, player_id, sc_date, score)VALUES
     (111, 1, '2023-05-20', 10),(112, 2,  '2023-04-25', 8),
     (113, 3, '2023-01-09', 1),(114, 4,  '2023-02-24', 5),
	 (115, 5,  '2023-12-15', 9),(116, 6,  '2023-05-04', 8),
     (117, 7,  '2023-01-23', 3),(118, 7,  '2023-02-23', 5),
 	 (119, 7,  '2023-03-20', 2), (120, 7,  '2023-05-15', 3),
	 (121, 1,   '2023-04-22', 10),(122,  2,  '2023-04-20', 4),
 	 (123,  3,  '2023-01-09 ', 7),(124,  4,  '2023-01-09', 4),
     (125,  5,  '2023-02-10 ', 1), (126,  6,  '2023-02-11', 0),
     (127,  7, '2023-02-12', 4),(128,  7,  '2023-02-13', 6),
     (129,  7,  '2023-02-14', 9),(130,  7,  '2023-12-9', 10),
	 (131,  1,  '2023-12-10', 6), (132,  2,  '2023-12-11', 7),
     (133,  3,  '2023-12-12', 7),(134,  4,  '2023-12-13', 8),
     (135,  5,  '2023-12-14', 10),(136,  6,  '2023-12-16', 4),     
     (137,  7,  '2023-05-17 ', 8);"""
    cursor.execute(query, insert_data_three)
    row = cursor.fetchall()  # creating the player table, record is a tuple
    for i in row:
        print(i)
        cursor.close()



# retrieve the users_name, date, the score from the function 
# below is the shell of the code
def retrieve_players_information():
    db_connection = connect_to_db()
    cursor = db_connection.cursor()
    # Update a record
    query = "UPDATE  SET  WHERE "
    cursor.execute(query, (''))
    # Commit changes
    cursor.commit()
    print("Record updated successfully")
    cursor.close()

def get_players_results():
    db_connection = connect_to_db()
    cursor = db_connection.cursor()
    query = """ select p.player_name, s.sc_date, s.score
                from group3a_educational_game_project.p_player p 
                inner join group3a_educational_game_project.score s
                on s.score_id
                order by p.player_name
                ;"""
    cursor.execute(query)
    result = cursor.fetchall()  # Will list db records, record is a tuple
    for i in result:
        print(i)
        cursor.close()

# This functions excuts all the query above 
def main():
    get_players_results()  # display players results
    Score.update_new_player_to_database() 

if __name__ == '__main__':
    main()