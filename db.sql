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
INSERT INTO `picks` VALUES (1,'piggy','aaa',37,'2017-04-22');
INSERT INTO `picks` VALUES (2,'piggy','ccc',34,'2017-04-22');
INSERT INTO `picks` VALUES (3,'piggy','bbb',66,'2017-04-22');
INSERT INTO `picks` VALUES (4,'lolo','ccc',22,'2017-04-22');
INSERT INTO `picks` VALUES (6,'lolo','bbb',44,'2017-04-22');
INSERT INTO `picks` VALUES (7,'lolo','aaa',25,'2017-04-22');
INSERT INTO `picks` VALUES (8,'noname','aaa',16,'2017-04-22');
INSERT INTO `picks` VALUES (9,'noname','bbb',40,'2017-04-22');
INSERT INTO `picks` VALUES (10,'noname','ccc',39,'2017-04-22');
INSERT INTO `picks` VALUES (11,'hesus','bbb',15,'2017-04-23');
INSERT INTO `picks` VALUES (12,'hesus','ccc',14,'2017-04-23');
INSERT INTO `picks` VALUES (13,'hesus','ccc',14,'2017-04-23');
CREATE TABLE `beacons` (
	`id`	INTEGER,
	`uid`	TEXT NOT NULL,
	`product`	TEXT NOT NULL,
	PRIMARY KEY(`id`)
);
INSERT INTO `beacons` VALUES (1,'aaa','Audi');
INSERT INTO `beacons` VALUES (2,'bbb','Ferrari');
INSERT INTO `beacons` VALUES (3,'ccc','Fiat126p');
COMMIT;
