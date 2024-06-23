from abc import ABC, abstractmethod
from models.Account import Account

class Taggeable(ABC):
    def __init__(self):
        self.tags = set()

    def add_tag(self, account: Account):
        self.tags.add(account)

    def remove_tag(self, account: Account):
        self.tags.remove(account)