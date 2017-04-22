BEGIN TRANSACTION;
CREATE TABLE `users` (
	`id`	INTEGER,
	`email`	TEXT NOT NULL,
	PRIMARY KEY(`id`)
);
INSERT INTO `users` VALUES (1,'piggy');
INSERT INTO `users` VALUES (2,'lolo');
CREATE TABLE "picks" (
	`id`	INTEGER,
	`email`	INTEGER NOT NULL,
	`uid`	INTEGER NOT NULL,
	`amount`	INTEGER NOT NULL,
	PRIMARY KEY(`id`)
);
INSERT INTO `picks` VALUES (1,'piggy','aaa',18);
INSERT INTO `picks` VALUES (2,'piggy','ccc',21);
INSERT INTO `picks` VALUES (3,'piggy','bbb',27);
INSERT INTO `picks` VALUES (4,'lolo','ccc',9);
INSERT INTO `picks` VALUES (6,'lolo','bbb',5);
INSERT INTO `picks` VALUES (7,'lolo','aaa',6);
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
