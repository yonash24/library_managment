import LibraryExceptions
from LibraryExceptions import LimitExceededError

#creating the class book that reprasent books
class Book:

    #book constructor
    def __init__(self, title, author, isbn,available_amount):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = None
        self.available_amount = available_amount
        self.how_borrow = None


    #check if book is available
    def available_book(self):
        if self.available_amount > 0:
           self.is_available = True
        else:
           self.is_available = False

        return self.is_available

    #updat borrowed book
    def borrow(self,name):
        if self.available_book():
            self.available_amount -= 1
            self.how_borrow = name
        else:
            raise LimitExceededError("book is not availbale at the moment");

    #update the return of the book
    def return_book(self,book):
        self.book.is_available = True
        self.book.available_amount += 1


#creating the class member that reprasent a member at the library
class Member:

    #member constructor
    def __init__(self, fname, lname, member_id, borrow_limit, borrowed_book):
        self.fname = fname
        self.lname = lname
        self.member_id = member_id
        self.borrow_limit = borrow_limit
        self.borrowed_book = borrowed_book

    #update if a member borrowed book
    def borrow_book(self, book):
        if self.borrowed_book <= self.borrow_limit:
            self.borrowed_book = self.borrowed_book+1
            book.how_borrow = self.member_id
        else:
            raise LimitExceededError("cannot borrow book until the returning of the books that he have")
            return


    #update that member has returned the book
    def return_book(self, book):
        self.borrowed_book = self.borrowed_book-1


"""
creating the class student that represent member at tghe library
that is a student
"""
class Student(Member):

    #student constructor
    def __init__(self, fname, lname, member_id, borrow_limit, borrowed_book):
        super().__init__(fname,lname,member_id,borrow_limit,borrowed_book)
        self.borrow_limit = 2
        self.position = "student"

"""
creating the class student that represent member at tghe library
that is in the faculty 
"""

#faculty member constructor
class FacultyMember(Member):
    def __init__(self, fname, lname, member_id, borrow_limit, borrowed_book):
        super().__init__(fname,lname,member_id,borrow_limit,borrowed_book)
        self.borrow_limit = 5
        self.position = "faculty member"


#creating the class transcript
class Transaction:

    #transcrupt constructor
    def __init__(self, member, book, borrowed_date, return_date):
        self.member = member
        self.book = book
        self.borrowed_date = borrowed_date
        self.return_date = return_date


    #update in the system the proccess of borrowing book
    def proccess_borrow(self,member,book):
        book.borrow()
        self.member.borrow_book(book)

    #update in the system the proccess of returnnig a book
    def proccess_return(self,member,book):
        book.return_book()
        self.member.return_book(book)

