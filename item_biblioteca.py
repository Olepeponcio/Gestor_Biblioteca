"""clase abstracta para gestionar los
items manejado por  una
lista en la clase Biblioteca.
Heredan de ella: """
from tipo_item import TipoItem
from abc import ABC, abstractmethod


class ItemBiblioteca(ABC):
    def __init__(self, codigo: str, titulo: str, tipo: TipoItem):
        self.codigo = codigo
        self.titulo = titulo
        self.tipo = tipo

    def __str__(self):
        return (f" codigo : {self.codigo}"
                f" titulo : {self.titulo}"
                f" {str(self.tipo)}")

    @abstractmethod
    def es_prestado(self) -> bool:
        """va a imprimir el objeto lista con su contenido, no hace
        falta iterar"""
        pass