import psycopg2
import os 
from queries import Players

pathways = {'project_files/nba_data/games_details.csv', 'project_files/nba_data/games.csv', 'project_files/nba_data/players.csv', 'project_files/nba_data/ranking.csv', 'project_files/nba_data/teams.csv'}

db_user=os.getenv('USER')
db_password=os.getenv('DB_PASSWORD')
connection_link = psycopg2.connect(database='nba_api', user=db_user, password=db_password, host='127.0.0.1', port='5432')
cursor = connection_link.cursor()

def create_table():
    cursor.execute(Players.CREATE_NBA_PLAYERS_TABLE)
    connection_link.commit()

def load_data_into_db(pathways):
    for i in range(len(pathways)):
        with open(pathways[i], 'r') as data: 
                next(data)
                cursor.copy_from(data, 'players', sep=',' )
    connection_link.commit()

connection_link.commit()
cursor.close()





    
 