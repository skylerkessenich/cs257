'''
   booksdatasourcetest.py
   Julian Bowers, Skyler Kessenich, 24 September 2021
'''

import booksdatasource
import unittest

class BooksDataSourceTester(unittest.TestCase):
    def setUp(self):
        self.data_source = booksdatasource.BooksDataSource('books1.csv')

    def tearDown(self):
        pass

    def test_unique_author(self):
        authors = self.data_source.authors('Pratchett')
        self.assertTrue(len(authors) == 1)
        self.assertTrue(authors[0] == Author('Pratchett', 'Terry'))
    def testAuthorBasics(self):
      #tests the basics of the author class
        authors= self.data_source.authors('Pratchett')
        self.assertTrue(authors[0].surname=='Pratchett')
        self.assertTrue(authors[0].given_name=='Terry')
        self.assertTrue(authors[0].birth_year==1948)
    def test_unique_book(self):
        book = self.data_source.books('Good Omens')
        self.assertTrue(len(book) == 1)
        self.assertTrue(book[0] == Book('Good Omens'))
    def testBookBasics(self):
      #tests the bascis of the book class
        book= self.data_source.books("Sense and Sensibility")
        self.assertTrue(len(book)==1)
        self.assertTrue(book[0].title=="Sense and Sensibility")
        self.assertTrue(book[0].publication_year==1813)
        print('here')
        self.assertTrue(book[0].author[0]==Author ('Austen','Jane'))
    def testDifferentAuthorSameName(self):
        #Checks to see if both authors with the same name are returned by author
        authors= self.data_source.authors('bronte')
        self.assertTrue(len(authors)==2)
        self.assertTrue(authors[0].given_name=='Charlotte')
        self.assertTrue(authors[1].given_name=='Emily')
    def testTwoAuthorsOneBook(self):
        #checks to see if both athors are in Good Omens
        book = self.data_source.books('Good Omens')
        self.assertTrue(book[0].author[0].surname=='Gaiman')
    def testGetAllBooks(self):
        #should return all the books
        book=self.data_source.books()
        self.assertTrue(len(book)==41)
    def testgetAllER(self):
      #gets all books with an 'er'
        books=self.data_source.books('er')
        self.assertTrue(len(books)==10)
    def testTitleSort(self):
        books=self.data_source.books('sex','title')
        self.assertTrue(books[0].title=='Boys and Sex')
    def testYearSort(self):
        books=self.data_source.books('sex','year')
        self.assertTrue(books[1].title=='Boys and Sex')
    def testBetweenYears(self):
      books=self.data_source.books_between_years(2018,2020)
      self.assertTrue(len(books)==4)
      self.assertTrue(books[0].title=="There, There")
      self.assertTrue(books[0].title=="The Invisible Life of Addie LaRue")
  

    
    

    

    
    



        
        

if __name__ == '__main__':
    unittest.main()

