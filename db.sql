BEGIN TRANSACTION;
CREATE TABLE `users` (
	`id`	INTEGER,
	`email`	TEXT NOT NULL,
	PRIMARY KEY(`id`)
);
INSERT INTO `users` VALUES (1,'piggy');
INSERT INTO `users` VALUES (2,'lolo');
INSERT INTO `users` VALUES (3,'hesus');
INSERT INTO `users` VALUES (4,'noname');
CREATE TABLE "picks" (
	`id`	INTEGER,
	`email`	INTEGER NOT NULL,
	`uid`	INTEGER NOT NULL,
	`amount`	INTEGER NOT NULL,
	`day`	TEXT,
	PRIMARY KEY(`id`)
);
INSERT INTO `picks` VALUES (1,'piggy','ahGH',37,'2017-04-22');
INSERT INTO `picks` VALUES (2,'piggy','N02W',34,'2017-04-22');
INSERT INTO `picks` VALUES (3,'piggy','JKyi',66,'2017-04-22');
INSERT INTO `picks` VALUES (4,'lolo','N02W',22,'2017-04-22');
INSERT INTO `picks` VALUES (6,'lolo','JKyi',44,'2017-04-22');
INSERT INTO `picks` VALUES (7,'lolo','ahGH',25,'2017-04-22');
INSERT INTO `picks` VALUES (8,'noname','ahGH
',16,'2017-04-22');
INSERT INTO `picks` VALUES (9,'noname','JKyi',40,'2017-04-22');
INSERT INTO `picks` VALUES (10,'noname','N02W',39,'2017-04-22');
INSERT INTO `picks` VALUES (11,'hesus','JKyi',15,'2017-04-23');
INSERT INTO `picks` VALUES (12,'hesus','N02W',14,'2017-04-23');
INSERT INTO `picks` VALUES (13,'hesus','N02W',14,'2017-04-23');
INSERT INTO `picks` VALUES (14,'noname','JKyi',40,'2017-04-23');
INSERT INTO `picks` VALUES (15,'piggy','ahGH',37,'2017-04-24');
INSERT INTO `picks` VALUES (16,'piggy','ahGH',37,'2017-04-25');
INSERT INTO `picks` VALUES (17,'piggy','ahGH',37,'2017-04-26');
CREATE TABLE `beacons` (
	`id`	INTEGER,
	`uid`	TEXT NOT NULL,
	`product`	TEXT NOT NULL,
	PRIMARY KEY(`id`)
);
INSERT INTO `beacons` VALUES (1,'ahGH','Audi');
INSERT INTO `beacons` VALUES (2,'JKyi','Ferrari');
INSERT INTO `beacons` VALUES (3,'N02W','Fiat126p');
COMMIT;
