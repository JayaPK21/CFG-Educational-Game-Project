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


USE group3_educational_game_project;

INSERT INTO player(Player_ID, Player_name)
VALUES
   (1, "Alice"),
   (2, "Belen"),
   (3, "Ciara"),
   (4, "Delia"),
   (5, "Everly"),
   (6, "Fabia"),
   (7, "Grace")
;

INSERT INTO score (Score_id,Game_id, Score_date, Score,Wins,Losses, Draws)
VALUES
   (1, 1, 2023-05-20, 7,4,2,0),
   (2, 2, 2023-04-25,8,10,6,2),
   (3, 3, 2023-01-09, 1, 6,2, 0),
   (4, 4, 2023-02-24, 1, 3,9, 1),
   (5, 5, 2023-12-15, 1, 9, 8, 2),
   (6, 6, 2023-05-04, 8, 1, 4,1),
   (7, 7,2023-01-23, 1, 2,3,0)
   ;

INSERT INTO round (round_id, player_id, game_id)
VALUES
   (1, 1, 1),
   (2, 2, 2),
   (3, 3, 3),
   (4, 4, 4),
   (5, 5, 5),
   (6, 6, 6),
   (7, 7, 7)
   ;

INSERT INTO game (game_id, round_id, score_id)
VALUES
   (1, 1, 1),
   (2, 2, 2),
   (3, 3, 3),
   (4, 4, 4),
   (5, 5, 5),
   (6, 6, 6),
   (7, 7, 7)
   ;
 
 

USE group3_educational_game_project;

select p.Player_name, s.wins, s.losses,s.draws
from player p
inner join score s
on s.score_id = s.id
order by player_id
;


INSERT INTO score (Score_id,Game_id, Score_date, Score,Wins,Losses, Draws)
VALUES
   (8, 1, 2023-05-20, 7,4,2,0)