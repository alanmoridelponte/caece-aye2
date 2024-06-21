from models.Account import Account
from repositories.InMemoryRepository import InMemoryRepository

class AccountInMemoryRepository(InMemoryRepository[Account]):
    def __init__(self):
        super().__init__()

    @classmethod
    def _type(cls):
        return Account
