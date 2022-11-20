import psycopg2
import os 
from queries import Players

db_user=os.getenv('USER')
db_password=os.getenv('DB_PASSWORD')
connection_link = psycopg2.connect(database='nba_api', user=db_user, password=db_password, host='127.0.0.1', port='5432')
cursor = connection_link.cursor()

def create_table():
    cursor.execute(Players.CREATE_NBA_PLAYERS_TABLE)
    connection_link.commit()

with open('project_files/nba_data/players.csv', 'r') as data: 
        next(data)
        cursor.copy_from(data, 'players', sep=',' )

connection_link.commit()
cursor.close()





    
 