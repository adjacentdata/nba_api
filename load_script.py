import psycopg2
import os 
from queries import Players

pathways = {
    'game_details': 'project_files/nba_data/games_details.csv', 
    'games':'project_files/nba_data/games.csv', 
    'players': 'project_files/nba_data/players.csv',
    'rankings': 'project_files/nba_data/ranking.csv', 
    'teams':'project_files/nba_data/teams.csv'}


db_user=os.getenv('USER')
db_password=os.getenv('DB_PASSWORD')
connection_link = psycopg2.connect(database='nba_api', user=db_user, password=db_password, host='127.0.0.1', port='5432')
cursor = connection_link.cursor()

def create_tables():
    cursor.execute(Players.CREATE_NBA_GAMES_TABLE)
    connection_link.commit()

def load_data_into_db(pathways):
    for i,key in enumerate(pathways):
        with open(pathways[key], 'r') as data: 
                next(data)
                cursor.copy_from(data, key, sep=',' )
        print(str(i) + ' was succesful.')
    connection_link.commit()

# Test
def to_json(query_data):
    return {
        'players': query_data , 
    }

def test():
    cursor.execute(Players.GET_ALL_PLAYERS)
    dbop = cursor.fetchall()
    return dbop

create_tables()
with open(pathways['games'], 'r') as data: 
    next(data)
    cursor.copy_from(data, 'games', sep=',' )


connection_link.commit()
cursor.close()





    
 