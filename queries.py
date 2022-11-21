class Players:
    CREATE_NBA_PLAYERS_TABLE = ("""
        CREATE TABLE IF NOT EXISTS players 
        (PLAYER_NAME varchar(255),
        TEAM_ID int,
        PLAYER_ID int,
        SEASON int)
        """)
        
    GET_ALL_PLAYERS = "SELECT * FROM players LIMIT 10"
