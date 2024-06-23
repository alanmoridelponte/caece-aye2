import datetime
from repositories.interfaces.IRepository import IRepository
from services.AccountService import AccountService
from models.Account import Account
from models.NormalAccount import NormalAccount
from models.PopularAccount import PopularAccount
from models.CompanyAccount import CompanyAccount
from models.Post import Post
from utils.Class import type_str
from utils.String import get_username_tags

class PostService:
    def __init__(self, post_repository: IRepository, account_service: AccountService):
        self.post_repository = post_repository
        self.account_service = account_service

    def create(self, author: Account, content: str, likeable: bool, repostable: bool) -> Post:        
        post_content_length = len(content)
        is_author_normal = type_str(author) == type_str(NormalAccount)

        if (is_author_normal and post_content_length > 150):
            raise Exception(f'{type_str(author)} cannot post content longer than 150 characters')
        elif (not is_author_normal and post_content_length > 300):
            raise Exception(f'{type_str(author)} cannot post content longer than 300 characters')
        
        post = Post(author, content)
        post.is_likeable = likeable
        post.is_repostable = repostable

        username_tags = get_username_tags(content)
        for account in self.account_service.get_accounts_by_usernames(username_tags):
            post.add_tag(account)

        return self.post_repository.add(post)


    def get_all_posts(self):
        return self.post_repository.list()
