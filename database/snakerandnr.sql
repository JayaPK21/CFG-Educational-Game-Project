USE group3_educational_game_project;

CREATE DATABASE group3_educational_game_project;
USE group3_educational_game_project;

CREATE table round (
Round_id int NOT NULL, 
Player_id int NOT NULL, 
Game_id int NOT NULL, 
primary key (Round_id)
);

CREATE table game (
Game_id int NOT NULL,
Round_id int NOT NULL, 
Score_id int NOT NULL, 
primary key (Game_id)
);

CREATE table score (
Score_id int NOT NULL, 
Game_id int NOT NULL,
Score_date date NOT NULL, 
Score int NOT NULL, 
Wins int NOT NULL, 
Losses int NOT NULL, 
Draws int NOT NULL, 
primary key (Score_id)
);

CREATE table game (
Game_id int NOT NULL,
Round_id int NOT NULL, 
Score_id int NOT NULL, 
primary key (Game_id)
);



CREATE table player (
Player_id int NOT NULL, 
Player_name char(50) NOT NULL, 
primary key (Player_id)
);