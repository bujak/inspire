BEGIN TRANSACTION;
CREATE TABLE `users` (
	`id`	INTEGER,
	`email`	TEXT NOT NULL,
	PRIMARY KEY(`id`)
);
CREATE TABLE `picks` (
	`id`	INTEGER,
	`user_id`	INTEGER NOT NULL,
	`beacon_id`	INTEGER NOT NULL,
	`amount`	INTEGER NOT NULL,
	PRIMARY KEY(`id`)
);
CREATE TABLE `beacons` (
	`id`	INTEGER,
	`uid`	TEXT NOT NULL,
	`product`	TEXT NOT NULL,
	PRIMARY KEY(`id`)
);
INSERT INTO `beacons` VALUES (1,'N02W','Audi');
INSERT INTO `beacons` VALUES (2,'ahGH','Ferrari');
INSERT INTO `beacons` VALUES (3,'JKyi','Fiat126p');
COMMIT;
