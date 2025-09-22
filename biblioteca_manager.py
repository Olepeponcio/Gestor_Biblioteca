"""Es la clase principal que correrá el programa en el módulo main.
tiene como atributo un objeto de la clase biblioteca
define metodos para correr el programa"""

from biblioteca import Biblioteca
from tipo_item import TipoItem
from autor  import Autor
from item_biblioteca import ItemBiblioteca


class BibliotecaManager:
    def __init__(self, biblioteca: Biblioteca):
        self.biblioteca = biblioteca

    def mostrar_menu(self):
        """muestra las  opciones disponibles"""
        pass

    def crear_item_desde_input(self):
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






