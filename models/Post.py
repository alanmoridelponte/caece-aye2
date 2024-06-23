from utils.Date import get_current_timestamp
from models.Entity import Entity
from models.Account import Account

class Post(Entity):
    def __init__(self, author: Account, content: str, id: int = None):
        super().__init__(id)
        self.author = author
        self.content = content
        self.create_date = get_current_timestamp()
        
