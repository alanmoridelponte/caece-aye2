from types import SimpleNamespace
from services.AccountService import AccountService
from services.UserService import UserService
from services.PostService import PostService
from services.FeedService import FeedService
from models.Account import Account
from models.User import User
from repositories.AccountInMemoryRepository import AccountInMemoryRepository
from repositories.UserInMemoryRepository import UserInMemoryRepository
from repositories.PostInMemoryRepository import PostInMemoryRepository
from utils.Menu import Menu
from main_metodos import *
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
    
    pruebas(user_service, post_service, account_service)

    ns = SimpleNamespace()
    ns.account_selected = None

    menu = Menu("Seleccione opción:")

    # Submenú de Ver la pizarra
    menuVerPizarra = Menu("Ver la pizarra")
    menuVerPizarra.opcion(0, 'Volver', menuVerPizarra.salir, False)
    menuVerPizarra.opcion(1, 'Realizar acción Me Gusta sobre una publicación', ver_pizarra_dar_like(post_service, ns))
    menuVerPizarra.opcion(2, 'Realizar acción Republicar sobre una publicación', ver_pizarra_repostear(post_service, ns))

    # Submenú de Seleccionar una cuenta
    menuSeleccionarCuenta = Menu("Seleccionar una cuenta")
    menuSeleccionarCuenta.opcion(0, 'Volver', menuSeleccionarCuenta.salir, False)
    menuSeleccionarCuenta.opcion(1, 'Ver la pizarra', ver_pizzarra(feed_service, ns, menuVerPizarra.mostrar), True)
    menuSeleccionarCuenta.opcion(2, 'Ver publicaciones realizadas', ver_pizarra_propia(feed_service, ns), True)
    menuSeleccionarCuenta.opcion(3, 'Publicar', lambda: publicar_desde_menu(user_service, account_service, post_service, ns), True)
    menuSeleccionarCuenta.opcion(4, 'Ver información de la cuenta', lambda: ver_informacion_cuenta(account_service, ns), True)
    menuSeleccionarCuenta.opcion(5, 'Ver alcance de la cuenta', lambda: ver_alcance_cuenta(user_service, account_service, post_service, ns), True)
    menuSeleccionarCuenta.opcion(6, 'Activar/Suspender la cuenta', lambda: activar_o_suspender_cuenta(user_service, account_service, ns), True)

    # Menú principal
    menu.opcion(1, 'Listar todas las cuentas de la red', listar_cuentas_de_la_red(account_service))
    menu.opcion(2, 'Seleccionar una cuenta', seleccionar_cuenta(account_service, ns, menuSeleccionarCuenta.mostrar), False)
    menu.opcion(3, 'Salir', menu.salir, False)

    menu.mostrar()