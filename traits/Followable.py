from abc import ABC, abstractmethod
from models.Account import Account

class Followable(ABC):
    def __init__(self):
        self.followers = set()
        self.following = set()

    @abstractmethod
    def can_follow(self, account):
        pass

    def follow(self, account):
        if self.state == Account.STATE_SUSPENDED:
            print(f"Account {self.id} is suspended and cannot follow other accounts.")
            return

        if self.can_follow(account):
            if account not in self.following:
                self.following.add(account)
                account.followers.add(self)
                print(f"Account {self.id} followed account {account.id}.")
            else:
                print(f"Account {self.id} already follows account {account.id}.")
        else:
            print(f"Account {self.id} cannot follow account {account.id} due to type restrictions.")