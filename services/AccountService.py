import datetime
from repositories.interfaces.IRepository import IRepository
from models.Account import Account
from models.NormalAccount import NormalAccount
from models.PopularAccount import PopularAccount
from models.CompanyAccount import CompanyAccount
from models.User import User

class AccountService:
    def __init__(self, account_repository: IRepository):
        self.account_repository = account_repository

    def register(self, user: User, account_type: str) -> Account:
        account_list = self.account_repository.list()
        if any(account.user.id == user.id for account in account_list):
            raise ValueError("User already registered") 

        if account_type == Account.NORMAL:
            account = NormalAccount(user)
        elif account_type == Account.POPULAR:
            account = PopularAccount(user)
        elif account_type == Account.COMPANY:
            account = CompanyAccount(user)
        else:
            raise ValueError("Unknown account type")       

        return self.account_repository.add(account)

    def follow(self, account: Account, follower: Account):
        if account.state == Account.STATE_SUSPENDED:
            print(f"Account {account.id} is suspended and cannot follow other accounts.")
            return

        if account.can_follow(follower):
            if follower not in account.following:
                account.follow(follower)
                print(f"Account {account.id} followed account {follower.id}.")
            else:
                print(f"Account {account.id} already follows account {follower.id}.")
        else:
            print(f"Account {account.id} cannot follow account {follower.id} due to type restrictions.")

    def unfollow(self, account: Account, follower: Account):
        if account.state == Account.STATE_SUSPENDED:
            print(f"Account {account.id} is suspended and cannot follow other accounts.")
            return

        if follower in account.following:
            account.unfollow(follower)
            print(f"Account {account.id} unfollowed account {follower.id}.")
        else:
            print(f"Account {account.id} does not follows account {follower.id}.")

    def get_all_accounts(self):
        return self.account_repository.list()