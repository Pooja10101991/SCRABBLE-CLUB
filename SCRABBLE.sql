CREATE TABLE player_details(
mem_id INT PRIMARY KEY,
first_name VARCHAR(20),
last_name VARCHAR(20),
phone_no INT,
email_id VARCHAR(50));

CREATE TABLE game_details(
game_id INT PRIMARY KEY,
game_date DATE,
game_place VARCHAR(20)
);

CREATE TABLE score_details(
game_id INT,
player1 INT,
player2 INT,    
player1_score FLOAT,
player1_score FLOAT,  
PRIMARY KEY(game_id,player1,player2),
FOREIGN KEY(player1) REFERENCES player_details(mem_id),
FOREIGN KEY(player2) REFERENCES player_details(mem_id),
FOREIGN KEY(game_id) REFERENCES game_details(game_id)
);

INSERT INTO player_details VALUES (1,'David','Wallace',1928364,'david.wall@mail.com');
INSERT INTO player_details VALUES (2,'Jan','Levinson',26374856,'jan.levi@mail.com');
INSERT INTO player_details VALUES (3,'Michal','Scott',26374856,'mic.scott@mail.com');
INSERT INTO player_details VALUES (4,'Angela','Martin',56789568,'angel.ma@mail.com');
INSERT INTO player_details VALUES (5,'Kelly','Kooper',26374856,'kel.kop@mail.com');
INSERT INTO player_details VALUES (6,'Stanley','Hudson',2345678,'sta.hud@mail.com');

INSERT INTO game_details(game_id,game_date,game_place) VALUES (101,'2020-03-03','Leeds');
INSERT INTO game_details(game_id,game_date,game_place) VALUES (102,'2020-03-30','York');
INSERT INTO game_details(game_id,game_date,game_place) VALUES (103,'2020-04-13','Manchester');
INSERT INTO game_details(game_id,game_date,game_place) VALUES (104,'2020-04-18','London');
INSERT INTO game_details(game_id,game_date,game_place) VALUES (105,'2020-05-18','Leeds');
INSERT INTO game_details(game_id,game_date,game_place) VALUES (106,'2020-05-29','York');
INSERT INTO game_details(game_id,game_date,game_place) VALUES (107,'2020-06-02','Bristol');
INSERT INTO game_details(game_id,game_date,game_place) VALUES (108,'2020-06-22','Bath');
INSERT INTO game_details(game_id,game_date,game_place) VALUES (109,'2020-06-30','Oxford');
INSERT INTO game_details(game_id,game_date,game_place) VALUES (110,'2020-07-05','london');
INSERT INTO game_details(game_id,game_date,game_place) VALUES (111,'2020-07-11','Bristol');
INSERT INTO game_details(game_id,game_date,game_place) VALUES (112,'2020-07-20','Leeds');
INSERT INTO game_details(game_id,game_date,game_place) VALUES (113,'2021-06-05','Lords');
INSERT INTO game_details(game_id,game_date,game_place) VALUES (114,'2021-06-15','Leeds');
INSERT INTO game_details(game_id,game_date,game_place) VALUES (115,'2021-06-25','Reading');
INSERT INTO game_details(game_id,game_date,game_place) VALUES (116,'2021-07-05','Oxford');
INSERT INTO game_details(game_id,game_date,game_place) VALUES (117,'2021-07-15','Bath');
INSERT INTO game_details(game_id,game_date,game_place) VALUES (118,'2021-07-25','Bath');
INSERT INTO game_details(game_id,game_date,game_place) VALUES (119,'2021-07-26','London');
INSERT INTO game_details(game_id,game_date,game_place) VALUES (120,'2021-07-30','Leeds');



INSERT INTO score_details(game_id,player1,player2,player1_score,player2_score) VALUES (101,1,2,450,350);
INSERT INTO score_details(game_id,player1,player2,player1_score,player2_score) VALUES (102,1,3,400,350);
INSERT INTO score_details(game_id,player1,player2,player1_score,player2_score) VALUES (103,2,3,450,400);
INSERT INTO score_details(game_id,player1,player2,player1_score,player2_score) VALUES (104,1,2,350,400);
INSERT INTO score_details(game_id,player1,player2,player1_score,player2_score) VALUES (105,2,4,450,400);
INSERT INTO score_details(game_id,player1,player2,player1_score,player2_score) VALUES (106,1,4,300,280);
INSERT INTO score_details(game_id,player1,player2,player1_score,player2_score) VALUES (107,3,1,350,400);
INSERT INTO score_details(game_id,player1,player2,player1_score,player2_score) VALUES (108,1,5,400,380);
INSERT INTO score_details(game_id,player1,player2,player1_score,player2_score) VALUES (109,1,5,350,450);
INSERT INTO score_details(game_id,player1,player2,player1_score,player2_score) VALUES (110,1,5,400,450);
INSERT INTO score_details(game_id,player1,player2,player1_score,player2_score) VALUES (111,3,1,400,380);
INSERT INTO score_details(game_id,player1,player2,player1_score,player2_score) VALUES (112,1,6,300,450);
INSERT INTO score_details(game_id,player1,player2,player1_score,player2_score) VALUES (113,1,2,341,361);
INSERT INTO score_details(game_id,player1,player2,player1_score,player2_score) VALUES (114,2,3,352,431);
INSERT INTO score_details(game_id,player1,player2,player1_score,player2_score) VALUES (115,2,1,452,413);
INSERT INTO score_details(game_id,player1,player2,player1_score,player2_score) VALUES (116,4,2,361,422);
INSERT INTO score_details(game_id,player1,player2,player1_score,player2_score) VALUES (117,2,6,445,446);
INSERT INTO score_details(game_id,player1,player2,player1_score,player2_score) VALUES (118,2,1,455,321);
INSERT INTO score_details(game_id,player1,player2,player1_score,player2_score) VALUES (119,2,4,431,433);
INSERT INTO score_details(game_id,player1,player2,player1_score,player2_score) VALUES (120,6,2,360,429);
