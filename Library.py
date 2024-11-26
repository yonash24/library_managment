import LibraryExceptions
from LibraryExceptions import LimitExceededError


class Library:
    pass


class Book:

    def __init__(self, title, author, isbn, is_available, how_borrow):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = is_available
        self.how_borrow = None


    def available_book(self,book):
        if book.is_available() == True:
            return False
        else:
            return True

    def borrow(self,book):
        if book.available_book():
            book.is_available = False
        else:
            raise LimitExceededError("book is not availbale at the moment");

    def return_book(self,book):
        book.is_available = True



class Member:

    def __init__(self, fname, lname, member_id, borrow_limit, borrowed_book):
        self.fname = fname
        self.lname = lname
        self.member_id = member_id
        self.borrow_limit = borrow_limit
        self.borrowed_book = borrowed_book

    def borrow_book(self, book):
        if self.borrowed_book <= self.borrow_limit:
            self.borrowed_book = self.borrowed_book+1
            book.how_borrow = self.member_id
        else:
            raise LimitExceededError("cannot borrow book until the returning of the books that he have")
            return



    def return_book(self, book):
        self.borrowed_book = self.borrowed_book-1



class Student(Member):

    def __init__(self, fname, lname, member_id, borrow_limit, borrowed_book):
        super().__init__(fname,lname,member_id,borrow_limit,borrowed_book)
        self.borrow_limit = 2



class FacultyMember(Member):
    def __init__(self, fname, lname, member_id, borrow_limit, borrowed_book):
        super().__init__(fname,lname,member_id,borrow_limit,borrowed_book)
        self.borrow_limit = 5




class Transaction:

    def __init__(self, member, book, borrowed_date, return_date):
        self.member = member
        self.book = book
        self.borrowed_date = borrowed_date
        self.return_date = return_date


    def proccess_borrow(self,member,book):
        book.borrow()
        member.borrow_book(book)


    def proccess_return(self,member,book):
        book.return_book()
        member.return_book(book)

