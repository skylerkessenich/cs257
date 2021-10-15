CREATE TABLE athlete (
	id SERIAL,
	name text,
	sex text,
	height float,
	weight float);

CREATE TABLE age (
	id SERIAL,
	age integer);

CREATE TABLE team (
	id SERIAL,
	team text,
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
	nationID SERIAL,
	eventID SERIAL,
	gameID SERIAL,
	medal text);





