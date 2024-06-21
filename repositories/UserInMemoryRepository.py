from models.User import User
from repositories.InMemoryRepository import InMemoryRepository

class UserInMemoryRepository(InMemoryRepository[User]):
    def __init__(self):
        super().__init__()

    @classmethod
    def _type(cls):
        return User
