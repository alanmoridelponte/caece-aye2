import datetime
from repositories.interfaces.IRepository import IRepository
from models.Account import Account
from models.NormalAccount import NormalAccount
from models.PopularAccount import PopularAccount
from models.CompanyAccount import CompanyAccount
from models.Post import Post
from utils.Class import type_str

class PostService:
    def __init__(self, post_repository: IRepository):
        self.post_repository = post_repository

    def create(self, author: Account, content: str, tags: set()) -> Post:
        # TODO logica de negocio para crear post
        post = Post(author, content)
        for tag in tags:
            post.add_tag(tag)
            
        return self.post_repository.add(post)


    def get_all_posts(self):
        return self.post_repository.list()
