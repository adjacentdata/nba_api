class Players:
    CREATE_NBA_PLAYERS_TABLE = ("""
        CREATE TABLE IF NOT EXISTS players 
        (PLAYER_NAME varchar(255),
        TEAM_ID int,
        PLAYER_ID int,
        SEASON int)
        """)
        
    GET_ALL_PLAYERS = "SELCT * FROM nba_players"

    INSERT_PLAYER = "INSERT INTO players (player_name, team_id, player_id, season) VALUES (%s, %s, %s) "


