class BookUnavailableError(Exception):

    def __init__(self,msg):
        self.msg = msg
        super.__init__(msg)



class LimitExceededError(Exception):

    def __init__(self,msg):
        self.msg = msg
        super.__init__(msg)