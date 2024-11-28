#exception that occure if the book is not available
class BookUnavailableError(Exception):

    def __init__(self,msg):
        self.msg = msg
        super.__init__(msg)


#exception that occure if the member got to his borrowing limit
class LimitExceededError(Exception):

    def __init__(self,msg):
        self.msg = msg
        super.__init__(msg)

class NotInLibraryError(Exception):

    def __init__(self,msg):
        self.msg = msg
        super.__init__(msg)