from repositories.interfaces.IRepository import IRepository
from models.User import User

class UserService:
    def __init__(self, user_repository: IRepository):
        self.user_repository = user_repository

    def create(self, username: str, password: str, email: str, fullname: str, birth_date: str) -> User:
        user = User(
            username=username,
            password=password,
            email=email,
            fullname=fullname, 
            birth_date=birth_date
        )       

        return self.user_repository.add(user)

    def get_all_users(self):
        return self.user_repository.list()