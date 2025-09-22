"""Es la clase principal que correrá el programa en el módulo main.
tiene como atributo un objeto de la clase biblioteca
define metodos para correr el programa"""

from enum import Enum
from biblioteca import Biblioteca
from tipo_item import TipoItem
from autor import Autor
from item_biblioteca import ItemBiblioteca
from mostrar_menu import muetra_el_menu, mostrar_submenu_busqueda, mostrar_submenu_prestamos


class Opciones(Enum):
    VOLVER_MENU = (0,)   # un solo valor basta

    AGREGAR = (1,)
    AGREGAR_OTRO = (1,1)

    BUSCAR = (2,)
    BUSCAR_AUTOR = (2,1)
    BUSCAR_TITULO = (2,2)
    BUSCAR_TIPO = (2,3)

    PRESTAR_DEVOLVER = (3,)
    PRESTAR = (3,1)
    DEVOLVER = (3,2)

    SALIR = (4,)



class BibliotecaManager:
    def __init__(self, biblioteca: Biblioteca):
        self.biblioteca = biblioteca



    def opciones_seleccion(self):
        """Pedir input y devolver un valor Opciones"""
        # aquí habría que mapear input -> Enum
        opcion = input("👉 Elige una opción: ")
        try:
            return Opciones(int(opcion))  # versión simplificada
        except ValueError:
            print("⚠️ Opción no válida")
            return Opciones.VOLVER_MENU

    def opciones_del_menu(self):
        """Usa opciones_seleccion() y gestiona según tupla"""

        dispatcher = {
            # Menú principal
            Opciones.VOLVER_MENU: muetra_el_menu,
            Opciones.AGREGAR: muetra_el_menu,
            Opciones.BUSCAR: mostrar_submenu_busqueda,
            Opciones.PRESTAR_DEVOLVER: mostrar_submenu_prestamos,
            Opciones.SALIR: exit,

            # Submenús de AGREGAR
            Opciones.AGREGAR_OTRO: muetra_el_menu,  # tras agregar vuelve al principal

            # Submenús de BUSCAR
            Opciones.BUSCAR_AUTOR: mostrar_submenu_busqueda,
            Opciones.BUSCAR_TITULO: mostrar_submenu_busqueda,
            Opciones.BUSCAR_TIPO: mostrar_submenu_busqueda,

            # Submenús de PRESTAR/DEVOLVER
            Opciones.PRESTAR: mostrar_submenu_prestamos,
            Opciones.DEVOLVER: mostrar_submenu_prestamos,
        }
        # Preguntar opción
        var = self.opciones_seleccion()

        # Buscar handler en el diccionario
        handler = dispatcher.get(var)

        if handler:
            handler()  # ejecuta la función correspondiente
        else:
            print("⚠️ Error: opción no reconocida")

    def crear_item_desde_input(self):
        """usado por opciones"""
        try:
            codigo = input("Código: ").strip()
            titulo = input("Título: ").strip()

            # pedir tipo (ej: 'DIGITAL', 'FISICO', etc.)
            tipo_str = input("Tipo de item (ej: DIGITAL, FISICO): ").strip().upper()
            tipo = TipoItem[tipo_str]  # lanza KeyError si el usuario escribe mal

            # pedir autores separados por coma
            print("Autores (formato: Nombre|Apellidos|Nacionalidad, separados por coma)")
            autores_str = input("Ejemplo: Miguel|de Cervantes|España, Isaac|Asimov|EEUU\n> ").strip()

            autores = []
            if autores_str:
                for datos in autores_str.split(","):
                    partes = [p.strip() for p in datos.split("|")]
                    if len(partes) == 3:
                        nombre, apellidos, nacionalidad = partes
                        autores.append(Autor(nombre, apellidos, nacionalidad))
                    else:
                        raise ValueError(
                            f"Formato de autor inválido: '{datos}'. "
                            "Usa Nombre|Apellidos|Nacionalidad"
                        )

            # crear y devolver el objeto ItemBiblioteca
            return ItemBiblioteca(codigo, titulo, tipo, autores)

        except Exception as e:
            print(f"Error al crear el ítem: {e}")
            return None

    # opcion agregar libro
    def gestionar_entrada(self):
        """genera un item que es agregado a la biblioteca"""
        #   crear objeto libro segun input
        item = self.crear_item_desde_input()
        self.biblioteca.agregar(item)

    def opcion_buscar(self, clave):
        """llama a la función de las subclases y
        muestra el resultado en pantalla"""
        var = self.biblioteca.busqueda(clave)
        """esto hay que definirlo bien"""
        print(var)

    def opcion_prestar(self, clave):
        self.biblioteca.prestar_devolver(clave, "prestar")

    def opcion_devolver(self, clave):
        self.biblioteca.prestar_devolver(clave, "devolver")

    # RUUN!!!!





    """
    | Estado actual            | Entrada usuario | Nuevo estado             | Comentario                    |
| ------------------------ | --------------- | ------------------------ | ----------------------------- |
| `(0,)` VOLVER\_MENU      | `1`             | `(1,)` AGREGAR           | Ir al menú de agregar         |
|                          | `2`             | `(2,)` BUSCAR            | Ir al submenú de búsqueda     |
|                          | `3`             | `(3,)` PRESTAR\_DEVOLVER | Ir al submenú de préstamos    |
|                          | `4`             | `(4,)` SALIR             | Salir del programa            |
|                          | otro            | `(0,)` VOLVER\_MENU      | Entrada inválida              |
| `(1,)` AGREGAR           | `1`             | `(1,1)` AGREGAR\_OTRO    | Subopción: agregar otro libro |
|                          | `0`             | `(0,)` VOLVER\_MENU      | Volver al menú principal      |
|                          | otro            | `(1,)` AGREGAR           | Entrada inválida → permanece  |
| `(2,)` BUSCAR            | `1`             | `(2,1)` BUSCAR\_AUTOR    | Buscar por autor              |
|                          | `2`             | `(2,2)` BUSCAR\_TITULO   | Buscar por título             |
|                          | `3`             | `(2,3)` BUSCAR\_TIPO     | Buscar por tipo               |
|                          | `0`             | `(0,)` VOLVER\_MENU      | Volver al menú principal      |
|                          | otro            | `(2,)` BUSCAR            | Entrada inválida → permanece  |
| `(3,)` PRESTAR\_DEVOLVER | `1`             | `(3,1)` PRESTAR          | Prestar un libro              |
|                          | `2`             | `(3,2)` DEVOLVER         | Devolver un libro             |
|                          | `0`             | `(0,)` VOLVER\_MENU      | Volver al menú principal      |
|                          | otro            | `(3,)` PRESTAR\_DEVOLVER | Entrada inválida → permanece  |
| `(4,)` SALIR             | —               | —                        | Estado terminal               |

    """
