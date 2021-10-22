'''Skyler Kessenich Oct 21st'''

import argparse
import psycopg2

def parseArgs():
	#parses the desired args 
	parser=argparse.ArgumentParser()
	parser.add_argument('--athletes','-a',nargs='+',help='lists all the athletes from a specified NOC. Need to input a NOC')
	parser.add_argument('--leaders','-l',action='store_true',help='lists all NOCs and their gold medals and sorts them in decending order of medals')
	parser.add_argument('--events','-e',nargs='+',help='lists all the events from a specified sport. Need to input a valid sport (for example entering Hockey would display mens and womens hockey')

	return parser


def athletes(NOC,cursor):
	#prints the athletes from a specific NOC
	try:
		query = 'SELECT DISTINCT athlete.name from athlete,nation,olympics WHERE athlete.id=olympics.athleteId and nation.NOC={}{}{} and nation.id=olympics.nationID;'.format("'",NOC,"'")
		cursor.execute(query)
	except Exception as e:
		print(e)
		exit()
	print('===== Athletes from %s ====='% NOC) 
	for row in cursor:
		print(row[0])
	print()
	exit()

def leaders(cursor):
	#prints the leaders from all NOCs
	try:
		# Query is the SQL quer'
		query = "SELECT COUNT(olympics.medal='Gold'), nation.NOC FROM olympics, nation WHERE olympics.nationID=nation.id  GROUP BY nation.NOC ORDER BY COUNT(olympics.medal='Gold') DESC;" 
		cursor.execute(query)
	except Exception as e:
		print(e)
		exit()
	print('===== Gold Meadal Board =====')
	for row in cursor:
		print(row[0], row[1])
	print()
	exit()

def events(sport, cursor):
	#shows the events from a specified sport
	try:
		query = 'SELECT DISTINCT events.event FROM events WHERE events.sport={}{}{};'.format("'",sport,"'")
		cursor.execute(query)
	except Exception as e:
		print(e)
		exit()
	print('===== Events in %s ====='% sport) 
	for row in cursor:
		print(row[0])
	print()
	exit()



def main():
	from config import password
	from config import database
	from config import user
	# Connect to the database
	try:
		connection = psycopg2.connect(database=database, user=user, password=password)
		cursor = connection.cursor()
	except Exception as e:
		print(e)
		exit()
	args=parseArgs()
	parsedArgs=args.parse_args()
	if parsedArgs.athletes !=None: #runts the athletes from NOC
		if len(parsedArgs.athletes)==1:
			athletes(parsedArgs.athletes[0],cursor)
		else:
			print('Please input exactly 1 NOC')
			args.print_help()
	if parsedArgs.events !=None: #runs the events from a sport
		if len(parsedArgs.events)==1:
			events(parsedArgs.events[0],cursor)
		else:
			print('Please input exactly 1 valid Sport')
			args.print_help()
	if parsedArgs.leaders: #shows the gold medal leaderboar
		leaders(cursor)
	exit()


if __name__ == '__main__':
	main()


