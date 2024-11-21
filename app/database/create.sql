CREATE TABLE Users (
	user_id INTEGER PRIMARY KEY,
	first_name VARCHAR2(50) NOT NULL,
	last_name VARCHAR2(50) NOT NULL,
	age INTEGER NOT NULL,
	email_address VARCHAR2(100) UNIQUE NOT NULL,
	password VARCHAR2(255) NOT NULL,
	date_of_birth DATE NOT NULL,
	role VARCHAR2(50) NOT NULL
);

CREATE TABLE Teams (
        team_id INTEGER PRIMARY KEY,
        team_name VARCHAR2(20) UNIQUE NOT NULL,
        skill_level VARCHAR2(20) NOT NULL
);

CREATE TABLE Players (
	player_id INTEGER PRIMARY KEY REFERENCES Users(user_id) ON DELETE CASCADE,
	team_id INTEGER REFERENCES Teams(team_id),
	position VARCHAR2(20) NOT NULL,
	skill_level VARCHAR2(20) DEFAULT 'beginner' NOT NULL
);

CREATE TABLE Referees (
	referee_id INTEGER PRIMARY KEY REFERENCES Users(user_id) ON DELETE CASCADE,
	experience_level VARCHAR2(50) NOT NULL
);

CREATE TABLE House_League (
	match_id INTEGER PRIMARY KEY,
	match_date DATE NOT NULL,
	skill_level VARCHAR2(20) NOT NULL,
	ht_id INTEGER REFERENCES Teams(team_id),
	at_id INTEGER REFERENCES Teams(team_id),
	ht_score INTEGER,
	at_score INTEGER
);

CREATE TABLE Match_Stats (
	match_id INTEGER REFERENCES House_League(match_id) ON DELETE CASCADE,
	player_id INTEGER REFERENCES Players(player_id) ON DELETE CASCADE,
	goals INTEGER,
	assists INTEGER,
	minutes_played INTEGER,
	yellow_cards INTEGER,
	red_cards INTEGER,
	attempted_goals INTEGER,
	PRIMARY KEY(match_id, player_id)
);

CREATE TABLE Match_Referee (
	match_id INTEGER REFERENCES House_League(match_id) ON DELETE CASCADE,
	referee_id INTEGER REFERENCES Referees(referee_id) ON DELETE CASCADE,
	PRIMARY KEY(match_id, referee_id)
);
