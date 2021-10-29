#!/usr/bin/env python3
'''
Skyler Kessenich Oct 28th
'''
import sys
import argparse
import flask
import json
import psycopg2

app = flask.Flask(__name__)

@app.route('/')
def home():
    return flask.render_template('help.html')

@app.route('/games')
def games():
    finalList=[]
    try: #connect to database
        connection = psycopg2.connect(database='olympics',user='skylerkessenich')
        cursor = connection.cursor()
    except Exception as e:
        print(e)
        exit()
    query='SELECT * FROM games;' #selects all the games data
    cursor.execute(query)
    for row in cursor:
        gameDict={'id':row[0],'year':row[2],'season':row[3],'city':row[4]} #puts data into the dictionary
        finalList.append(gameDict)
    return json.dumps(finalList)


@app.route('/NOC')
def NOC():
    finalList=[]
    try:    #connect to database
        connection = psycopg2.connect(database='olympics',user='skylerkessenich')
        cursor = connection.cursor()
    except Exception as e:
        print(e)
        exit()
    query='SELECT * FROM nation ORDER BY nation.NOC ASC;' #selects all the nation data
    cursor.execute(query)
    for row in cursor:
        NOCDict = {'abbreviation':row[1],'name':row[2]}
        finalList.append(NOCDict)
    return json.dumps(finalList)



@app.route('/medalists/games/<games_id>')
def medalists(games_id,noc=None):
    finalList=[]
    try: #connect to database
        connection = psycopg2.connect(database='olympics',user='skylerkessenich')
        cursor = connection.cursor()
    except Exception as e:
        print(e)
        exit()
    noc = flask.request.args.get('noc',default=None)
    if noc==None: #if there is no specified NOC then execute this query
        query='SELECT athlete.id, athlete.name, athlete.sex, events.sport, events.event, olympics.medal FROM athlete, olympics, events WHERE olympics.medal IN ({}Gold{},{}Silver{},{}Bronze{}) AND events.id={} AND olympics.eventID=events.id AND olympics.athleteID=athlete.id;'.format("'","'","'","'","'","'",games_id) #selects all the games data
    else: #else do this query
            query='SELECT athlete.id, athlete.name, athlete.sex, events.sport, events.event, olympics.medal FROM athlete, olympics, events, nation WHERE olympics.medal IN ({}Gold{},{}Silver{},{}Bronze{}) AND events.id={} AND olympics.eventID=events.id AND olympics.athleteID=athlete.id AND nation.NOC={}{}{} AND olympics.nationID=nation.id;'.format("'","'","'","'","'","'",games_id,"'",noc,"'")
    cursor.execute(query)
    for row in cursor:
        gameMedalDict = {'athlete_id':row[0],'athlete_name':row[1],'athlete_sex':row[2],'sport':row[3],'event':row[4],'medal':row[5]} #format data
        finalList.append(gameMedalDict)
    return json.dumps(finalList)


if __name__ == '__main__':
    parser = argparse.ArgumentParser('A sample Flask application demonstrating templates.')
    parser.add_argument('host', help='the host on which this application is running')
    parser.add_argument('port', type=int, help='the port on which this application is listening')
    arguments = parser.parse_args()
    app.run(host=arguments.host, port=arguments.port, debug=True)
