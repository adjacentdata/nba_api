import psycopg2
import os 
import json
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
    cursor.execute(Players.CREATE_NBA_PLAYERS_TABLE)
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
    print(json.dumps(db)) 
    return to_json(jop)

print(test())
connection_link.commit()
cursor.close()


t=[("Royce O'Neale", 1610612762, 1626220, 2019), 
('Bojan Bogdanovic', 1610612762, 202711, 2019), 
('Rudy Gobert', 1610612762, 203497, 2019), 
('Donovan Mitchell', 1610612762, 1628378, 2019), 
('Mike Conley', 1610612762, 201144, 2019), 
('Joe Ingles', 1610612762, 204060, 2019), 
('Ed Davis', 1610612762, 202334, 2019), 
('Jeff Green', 1610612762, 201145, 2019), 
('Dante Exum', 1610612762, 203957, 2019), 
('Emmanuel Mudiay', 1610612762, 1626144, 2019)]


    
 