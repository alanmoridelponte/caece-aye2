from models.Post import Post
from repositories.InMemoryRepository import InMemoryRepository

class PostInMemoryRepository(InMemoryRepository[Post]):
    def __init__(self):
        super().__init__()

    @classmethod
    def _type(cls):
        return Post
