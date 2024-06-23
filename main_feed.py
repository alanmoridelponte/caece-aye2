from services.AccountService import AccountService
from services.UserService import UserService
from services.PostService import PostService
from services.FeedService import FeedService
from models.Account import Account
from repositories.AccountInMemoryRepository import AccountInMemoryRepository
from repositories.UserInMemoryRepository import UserInMemoryRepository
from repositories.PostInMemoryRepository import PostInMemoryRepository
from utils.Menu import Menu
from utils.String import generate_post_ascii


if __name__ == "__main__":        
    user_service = UserService(
        user_repository=UserInMemoryRepository()
    )
    account_service = AccountService(
        account_repository=AccountInMemoryRepository()
    )
    post_service = PostService(
        post_repository=PostInMemoryRepository(),
        account_service=account_service
    )
    feed_service = FeedService(
        account_service=account_service,
        post_service=post_service
    )

    user1 = user_service.create(
            username='bob', 
            password='password',
            email='bob@email.com',
            fullname='Bob', 
            birth_date='30/12/1997'
    )
    acc1 = account_service.register(user1, Account.NORMAL)

    user2 = user_service.create(
            username='alice', 
            password='password',
            email='alice@email.com',
            fullname='Alice', 
            birth_date='23/05/1992'
    )
    acc2 = account_service.register(user2, Account.NORMAL)

    user3 = user_service.create(
            username='jorge', 
            password='password',
            email='jorge@email.com',
            fullname='Jorge', 
            birth_date='05/03/1955'
    )
    acc3 = account_service.register(user3, Account.NORMAL)

    account_service.follow(acc3, acc1)

    repost1 = post_service.create(acc1, 'hola @alice. @roberto @bob', False, True)
    post_service.create(acc1, 'hola 2', False, False)

    post_service.repost(repost1, acc3)
    posts = feed_service.get_feed(acc1)

    for post in posts:
        print(
            generate_post_ascii(
                f"{post.author.user.username} dijo:", 
                post.content, 
                len(post.likes)
            )
        )

