from services.AccountService import AccountService
from services.UserService import UserService
from repositories.AccountInMemoryRepository import AccountInMemoryRepository
from repositories.UserInMemoryRepository import UserInMemoryRepository
from utils.Menu import Menu


if __name__ == "__main__":        
    user_service = UserService(
        user_repository=UserInMemoryRepository()
    )
    account_service = AccountService(
        account_repository=AccountInMemoryRepository(),
        user_service=user_service
    )

    def create_custom_account():
        account_service.register(
            username='bob', 
            password='password',
            email='bob@email.com',
            fullname='Bob', 
            birth_date='30/12/1997'
        )
    def see_all_useraccounts():
        all_accounts = account_service.get_all_accounts()
        print(f"Ids de usuarios en cuentas: {[account.user.id for account in all_accounts]}")


    menu = Menu("Seleccione opción:")
    menu.opcion(1, 'Crear cuenta predefinida', create_custom_account, False)
    menu.opcion(2, 'Ver cuentas con usuarios', see_all_useraccounts)
    menu.opcion(3, 'Salir', menu.salir, False)

    menu.mostrar()