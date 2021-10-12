'''Julain Bowers, Skyler Kessenich'''

import booksdatasource
import sys
import argparse

def parseArgs():
	#parses the desired args 
	parser=argparse.ArgumentParser()
	parser.add_argument('--data','-d',help='the data file to be read')
	parser.add_argument('--titles','-t',nargs='*', help='book search followed by search text')
	parser.add_argument('--authors','-a', nargs='*', help='author seach followed by search text')
	parser.add_argument('--between','-b',action='store_true',help='the between years flag will return all if no start or end flag included')
	parser.add_argument('--start','-s', type=int, help='start year for books_between_years')
	parser.add_argument('--end', '-e',type=int, help='end year for books_between_years')
	parser.add_argument('--year','-y',action='store_true',help='sorts the books by year')
	parser.add_argument('--name','-n',action='store_true',help='sorts books by title which is default')
	parser.add_argument('--usage','-u',action='store_true',help='prints usage statment')

	return parser.parse_args()

def printData(data,dataType=None):
	#prints the desired data from out CLI methods
	if dataType=='book':
		for i in data:
			print(i.title)
	else:
		for i in data:
			print('Name:'+' '+i.given_name+' '+i.surname)
			print('Books: ')
			for a in i.booksWritten:
				print(a.title+'\n')

def usage():
	#prints usage.txt
	f=open('usage.txt','r')
	contents=f.read()
	print(contents)
	f.close()


def main():
	args=parseArgs() #gets the parsed args
	if args.data==None: #if there is no data exit
		print('Need a specified data file with -d flag')
		exit() 
	else:
		if args.usage:
			#if the user used -h flag print the usage
			usage()
		bookList=booksdatasource.BooksDataSource(args.data) #initialize booksdatasource object
		#these conditional statments check for which flags to run
		if args.titles != None:
			if len(args.titles)==0:
				searchText=None
			else:
				searchText=args.titles[0]
			if args.year:
				printData(bookList.books(searchText,'year'),'book')
			else:
				printData(bookList.books(searchText),'book')
		if args.authors != None:
			if len(args.authors)==0:
				searchText=None
			else:
				searchText=args.authors[0]
			printData(bookList.authors(searchText))
		if args.between:
			if args.start != None and args.end != None:
				printData(bookList.books_between_years(args.start,args.end),'book')
			elif args.start != None:
				printData(bookList.books_between_years(args.start),'book')
			elif args.end != None:
				printData(bookList.books_between_years(args.end),'book')
			else:
				printData(bookList.books_between_years(),'book')
	exit()
		







if __name__ == '__main__':
	main()
