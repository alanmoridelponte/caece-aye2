from typing import Callable
from services.AccountService import AccountService
from services.UserService import UserService
from services.PostService import PostService
from services.FeedService import FeedService
from models.Account import Account
from models.Post import Post
from repositories.AccountInMemoryRepository import AccountInMemoryRepository
from repositories.UserInMemoryRepository import UserInMemoryRepository
from repositories.PostInMemoryRepository import PostInMemoryRepository
from utils.Menu import Menu, choose_option_bool
from utils.String import generate_post_ascii

def crear_usuarios_cuentas_y_relaciones(user_service: UserService, account_service: AccountService):
    for i in range(1, 11):
        username = f'User{i}'
        type = Account.NORMAL
        if i > 5 and i < 9:
            username = f'Pop{i-5}'
            type = Account.POPULAR
        elif i > 8:
            username = f'Empresa{i-8}'
            type = Account.COMPANY

        user = user_service.create(
            username=username, 
            password='password',
            email=f'{username}@email.com',
            fullname=username, 
            birth_date='30/12/1997'
        )

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

def empresa1_publica_texto_ext_likeable_republicable(post_service: PostService, account_service: AccountService):
    empresa1 = account_service.get_account_by_id(9)
    post_service.create(empresa1, "Hola, soy Empresa1", True, True)

def empresa1_publica_texto_ext_likeable_2(post_service: PostService, account_service: AccountService):
    empresa1 = account_service.get_account_by_id(9)
    post_service.create(empresa1, "Hola, acá de nuevo Empresa1", True, False)

def empresa2_publica_texto_ext_likeable_republicable(post_service: PostService, account_service: AccountService):
    empresa2 = account_service.get_account_by_id(10)
    post_service.create(empresa2, "Hola, soy Empresa2", True, True)

def empresa2_publica_texto_ext_republicable_2(post_service: PostService, account_service: AccountService):
    empresa2 = account_service.get_account_by_id(10)
    return post_service.create(empresa2, "Hola, acá de nuevo Empresa2", False, True)

def pop1_publica_texto_ext_likeable_republicable_con_tag_pop2(post_service: PostService, account_service: AccountService):
    pop1 = account_service.get_account_by_id(6)
    return post_service.create(pop1, "Hola, soy Pop1 amiga de @Pop2", True, True)

def pop2_republica_pop1(post_service: PostService, account_service: AccountService, post: Post):
    pop2 = account_service.get_account_by_id(7)
    post_service.repost(post, pop2)

def user2_publica_texto_peq_likeable_con_tag_user3_user4_pop1(post_service: PostService, account_service: AccountService):
    user2 = account_service.get_account_by_id(2)
    return post_service.create(user2, "Que bueno estar con @User3 y @User4 viendo a @Pop1", True, False)

def user1_user_3_y_user4_likean_post_user2(post_service: PostService, account_service: AccountService, post: Post):
    user1 = account_service.get_account_by_id(1)
    user3 = account_service.get_account_by_id(3)
    user4 = account_service.get_account_by_id(4)
    post_service.add_like(post, user1)
    post_service.add_like(post, user3)
    post_service.add_like(post, user4)

def mostrar_alcance_empresa1(post_service: PostService, account_service: AccountService):
    empresa1 = account_service.get_account_by_id(9)
    alcance = len(post_service.scope_followers(empresa1)) - 1
    print(f"se muestra el alcance de la cuenta (Empresa1): {alcance}")

def user_3_likean_post_user2(post_service: PostService, account_service: AccountService, post: Post):
    user3 = account_service.get_account_by_id(3)
    post_service.add_like(post, user3)

def pop_3_likean_post_empresa2(post_service: PostService, account_service: AccountService, post: Post):
    pop3 = account_service.get_account_by_id(8)
    try:        
        post_service.add_like(post, pop3)
    except Exception as e:
        print(e)
    
def user_5_publica_texto_ext(post_service: PostService, account_service: AccountService):
    user5 = account_service.get_account_by_id(5)
    try:  
        post_service.create(
            user5, 
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud.", 
            True, 
            False
        )
    except Exception as e:
        print(e)

