from services.AccountService import AccountService
from services.PostService import PostService
from models.Account import Account

class FeedService:
    def __init__(self, account_service: AccountService, post_service: PostService):
        self.account_service = account_service
        self.post_service = post_service

    def get_feed(self, account: Account):
        def condition(post):
            is_author = post.author == account
            is_in_post_tags = account in post.tags
            is_author_followed = post.author in account.following

            return is_author or is_in_post_tags or is_author_followed

        return self.post_service.get_filtered_posts(condition)

    def get_own_feed(self, account: Account):
        def condition(post):
            return post.author == account

        return self.post_service.get_filtered_posts(condition)