"""Skyler Kessenich, Oct 21st 2021
This program takes the data in the olimpics.csv and reads it into new csv files to be stored in a table"""

import csv

def readFile(csvreader):
	athleteTrack={}
	#counters for i.d
	eID=1
	gID=1
	nID=1
	#dictionaries to check for reeats
	nationDict={}
	gameDict={}
	eventDict={}
	#creates csv writers for files
	fileAthlete=open('athlete.csv', mode = 'w') #opens athlete.csv for writing
	csvAthlete=csv.writer(fileAthlete, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL) #creates a csv writer
	fileEvents=open('events.csv', mode = 'w') #opens events.csv for writing
	csvEvents=csv.writer(fileEvents, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL) #creates a csv writer
	fileGames=open('games.csv', mode = 'w') #opens games.csv for writing
	csvGames=csv.writer(fileGames, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL) #creates a csv writer
	olympic=open('olympics.csv', mode = 'w') 
	fileTeam=open('nations.csv', mode = 'w')  #opens teams.csv for writing
	csvTeam=csv.writer(fileTeam, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL) #creates a csv writer
	csvOly=csv.writer(olympic, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
	for entry in csvreader: #for every entry in athlete_events.csv, if the id is in our tracking list then ignore, if not add it
		if athleteTrack.get(entry[0]) == None:
			#creates new athlete
			csvAthlete.writerow([entry[0],entry[1],entry[2]])
			athleteTrack[entry[0]]=1
		if eventDict.get(entry[13])==None: 
			#creates new event
			csvEvents.writerow([eID,entry[12], entry[13]])
			eventDict[entry[13]]=eID
			eID+=1
		if gameDict.get(entry[8])==None:
			#creates a new game
			csvGames.writerow([gID,entry[8], entry[9],entry[10],entry[11]])
			gameDict[entry[8]]=gID
			gID+=1
		if nationDict.get(entry[7]) == None:
			#creates new country
			csvTeam.writerow([nID,entry[7],entry[6]])
			nationDict[entry[7]]=nID
			nID+=1
		nationId=nationDict[entry[7]]
		eventID=eventDict[entry[13]]
		gameID=gameDict[entry[8]]
		#formats the NA values to NULL
		if entry[-1]=='NA':
			entry[-1]='NULL'
		if entry[3]=='NA':
			entry[3]='NULL'
		if entry[4]=='NA':
			entry[4]='NULL'
		if entry[5]=='NA':
			entry[5]='NULL'
		#creates a new olympic entry
		newEntry=[entry[0],entry[3],entry[4],entry[5],nationId,eventID,gameID,entry[-1]]
		csvOly.writerow(newEntry)



def main():
	file = open('athlete_events.csv')
	csvreader = csv.reader(file)
	header=next(csvreader)
	readFile(csvreader)
	file.close()
	exit()



if __name__ == '__main__':
	main()





