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


if __name__ == '__main__':
    main()