CREATE TABLE athlete (
	id SERIAL,
	name text,
	sex text);

CREATE TABLE nation (
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





