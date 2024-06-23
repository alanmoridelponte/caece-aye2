from abc import ABC, abstractmethod
from models.Account import Account

class Followable(ABC):
    def __init__(self):
        self.followers = set()
        self.following = set()

    @abstractmethod
    def can_follow(self, account: Account):
        pass

    def follow(self, account: Account):
        self.following.add(account)
        account.followers.add(self)

    def unfollow(self, account: Account):
        self.following.remove(account)
        account.followers.remove(self)