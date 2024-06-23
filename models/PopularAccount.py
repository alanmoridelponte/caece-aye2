from traits.Followable import Followable
from models.Account import Account
from models.User import User

class PopularAccount(Account, Followable):
    def __init__(self, user: User, id: int = None):
        super().__init__(user, id)
        Followable.__init__(self)

    def can_follow(self, account):
        return True
        
