from abc import ABC, abstractmethod
from models.Account import Account

class Repostable(ABC):
    def __init__(self):
        self.is_repostable = False