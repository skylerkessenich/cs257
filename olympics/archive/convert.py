"""Skyler Kessenich, Oct 14th 2021
This program takes the data in the olimpics.csv and reads it into new csv files to be stored in a table"""

import csv

def readFile(csvreader):
	athleteTrack=[]
	eventTrack=[]
	gameTrack=[]
	nationTrack=[]
	eID=1
	gID=1
	nID=1
	teamDict={}
	gameDict={}
	eventDict={}
	fileAthlete=open('athlete.csv', mode = 'w') #opens athlete.csv for writing
	csvAthlete=csv.writer(fileAthlete, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL) #creates a csv writer
	fileEvents=open('events.csv', mode = 'w') #opens events.csv for writing
	csvEvents=csv.writer(fileEvents, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL) #creates a csv writer
	fileGames=open('games.csv', mode = 'w') #opens games.csv for writing
	csvGames=csv.writer(fileGames, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL) #creates a csv writer
	olympic=open('olympics.csv', mode = 'w') 
	fileTeam=open('teams.csv', mode = 'w')  #opens teams.csv for writing
	csvTeam=csv.writer(fileTeam, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL) #creates a csv writer
	csvOly=csv.writer(olympic, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
	for entry in csvreader: #for every entry in athlete_events.csv, if the id is in our tracking list then ignore, if not add it
		if entry[0] not in athleteTrack:
			if entry[4]=='NA':
				entry[4]='NULL'
			if entry[5]=='NA':
				entry[5]='NULL'
			csvAthlete.writerow([entry[0],entry[1],entry[2], entry[4],entry[5]])
			athleteTrack.append(entry[0])
		if entry[13] not in eventTrack:
			csvEvents.writerow([eID,entry[12], entry[13]])
			eventDict[entry[13]]=eID
			eID+=1
			eventTrack.append(entry[13])
		if entry[8] not in gameTrack:
			csvGames.writerow([gID,entry[8], entry[9],entry[10],entry[11]])
			gameDict[entry[8]]=gID
			gID+=1
			gameTrack.append(entry[8])
		if entry[7] not in nationTrack:
			csvTeam.writerow([nID,entry[7],entry[6]])
			teamDict[entry[7]]=nID
			nID+=1
			nationTrack.append(entry[7])
		nationId=teamDict[entry[7]]
		eventID=eventDict[entry[13]]
		gameID=gameDict[entry[8]]
		if entry[-1]=='NA':
			entry[-1]=='NULL'
		if entry[3]=='NA':
			entry[3]='NULL'
		newEntry=[entry[0],entry[3],nationId,eventID,gameID,entry[-1]]
		csvOly.writerow(newEntry)



		

def createAge():
	tracker=[]
	with open('age.csv', mode = 'w') as fileW: #opens age.csv for writing
		csvwriter=csv.writer(fileW, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL) #creates a csv writer
		for i in range(1,101): #we are going to write ages from 1 to 101 for possible ages
			csvwriter.writerow([i,i]) 


def createMedals():
	with open('medals.csv', mode = 'w') as fileW: #opens games.csv for writing
		csvwriter=csv.writer(fileW, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL) #creates a csv writer
		csvwriter.writerow(['id','medal'])
		csvwriter.writerow(['1','Bronze'])
		csvwriter.writerow(['2','Silver'])
		csvwriter.writerow(['3','Gold'])
		csvwriter.writerow(['4','NA'])



def main():
	file = open('athlete_events.csv')
	csvreader = csv.reader(file)
	header=next(csvreader)
	createAge()
	createMedals()
	readFile(csvreader)

	exit()



if __name__ == '__main__':
	main()





