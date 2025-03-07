import  LibraryExceptions
import LibraryModels

class libraryControllers:

    #the library structor
    def __init__(self):
        self.library_books = []
        self.library_members = []


    #Admin functionality to add books to the library
    # it would be a sorted array that sort by letter by the author name
    def add_books(self,book):
        author = book.author
        if(len(self.library_books) == 0):
            self.library_books.insert(0, book)
            return
        self.library_books.insert(0, book)
        for i in range(len(self.library_books)):
           for j in range (len(author)-1):
               if(author[j] < self.library_books[i].author[j]):
                    temp = self.library_books[j]
                    self.library_books[j] = self.library_books[j+1]
                    self.library_books[j+1] = temp
               else:
                   continue



    #Register members as StudentMember or FacultyMember
    #sort them by theire first name
    def register_member(self,member):
            author = member.member.fname
            if (len(self.library_members) == 0):
                self.library_members.insert(0, member)
                return
            self.library_members.insert(0, member)
            for i in range(len(self.library_members)):
                for j in range(len(member.fname) - 1):
                    if (member.fname[j] < self.library_members[i].member.fname[j]):
                        temp = self.library_members [j]
                        self.library_members [j] = self.library_members [j + 1]
                        self.library_members [j + 1] = temp
                    else:
                        continue

    def assign_book(self,book):
        for i in  range(len(self.library_books)):
            if book.isbn == self.library_books[i].isbn:
                book = self.library_books[i]

    #Check if the book is available and if the member's borrowing limit has reached
    def process_borrowing(self,book_name,borrowing_member):
        for i in range(len(self.library_books)):
            if(book_name == self.library_books[i].title):
                    if book_name.available_book():
                            if borrowing_member.borrow_limit == 0:
                                print("cannot borrow any more book, member in limit of books")
                            else:
                                borrowing_member.borrow_book()
                                self.library_books[i].borrow()



    # Processes the return of a book
    def process_returning(self, book_title, member):
        for book in member.borrowed_books:
            if book.title.lower() == book_title.lower():
                member.return_book(book)
                book.return_book()
                print(f"{member.fname} returned '{book.title}'")
                return
        print("This book was not borrowed by the member.")

    # Searches for a book by title, author, or ISBN and returns matching books
        results = []
    def search_book(self, query):
        results = []
        query = query.lower()
        for book in self.library_books:
            if (query in book.title.lower()) or (query in book.author.lower()) or (query in book.isbn):
                results.append(book)

        if results:
            print("Search results:")
            for book in results:
                print(f"- {book.title} by {book.author} (ISBN: {book.isbn}) - {'Available' if book.is_available else 'Not Available'}")
        else:
            print("No matching books found.")

