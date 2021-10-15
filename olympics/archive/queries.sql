SELECT team FROM team 
ORDER BY team ASC;

SELECT athlete.name FROM athlete, olympics
WHERE olympics.nationID=85 and athlete.id=olympics.athleteId;

SELECT olympics.medal, games.game, events.event, athlete.name FROM olympics, games, events, athlete
WHERE olympics.athleteID=71665 AND games.id=olympics.gameID and olympics.eventID=events.id AND athlete.id=71665 AND NOT olympics.medal='NA'
ORDER BY games.year;


