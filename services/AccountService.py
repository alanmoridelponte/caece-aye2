import datetime
from repositories.interfaces.IRepository import IRepository
from services.UserService import UserService
from models.Account import Account
from models.User import User

class AccountService:
    def __init__(self, account_repository: IRepository, user_service: UserService):
        self.account_repository = account_repository
        self.user_service = user_service

    def register(self, username: str, password: str, email: str, fullname: str, birth_date: str) -> Account:
        user = self.user_service.create(
            username=username,
            password=password,
            email=email,
            fullname=fullname, 
            birth_date=birth_date
        )

        account = Account(
            user=user,
            create_date=datetime.datetime.now().replace(microsecond=0).isoformat(),
            type=Account.TYPE_NORMAL,
            status=Account.STATUS_OPEN
        )

        return self.account_repository.add(account)

    def get_all_accounts(self):
        return self.account_repository.list()