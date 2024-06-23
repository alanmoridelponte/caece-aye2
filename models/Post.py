from models.Entity import Entity
from models.User import User

class Post(Entity):
    def __init__(self, author: User, create_date: str, content: str, status: str, id: int = None):
        super().__init__(id)
        self.author = author
        self.create_date = create_date
        self.content = content
        
