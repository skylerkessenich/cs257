SELECT NOC FROM nation 
ORDER BY NOC ASC;

SELECT DISTINCT athlete.name FROM athlete, olympics
WHERE olympics.nationID=85 and athlete.id=olympics.athleteId;

SELECT olympics.medal, games.game, events.event, athlete.name FROM olympics, games, events, athlete
WHERE olympics.athleteID=71665 AND games.id=olympics.gameID AND olympics.eventID=events.id AND athlete.id=71665 AND olympics.medal IN ('Gold','Silver','Bronze')
ORDER BY games.year;

SELECT COUNT(olympics.medal='Gold'), nation.NOC FROM olympics, nation
WHERE olympics.nationID=nation.id 
GROUP BY nation.NOC
ORDER BY COUNT(olympics.medal='Gold') DESC;




