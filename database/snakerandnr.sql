USE groupa_educational_game_project;

-- creating the DATABASE group3a_educational_game_project
CREATE DATABASE group3a_educational_game_project;
USE groupa_educational_game_project;

-- creating the player table 
CREATE TABLE group3a_educational_game_project.p_player (
  player_id INT NOT NULL,
  player_name VARCHAR(45) NULL,
  PRIMARY KEY (player_id)
  );

-- creating the game table
CREATE table group3a_educational_game_project.game (
game_id int NOT NULL,
player_id int,
primary key (Game_id),
FOREIGN KEY (player_id) REFERENCES p_player(player_id)
);

-- creating the score table 
CREATE table group3a_educational_game_project.score (
score_id int NOT NULL,
player_id int,
sc_date date NOT NULL, 
score int NOT NULL, 
primary key (Score_id),
FOREIGN KEY (player_id) REFERENCES p_player(player_id)
);


USE group3_educational_game_project;

-- input data into the player table 
INSERT INTO player(player_id, player_name)
VALUES
   (1, "Alice"),
   (2, "Belen"),
   (3, "Ciara"),
   (4, "Delia"),
   (5, "Everly"),
   (6, "Fabia"),
   (7, "Grace")
;

-- input data into the  score table 
INSERT INTO group3a_educational_game_project.score (score_id, player_id, sc_date, score)
VALUES
     (111, 1, '2023-05-20', 10),
     (112, 2,  '2023-04-25', 8),
     (113, 3, '2023-01-09', 1),
	  (114, 4,  '2023-02-24', 5),
	  (115, 5,  '2023-12-15', 9),
     (116, 6,  '2023-05-04', 8),
     (117, 7,  '2023-01-23', 3),
     (118, 7,  '2023-02-23', 5),
 	  (119, 7,  '2023-03-20', 2),
     (120, 7,  '2023-05-15', 3),
	  (121, 1,   '2023-04-22', 10),
	  (122,  2,  '2023-04-20', 4),
 	  (123,  3,  '2023-01-09 ', 7),
	  (124,  4,  '2023-01-09', 4),
     (125,  5,  '2023-02-10 ', 1), 	 
     (126,  6,  '2023-02-11', 0),
     (127,  7, '2023-02-12', 4),
      (128,  7,  '2023-02-13', 6),
      (129,  7,  '2023-02-14', 9),
      (130,  7,  '2023-12-9', 10),
	   (131,  1,  '2023-12-10', 6),
      (132,  2,  '2023-12-11', 7),
      (133,  3,  '2023-12-12', 7),
	   (134,  4,  '2023-12-13', 8),
      (135,  5,  '2023-12-14', 10),
     (136,  6,  '2023-12-16', 4),     
     (137,  7,  '2023-05-17 ', 8)
;

-- input data into the game table 
INSERT INTO group3a_educational_game_project.game (game_id, player_id)
VALUES
   (101,  1),
   (102,  2),
   (103,  3),
   (104,  4),
   (105,  5),
   (106,  6),
   (107,  7),
   (108,  7),
   (109,  7),
   (110,  7),
   (111,  1),
   (112,  2),
   (113,  3),
   (114,  4),
   (115,  5),
   (116,  6),
   (117,  7),
   (118,  7),
   (119,  7),
   (120,  7),
   (121,  1),
   (122,  2),
   (123,  3),
   (124,  4),
   (125,  5),
   (126,  6),
   (127,  7),
   (128,  7),
   (129,  7),
   (130,  7)
   ;

USE group3_educational_game_project;

-- old query 
select p.Player_name, s.wins, s.losses,s.draws
from player p
inner join score s
on s.score_id = s.id
order by player_id
;
-- new query due to changes 
select p.player_name, s.sc_date, s.score
from player p
inner join score s
on s.score_id = s.id
order by player_id
;