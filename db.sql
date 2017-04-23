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

CREATE TABLE `product_details` (
	`id`	INTEGER,
	`product`	TEXT,
	`details`	TEXT,
	PRIMARY KEY(`id`)
);
INSERT INTO `product_details` VALUES (1,'Audi','{"price": "10k$", 
"name":"Audi","engine":"168-hp, 2.5-liter I-4 (regular gas)",
"transmission":"2-speed CVT w/OD and auto-manual, 6-speed manual w/OD",
"combined_mpg":"27",
"city_mpg":"27",
"highway_mpg":"37",
}');
INSERT INTO `product_details` VALUES (2,'Fiat','{"price": "150k$","name":"Fiat","engine":"185-hp, 2.4-liter I-4 (regular gas)",
"transmission":"2-speed CVT w/OD",
"combined_mpg":"25",
"city_mpg":"22",
"highway_mpg":"11"}');
INSERT INTO `product_details` VALUES (3,'Ferrari','{	"price": "250k$"
	"name":"Ferrari",
	"engine":"196-hp, 2.5-liter I-4 (regular gas)",
	"transmission":"6-speed automatic w/OD",
	"combined_mpg":"25",
	"city_mpg":"22",
	"highway_mpg":"31",
}');

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
