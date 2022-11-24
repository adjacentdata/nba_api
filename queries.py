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

    CREATE_NBA_GAMES_TABLE = (""" 
    	CREATE TABLE IF NOT EXISTS games
	(
	GAME_DATE_EST date,
	GAME_ID	int,
	GAME_STATUS_TEXT varchar(10),
	HOME_TEAM_ID int,
	VISITOR_TEAM_ID	int,
	SEASON int,
	TEAM_ID_home int,
	PTS_home varchar,
	FG_PCT_home varchar,
	FT_PCT_home	varchar,
	FG3_PCT_home varchar,
	AST_home varchar,
	REB_home varchar,
	TEAM_ID_away varchar,
	PTS_away varchar,
	FG_PCT_away	varchar,
	FT_PCT_away	varchar,
	FG3_PCT_away varchar,
	AST_away varchar,
	REB_away varchar,
	HOME_TEAM_WINS int
	)
    """)
    
        
    GET_ALL_PLAYERS = "SELECT * FROM players LIMIT 10"
