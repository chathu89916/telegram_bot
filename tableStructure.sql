CREATE TABLE IF NOT EXISTS allusers(
	userid TEXT,
	fname TEXT,
	lname TEXT,
	uname TEXT,
	PRIMARY KEY (userid)
);

CREATE TABLE IF NOT EXISTS bangroups(
	groupid TEXT,
	title TEXT,
	PRIMARY KEY (groupid)
);

CREATE TABLE IF NOT EXISTS groups(
	groupid TEXT,
	title TEXT,
	welcomeMessage TEXT,
	stickerPermission TEXT,
	hhhPermission TEXT,
	PRIMARY KEY (groupid)
);

CREATE TABLE IF NOT EXISTS subscribe(
	userid TEXT,
	subsname TEXT,
	count INTEGER,
	PRIMARY KEY (userid, subsname),
	FOREIGN KEY (userid) REFERENCES allusers(userid)
);

CREATE TABLE IF NOT EXISTS superadmin(
	userid TEXT,
	PRIMARY KEY (userid),
	FOREIGN KEY (userid) REFERENCES allusers(userid)
);

CREATE TABLE IF NOT EXISTS users(
	groupid TEXT,
	userid TEXT,
	PRIMARY KEY (groupid, userid),
	FOREIGN KEY (groupid) REFERENCES groups(groupid),
	FOREIGN KEY (userid) REFERENCES allusers(userid)
);