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
            case str():
                for item in self.lista_items:
                    if (item.titulo == clave
                            or item.codigo == clave
                            or any(autor.nombre_completo() == clave for autor in item.autores)
                    ):
                        return item
                return None
            case TipoItem():  # si es Enum → buscar por tipo
                for item in self.lista_items:
                    if item.tipo == clave:
                        return item
                return None

            case _:  # cualquier otro tipo → no válido
                raise ValueError("Clave de búsqueda inválida")

    def prestar_devolver(self, cod: str):
        """Es usado por Biblioteca Manager;
        realiza la busqueda según argumento
        debería devolver"""
        var = self.busqueda(cod)
        if  var is not None:
            var.prestar_devolver()
        return var.es_prestado()

    def contar_por_tipo(self, t: TipoItem):
        """devuelve el num de item de ese tipo"""
        return len([item for item in self.lista_items if item.tipo == t])
