#!/usr/bin/env python3
'''
    booksdatasource.py
    Julian Bowers Skyler Kessenich Oct 2nd 2021
'''

import csv


class Author:
    def __init__(self, surname='', given_name='', birth_year=None, death_year=None):
        self.surname = surname
        self.given_name = given_name
        self.birth_year = birth_year
        self.death_year = death_year
        self.booksWritten = []

    def __eq__(self, other):
        ''' For simplicity, we're going to assume that no two authors have the same name. '''
        return self.surname == other.surname and self.given_name == other.given_name

class Book:
    def __init__(self, title='', publication_year=None, authors=[]):
        ''' Note that the self.authors instance variable is a list of
            references to Author objects. '''
        self.title = title
        self.publication_year = publication_year
        self.authors = authors

    def __eq__(self, other):
        ''' We're going to make the excessively simplifying assumption that
            no two books have the same title, so "same title" is the same
            thing as "same book". '''
        return self.title == other.title

class BooksDataSource:
    def __init__(self, books_csv_file_name):
        ''' 
            This __init__ method parses the specified CSV file and creates
            suitable instance variables for the BooksDataSource object containing
            a collection of Author objects and a collection of Book objects.
        '''
        file = open(books_csv_file_name)
        csvreader=csv.reader(file)
        header=next(csvreader)
        self.booksList = []
        self.authorsList=[]
        for book in csvreader:
            #read every book and parse it into the book and author objects after this function, we should have a list of books and authors
            counter=0
            author=book[2].split('and')
            authorsLocal=[]
            while len(author)>counter: #extracts info about the author
                authorI=author[counter].split('(')
                authorName=authorI[0].strip()
                authorName=authorName.split(' ',1)
                givenName=authorName[0]
                surname=authorName[1]
                lifeSpan=authorI[1].split('-')
                birthYear=int(lifeSpan[0])
                deathYear=lifeSpan[1].strip(')').strip()
                if deathYear=='':
                    deathYear==None
                else:
                    deathYear=int(deathYear)
                newAuthor=Author(surname,givenName,birthYear,deathYear)
                if newAuthor not in self.authorsList: #adds newAuthor to list of all authors
                    self.authorsList.append(newAuthor)
                authorsLocal.append(newAuthor) #adds newAuthor to list of authors for this book
                counter+=1
            newBook=Book(book[0],int(book[1]),authorsLocal)
            for a in authorsLocal:
                a.booksWritten.append(newBook)
            self.booksList.append(newBook)

       
        pass

    def authors(self, search_text=None):
        ''' Returns a list of all the Author objects in this data source whose names contain
            (case-insensitively) the search text. If search_text is None, then this method
            returns all of the Author objects. In either case, the returned list is sorted
            by surname, breaking ties using given name (e.g. Ann Brontë comes before Charlotte Brontë).
        '''
        authorsReturned=[]
        if search_text==None:
            return self.authorsList
        search_text=search_text.lower()
        for author in self.authorsList:
            fullName=author.given_name+author.surname
            if search_text in fullName.lower():
                authorsReturned.append(author)
        authorsReturned.sort(key=lambda x:(x.surname,x.given_name),reverse=False)
        return authorsReturned

    def books(self, search_text=None, sort_by='title'):
        ''' Returns a list of all the Book objects in this data source whose
            titles contain (case-insensitively) search_text. If search_text is None,
            then this method returns all of the books objects.

            The list of books is sorted in an order depending on the sort_by parameter:

                'year' -- sorts by publication_year, breaking ties with (case-insenstive) title
                'title' -- sorts by (case-insensitive) title, breaking ties with publication_year
                default -- same as 'title' (that is, if sort_by is anything other than 'year'
                            or 'title', just do the same thing you would do for 'title')
        '''

        booksReturned=[]
        if search_text==None:
            booksReturned=self.booksList
        else:
            search_text=search_text.lower()
            for book in self.booksList:
                if search_text in book.title.lower():
                    booksReturned.append(book)
        if sort_by=='year':
            booksReturned.sort(key=lambda x:x.publication_year,reverse=False)     
        else:
            booksReturned.sort(key=lambda x:x.title,reverse=False)
        return booksReturned

    def books_between_years(self, start_year=None, end_year=None):
        ''' Returns a list of all the Book objects in this data source whose publication
            years are between start_year and end_year, inclusive. The list is sorted
            by publication year, breaking ties by title (e.g. Neverwhere 1996 should
            come before Thief of Time 1996).

            If start_year is None, then any book published before or during end_year
            should be included. If end_year is None, then any book published after or
            during start_year should be included. If both are None, then all books
            should be included.
        '''
        booksReturned=[]
        if start_year==None and end_year==None:
            booksReturned=self.booksList
        elif start_year==None:
            end_year=int(end_year)
            for book in self.booksList:
                if book.publication_year<=end_year:
                    booksReturned.append(book)
        elif end_year==None:
            start_year=int(start_year)
            for book in self.booksList:
                if book.publication_year>=start_year:
                    booksReturned.append(book)
        else:
            start_year=int(start_year)
            end_year=int(end_year)
            for book in self.booksList:
                if book.publication_year>=start_year and book.publication_year<=end_year:
                    booksReturned.append(book)

        booksReturned.sort(key=lambda x:x.publication_year, reverse=False)
        return booksReturned


