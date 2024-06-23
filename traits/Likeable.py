from abc import ABC, abstractmethod
from models.Account import Account

class Likeable(ABC):
    def __init__(self):
        self.likes = set()
        self.is_likeable = False

    def add_like(self, account: Account):
        self.likes.add(account)

    def remove_like(self, account: Account):
        self.likes.remove(account)