def pruebas(user_service: UserService, post_service: PostService, account_service: AccountService):
    crear_usuarios_cuentas_y_relaciones(user_service, account_service)
    empresa1_publica_texto_ext_likeable_republicable(post_service, account_service)
    empresa1_publica_texto_ext_likeable_2(post_service, account_service)
    empresa2_publica_texto_ext_likeable_republicable(post_service, account_service)
    post_empresa2 = empresa2_publica_texto_ext_republicable_2(post_service, account_service)
    post_pop1 = pop1_publica_texto_ext_likeable_republicable_con_tag_pop2(post_service, account_service)
    pop2_republica_pop1(post_service, account_service, post_pop1)
    post_user2 = user2_publica_texto_peq_likeable_con_tag_user3_user4_pop1(post_service, account_service)
    user1_user_3_y_user4_likean_post_user2(post_service, account_service, post_user2)
    mostrar_alcance_empresa1(post_service, account_service)
    user_3_likean_post_user2(post_service, account_service, post_user2)
    pop_3_likean_post_empresa2(post_service, account_service, post_empresa2)
    user_5_publica_texto_ext(post_service, account_service)

def listar_cuentas_de_la_red(account_service: AccountService):
    def accounts_list():
        for account in account_service.get_all_accounts():
            print('{:<2} - {}'.format(account.id, account.user.username))
    return accounts_list

def seleccionar_cuenta(account_service: AccountService, instance, action: Callable):
    def accounts_select():
        account_id = int(input('Seleccione id de cuenta: '))
        if any(account.id == account_id for account in account_service.get_all_accounts()):
            instance.account_selected = account_service.get_account_by_id(account_id)
            action()
        else:
            print('No existe el id de cuenta...')             
        
    return accounts_select

def ver_pizzarra(feed_service: FeedService, instance, action: Callable):
    def see_feed():
        for post in feed_service.get_feed(instance.account_selected):
            print(
                generate_post_ascii(
                    f"Post ID: {post.id} - {post.author.user.username} dijo:", 
                    post.content, 
                    len(post.likes)
                )
            )
        action()

    return see_feed

def ver_pizarra_dar_like(post_service: PostService, instance):
    def add_like():
        post_id = int(input('Seleccione id de post: '))
        if any(post.id == post_id for post in post_service.get_all_posts()):
            post_selected = post_service.get_post_by_id(post_id)
            post_service.add_like(post_selected, instance.account_selected)
        else:
            print('No existe el id de post...')

    return add_like

def ver_pizarra_repostear(post_service: PostService, instance):
    def add_like():
        post_id = int(input('Seleccione id de post: '))
        if any(post.id == post_id for post in post_service.get_all_posts()):
            post_selected = post_service.get_post_by_id(post_id)
            post_service.repost(post_selected, instance.account_selected)
        else:
            print('No existe el id de post...')

    return add_like

def ver_pizarra_propia(feed_service: FeedService, instance):
    def get_own_feed():
        for post in feed_service.get_own_feed(instance.account_selected):
            print(
                generate_post_ascii(
                    f"Post ID: {post.id} - {post.author.user.username} dijo:", 
                    post.content, 
                    len(post.likes)
                )
            )
    return get_own_feed

def publicar_desde_menu(user_service: UserService, account_service: AccountService, post_service: PostService, instance):
    post_dato = input("Ingrese el mensaje que quiere enviar: ")
    repostable = choose_option_bool('¿Quiere que el post sea reposteable?')
    likeable = choose_option_bool('¿Quiere que el post sea likeable?')

    post_service.create(instance.account_selected, post_dato, repostable, likeable)

def ver_informacion_cuenta(account_service: AccountService, instance):
    print("User:", instance.account_selected.user.username)
    print("Fecha de crecion:", instance.account_selected.create_date)
    print("Estado de la cuenta:", instance.account_selected.state)

def ver_alcance_cuenta(user_service: UserService, account_service: AccountService, post_service: PostService, instance):
    account_selected = instance.account_selected
    alcance = len(post_service.scope_followers(account_selected)) - 1
    print(f"se muestra el alcance de la cuenta {(account_selected.user.username)}: {alcance}")

def activar_o_suspender_cuenta(user_service: UserService, account_service: AccountService, instance):
    account_selected = instance.account_selected
    print(f"El estado de la cuenta {account_selected.user.username} actual es: {account_selected.state}")
    should_toogle_status = choose_option_bool('¿Esta seguro que desea cambiar el estado de la cuenta?')
    if should_toogle_status:
        account_service.toggle_account_status(account_selected)
        print(f"El estado de la cuenta {account_selected.user.username} actual ahora es: {account_selected.state}")
