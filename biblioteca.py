"""contiene la clase ItemBiblioteca
define metodos:
agregar(i: ItemBiblioteca)
buscar por titulo ()
buscar por autor ()
buscar por tipo ()
prestar(cod)
devolver(cod)
contar por tipo()
get por Codigo()"""

from item_biblioteca import ItemBiblioteca
from tipo_item import TipoItem


class Biblioteca:
    def __init__(self):
        self.lista_items = []

    def agregar(self, i: ItemBiblioteca):
        """agrega elemento type ItemBiblioteca a la lista
        atributo de la clase"""
        self.lista_items.append(i)
        # #ordenar la lista
        self.lista_items.sort(key=lambda l: l.titulo)

    def busqueda(self, clave):
        match clave:
            case str():  # si es string → buscar por titulo o autor
                for item in self.lista_items:
                    if item.titulo == clave or item.autor == clave or item.codigo == clave:
                        return item

            case TipoItem():  # si es Enum → buscar por tipo
                for item in self.lista_items:
                    if item.tipo == clave:
                        return item

            case _:  # cualquier otro tipo → no válido
                raise ValueError("Clave de búsqueda inválida")
        return None

    def prestar_devolver(self, cod: str):
        var = self.busqueda(cod)
        var.prestar_devolver()

    def contar_por_tipo(self, t: TipoItem):
        """devuelve el num de item de ese tipo"""
        return len([item for item in self.lista_items if item.tipo == t])
