'''Julain Bowers, Skyler Kessenich'''

import booksdatasource
import sys

def books(args,bookList):
	if len(args)<=2:
		return bookList.books()
	elif args[2]=='-S':
		if args[4]=='y'
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
	f=open('usage.txt',r)
	contents=f.read()
	if function==None:
		print(contents)
	elif function=='books':
		lines=[8,20]
		for i, line in enumerate(f):
			if(i in lines):
				print(line)
	elif function=='authors':
		lines=[26,32]
		for i, line in enumerate(f):
			if(i in lines):
				print(line)
	elif function=='between':
		lines=[35,40]
		for i, line in enumerate(f):
			if(i in lines):
				print(line)
	elif function=='usage':
		lines=[47,54]
		for i, line in enumerate(f):
			if(i in lines):
				print(line)
	else:
		print(contents)

def main():
	bookList=booksdatasource.BooksDataSource("books1.csv")
	if sys.argv[1]=='-t' or '--titles':
		returnList=books(sys.argv,bookList)
	elif sys.argv[1]=='-a' or '--authors':
		returnList=authors(sys.argv,bookList)
	elif sys.argv[1]=='-b' or '--between':
		returnList=between(sys.argv,bookList)
	elif sys.argv[1]=='-u' or '--usage':
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
	for i in returnList:
		print(i)





if __name__ == '__main__':
	main()
