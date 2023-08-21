import mysql.connector 
from config import USER, PASSWORD, HOST

def connect_to_db(db_name):
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return cnx 

<<<<<<< Updated upstream

def get_players_results():
    db_connection = _connect_to_db()
    cursor = db_connection.cursor()
    query = """select p.Player_name, s.wins, s.losses,s.draws 
    from player p 
    inner join score s
    on s.score_id 
    order by player_id"""
    cursor.execute(query)
    result = cursor.fetchall()  # this is a list with db records where each record is a tuple
    for i in result:
        print(i)
        cursor.close()




# This functions excuts all the query above 
def main():
    get_players_results()  # display players results 


=======
>>>>>>> Stashed changes
if __name__ == '__main__':
    main()