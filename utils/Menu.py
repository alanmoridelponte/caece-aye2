class Menu():
    def __init__(self, titulo=''):
        """
        Inicializa el menú con un título opcional.
        """
        self.opciones = {}
        self.titulo = titulo
        self.activo = True

    def opcion(self, indice, texto='', accion=lambda: False, esperar_a_usuario=True):
        """
        Agrega una opción al menú.

        :param indice: Índice de la opción.
        :param texto: Texto que se muestra para la opción.
        :param accion: Función que se ejecuta cuando se selecciona la opción.
        :param esperar_a_usuario: Indica si se debe esperar a que el usuario presione Enter después de ejecutar la acción.
        """
        self.opciones[f'{indice}'] = {
            'texto': texto,
            'accion': accion,
            'esperar_a_usuario': esperar_a_usuario
        }

    def mostrar(self):
        """
        Muestra el menú y permite al usuario seleccionar una opción.
        """
        while self.activo:
            if self.titulo:
                print(self.titulo)
            for indice, opcion in self.opciones.items():
                print(f'{indice} - {opcion["texto"]}')
            self.__seleccionar()
        self.activo = True

    def salir(self):
        """
        Sale del menú.
        """
        self.activo = False

    def __seleccionar(self):
        """
        Solicita al usuario que seleccione una opción y ejecuta la acción correspondiente.
        """
        indice = input('> ')
        try:
            opcion = self.opciones[indice]
            print(f'\n[{opcion["texto"]}]')
            opcion['accion']()
            if opcion['esperar_a_usuario']:
                input("[Enter para continuar]")
            print()
        except KeyError:
            print("Opción no válida, por favor intente de nuevo.")
        except Exception as e:
            print(f"Error al ejecutar la opción: {e}")
