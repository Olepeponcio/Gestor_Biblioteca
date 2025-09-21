"""hereda de libro, define atributos:
numero de la edición
periodicidad de la edición"""
from libro import Libro


class Revista(Libro):
    def __init__(self, codigo: str, titulo: str, tipoItem, autores: list, num_edi: int, periodicidad: str):
        super().__init__(codigo, titulo, tipoItem, autores)
        self.num_edi = num_edi
        self.periodicidad = periodicidad

    def __str__(self):
        return super().__str__() + (f""
                                    f" numero: {self.num_edi}"
                                    f" periodicidad: {self.periodicidad}")