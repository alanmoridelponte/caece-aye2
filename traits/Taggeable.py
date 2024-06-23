from abc import ABC, abstractmethod
from models.Account import Account

class Taggeable(ABC):
    def __init__(self):
        self.tags = set()

    def addTag(self, account: Account):
        self.tags.add(account)