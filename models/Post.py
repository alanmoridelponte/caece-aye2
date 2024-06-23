from utils.Date import get_current_timestamp
from models.Entity import Entity
from models.Account import Account
from traits.Taggeable import Taggeable

class Post(Entity, Taggeable):
    def __init__(self, author: Account, content: str, id: int = None):
        super().__init__(id)
        Taggeable.__init__(self)
        self.author = author
        self.content = content
        self.create_date = get_current_timestamp()
        
