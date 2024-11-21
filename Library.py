class Book:

    def __init__(self, title, author, isbn, is_available):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = is_available

    def borrow(self):
        pass

    def return_book(self):
        pass


class Member:

    def __init__(self, fname, lname, member_id, borrow_limit, borrowed_book):
        self.fname = fname
        self.lname = lname
        self.member_id = member_id
        self.borrow_limit = borrow_limit
        self.borrowed_book = borrowed_book

    def borrow_book(self, book):
        pass

    def return_book(self, book):
        pass



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

        


