from repositories.InMemoryRepository import InMemoryRepository
from models.Entity import Entity

if __name__ == "__main__":
    menu = Menu("Seleccione opción:")

    # Submenú de Ver la pizarra
    menuVerPizarra = Menu("Ver la pizarra")
    menuVerPizarra.opcion(0, 'Volver', menuVerPizarra.salir, False)
    menuVerPizarra.opcion('i', 'Realizar acción Me Gusta sobre una publicación', lambda: True)
    menuVerPizarra.opcion('ii', 'Realizar acción Republicar sobre una publicación', lambda: True)

    # Submenú de Seleccionar una cuenta
    menuSeleccionarCuenta = Menu("Seleccionar una cuenta")
    menuSeleccionarCuenta.opcion(0, 'Volver', menuSeleccionarCuenta.salir, False)
    menuSeleccionarCuenta.opcion('a', 'Ver la pizarra', menuVerPizarra.mostrar, False)
    menuSeleccionarCuenta.opcion('b', 'Ver publicaciones realizadas', lambda: True)
    menuSeleccionarCuenta.opcion('c', 'Publicar', lambda: True)
    menuSeleccionarCuenta.opcion('d', 'Ver información de la cuenta', lambda: True)
    menuSeleccionarCuenta.opcion('e', 'Ver alcance de la cuenta', lambda: True)
    menuSeleccionarCuenta.opcion('f', 'Activar/Suspender la cuenta', lambda: True)

    # Menú principal
    menu.opcion(1, 'Listar todas las cuentas de la red', lambda: True)
    menu.opcion(2, 'Seleccionar una cuenta', menuSeleccionarCuenta.mostrar, False)
    menu.opcion(3, 'Salir', menu.salir, False)

    menu.mostrar()