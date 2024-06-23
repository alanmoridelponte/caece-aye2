from services.AccountService import AccountService
from services.UserService import UserService
from services.PostService import PostService
from services.FeedService import FeedService
from models.Account import Account
from repositories.AccountInMemoryRepository import AccountInMemoryRepository
from repositories.UserInMemoryRepository import UserInMemoryRepository
from repositories.PostInMemoryRepository import PostInMemoryRepository
from utils.Menu import Menu
from utils.Class import type_str


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

    for i in range(1, 11):
        user = user_service.create(
            username=f'u{i}', 
            password='password',
            email=f'u{i}@email.com',
            fullname=f'u{i}', 
            birth_date='30/12/1997'
        )
        type = Account.NORMAL
        if i > 5 and i < 9:
            type = Account.POPULAR
        elif i > 8:
            type = Account.COMPANY
        account_service.register(user, type)

    accounts = account_service.get_all_accounts()

    account_service.follow(accounts[0], accounts[1])
    account_service.follow(accounts[0], accounts[7])
    account_service.follow(accounts[0], accounts[9])

    account_service.follow(accounts[1], accounts[5])
    account_service.follow(accounts[1], accounts[9])

    account_service.follow(accounts[2], accounts[3])
    account_service.follow(accounts[2], accounts[5])
    account_service.follow(accounts[2], accounts[8])

    account_service.follow(accounts[3], accounts[2])
    account_service.follow(accounts[3], accounts[4])
    account_service.follow(accounts[3], accounts[6])

    account_service.follow(accounts[4], accounts[6])
    account_service.follow(accounts[4], accounts[7])
    account_service.follow(accounts[4], accounts[8])

    account_service.follow(accounts[5], accounts[8])
    account_service.follow(accounts[5], accounts[9])

    account_service.follow(accounts[6], accounts[8])

    account_service.follow(accounts[7], accounts[5])
    account_service.follow(accounts[7], accounts[8])
    account_service.follow(accounts[7], accounts[9])
    

    def create_custom_account():
        user = user_service.create(
            username='bob', 
            password='password',
            email='bob@email.com',
            fullname='Bob', 
            birth_date='30/12/1997'
        )
        account_service.register(user, Account.NORMAL)

    def see_all_useraccounts():
        all_accounts = account_service.get_all_accounts()
        print(f"Ids de usuarios en cuentas: {[f'id: {account.user.id} {type_str(account)}' for account in all_accounts]}")

    def make_follower():
        all_accounts = account_service.get_all_accounts()
        account_service.follow(all_accounts[0], all_accounts[1])
        print(f"{account_service.get_all_accounts()[1].followers}")

    def test_post():
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

        post_service.create(acc1, 'hola @alice. @roberto @bob', False, False)
        posts = post_service.get_all_posts()

        for post in posts:
            print(f"Post {[ post.author.user.fullname + ': ' + post.content for post in posts ]}")
            for tag in post.tags:
                print(f"tag: {str(tag.user.fullname)}")

    menu = Menu("Seleccione opción:")
    menu.opcion(1, 'Crear cuenta predefinida', create_custom_account, False)
    menu.opcion(2, 'prueba seguir', make_follower, False)
    menu.opcion(3, 'Ver cuentas con usuarios', see_all_useraccounts)
    menu.opcion(4, 'posts', test_post, False)
    menu.opcion(5, 'Salir', menu.salir, False)

    menu.mostrar()