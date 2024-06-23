import datetime
from typing import Callable
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
        if author.state == Account.STATE_SUSPENDED:
            raise Exception(f"Account {account.id} is suspended and cannot create post.")

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

    def get_filtered_posts(self, callback: Callable):
        return self.post_repository.filter(callback)

    def add_like(self, post: Post, account: Account):
        if account.state == Account.STATE_SUSPENDED:
            raise Exception(f"Account {account.id} is suspended and cannot add like.")

        if not post.is_likeable:
            raise Exception('Post is not likeable')
 
        post.add_like(account)
    
    def remove_like(self, post: Post, account: Account):
        if account.state == Account.STATE_SUSPENDED:
            raise Exception(f"Account {account.id} is suspended and cannot remove like.")

        if not post.is_likeable:
            raise Exception('Post is not likeable')
 
        post.remove_like(account)

    def repost(self, post: Post, account: Account):
        if not post.is_repostable:
            raise Exception('Post is not repostable')

        return self.create(account, post.content, post.is_likeable, True)

    def scoped_post_followers(self, post: Post):        
        return self.scope_followers(post.author)

    def scope_followers(self, account: Account, followers: set = None) -> set:
        if followers is None:
            followers = set()

        if account in followers:
            return followers

        followers.add(account)

        for follower in account.following:
            self.scope_followers(follower, followers)

        return followers
        