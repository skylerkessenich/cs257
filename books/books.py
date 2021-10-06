'''Julain Bowers, Skyler Kessenich'''

import booksdatasource
import sys

def books(args,bookList):
	print('hlll')
	if len(args)<=2:
		return bookList.books()
	elif args[2]=='-S':
		if len(args)<5:
			return bookList.books(args[3])
		elif args[4]=='y':
			return bookList.books(args[3],'years')
		else:
			return bookList.books(args[3])

	else:
		print('Invalid Args')
		usage('books')
		return None


def authors(args,bookList):
	if len(args)<=2:
		return bookList.authors()
	elif args[2]=='-S':
		return bookList.authors(args[3])
	else:
		print('Invalid Args')
		usage('authors')
		return None

def between(args,bookList):
	if len(args)<=2:
		return bookList.books_between_years()
	elif len(args)<=4:
		if args[2]=='-s':
			return bookList.books_between_years(args[3],None)
		elif args[2]=='-e':
			bookList.books_between_years(None,args[3])
		else:
			print('Invalid Args')
			usage('between')
			return None
	elif args[2]=='-s' and args[4]=='-e':
		return bookList.books_between_years(args[3], args[5])
	else:
		print('Invalid Args')
		usage('between')
		return None


def usage(function=None):
	f=open('usage.txt','r')
	contents=f.readlines()
	if function==None:
		print(contents)
	elif function=='books':
		lines=[8,9,10,11,12,13,14,15,16,17,18,19,20]
		for i, line in enumerate(contents):
			if(i in lines):
				print(line)
	elif function=='authors':
		lines=[26,27,28,29,30,31,32]
		for i, line in enumerate(contents):
			if(i in lines):
				print(line)
	elif function=='between':
		lines=[35,36,37,38,39,40]
		for i, line in enumerate(contents):
			if(i in lines):
				print(line)
	elif function=='usage':
		lines=[47,48,49,50,51,52,53,54]
		for i, line in enumerate(contents):
			if(i in lines):
				print(line)
	else:
		print(contents)
	f.close()


def main():
	bookList=booksdatasource.BooksDataSource("books1.csv")
	print(sys.argv[1])
	if sys.argv[1]=='-t' or sys.argv[1]=='--titles':
		returnList=books(sys.argv,bookList)
	elif sys.argv[1]=='-a' or sys.argv[1]=='--authors':
		
		returnList=authors(sys.argv,bookList)
	elif sys.argv[1]=='-b' or sys.argv[1]=='--between':
		returnList=between(sys.argv,bookList)
	elif sys.argv[1]=='-u' or sys.argv[1]=='--usage':
		if sys.argv[2]=='-t' or '--titles':
			usage('books')
		elif sys.argv[2]=='-a' or '--authors':
			usage('authors')
		elif sys.argv[2]=='-b' or '--between':
			usage('between')
		returnList=None
	else:
		usage()
		returnList=None
	if returnList !=None:
		for i in returnList:
			if type(i)==booksdatasource.Book:
				print(i.title)
			else:
				print(i.given_name+' '+i.surname)





if __name__ == '__main__':
	main()
