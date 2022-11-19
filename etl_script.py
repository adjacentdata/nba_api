import psycopg2
import os 

connection_link = psycopg2.connect(os.getenv("DB_LINK"))
cursor = connection_link.cursor()

def load_data_from_csv():
    players = open('project_files/nba_data/players.csv')
    cursor.copy_from(players, 'players', sep=',' )
    players.close()
    cursor.close()
    
 