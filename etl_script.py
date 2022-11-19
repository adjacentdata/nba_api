import psycopg2
import os 

connection_link = psycopg2.connect(os.getenv("DB_LINK"))
cursor = connection_link.cursor()

def load_data_from_csv():
    """
    The function reads data from a csv file and auto loads it into the PostgreSQL server. 
    """
    with open('project_files/nba_data/players.csv', 'r') as data: 
        next(data)
        cursor.copy_from(data, 'players', sep=',' )

cursor.commit()
cursor.close()


    
 