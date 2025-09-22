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
        """Devuelve lista de items que cumplen con la clave"""
        match clave:
            case str():
                return [
                    item for item in self.lista_items
                    if (item.titulo == clave
                        or item.codigo == clave
                        or any(autor.nombre_completo() == clave for autor in item.autores))
                ]
            case TipoItem():
                return [item for item in self.lista_items if item.tipo == clave]
            case _:
                raise ValueError("Clave de búsqueda inválida")

    def prestar_devolver(self, clave, accion: str):
        """Es usado por Biblioteca Manager.
        llama a self.busqueda(clave) e itera en la lista comprobando
        el estado del libro y cambia según no prestado
        devuelve estado para control desde manager deberia devolver
        True, False (libro prestado o no) y None (porque puede que el libro no esté en la lista)"""
        libros = self.busqueda(clave)
        estado = None
        # comprobar que la lista no esté vacia
        if libros:
            for libro in libros:
                if accion == "prestar":
                    if  not libro.es_prestado():
                        libro.prestar_devolver()
                        estado = True
                elif accion == "devolver":
                    if libro.es_prestado():
                        libro.prestar_devolver()
                        estado = True
                else:
                    estado = None
            return estado


    def contar_por_tipo(self, t: TipoItem):
        """devuelve el num de item de ese tipo"""
        return len([item for item in self.lista_items if item.tipo == t])





