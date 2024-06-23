from traits.Followable import Followable
from models.Account import Account
from models.CompanyAccount import CompanyAccount
from models.User import User

class NormalAccount(Account, Followable):
    def __init__(self, user: User, id: int = None):
        super().__init__(user, id)
        Followable.__init__(self)

    def can_follow(self, account: Account):
        return True
        
