CREATE TABLE IF NOT EXISTS allusers(
	userid VARCHAR(15),
	fname VARCHAR(20),
	lname VARCHAR(20),
	uname VARCHAR(20),
	PRIMARY KEY (userid)
);

CREATE TABLE IF NOT EXISTS bangroups(
	groupid VARCHAR(15),
	title VARCHAR(50),
	PRIMARY KEY (groupid)
);

CREATE TABLE IF NOT EXISTS groups(
	groupid VARCHAR(15),
	title VARCHAR(50),
	welcomeMessage VARCHAR(255),
	stickerPermission VARCHAR(5),
	hhhPermission VARCHAR(5),
	PRIMARY KEY (groupid)
);

CREATE TABLE IF NOT EXISTS subscribe(
	subsname VARCHAR(20),
	userid VARCHAR(15),
	count INT,
	PRIMARY KEY (subsname),
	FOREIGN KEY (userid) REFERENCES allusers(userid)
);

CREATE TABLE IF NOT EXISTS superadmin(
	userid VARCHAR(15),
	PRIMARY KEY (userid),
	FOREIGN KEY (userid) REFERENCES allusers(userid)
);

CREATE TABLE IF NOT EXISTS users(
	groupid VARCHAR(15),
	userid VARCHAR(15),
	PRIMARY KEY (groupid, userid),
	FOREIGN KEY (groupid) REFERENCES groups(groupid),
	FOREIGN KEY (userid) REFERENCES allusers(userid)
);