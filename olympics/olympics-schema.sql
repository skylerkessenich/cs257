CREATE TABLE athlete (
	id SERIAL,
	name text,
<<<<<<< HEAD:olympics/olympics-schema.sql
	sex text);

CREATE TABLE nation (
=======
	sex text,
	height float,
	weight float);

CREATE TABLE team (
>>>>>>> 5d3ee4c8469b97437ff35501873e128137353d88:olympics/archive/olympics-schema.sql
	id SERIAL,
	NOC text,
	country text);

CREATE TABLE events (
	id SERIAL,
	sport text,
	event text);

CREATE TABLE games(
	id SERIAL,
	game text,
	year integer,
	season text,
	location text);

CREATE TABLE olympics(
	athleteId SERIAL,
	age integer,
	height float,
	weight float,
	nationID SERIAL,
	eventID SERIAL,
	gameID SERIAL,
	medal text);





