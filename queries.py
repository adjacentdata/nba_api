class Players:
    CREATE_NBA_PLAYERS_TABLE = ("""
        CREATE TABLE IF NOT EXISTS players 
        (PLAYER_NAME varchar(255),
        TEAM_ID int,
        PLAYER_ID int,
        SEASON int)
        """)
    
    CREATE_NBA_TEAMS_TABLE = ("""
        CREATE TABLE IF NOT EXISTS teams
        (LEAGUE_ID int,
        TEAM_ID int,
        MIN_YEAR int,
        MAX_YEAR int,
        ABBREVIATION varchar(5),
        NICKNAME varchar(255),
        YEARFOUNDED int,
        CITY varchar(255),
        ARENA varchar(255),
        ARENACAPACITY varchar(255),
        OWNER varchar(255),
        GENERALMANAGER varchar(255),
        HEADCOACH varchar(255),
        DLEAGUEAFFILIATION varchar(255));
        """)
    
        
    GET_ALL_PLAYERS = "SELECT * FROM players LIMIT 10"
