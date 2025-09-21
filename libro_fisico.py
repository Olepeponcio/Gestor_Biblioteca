"""clase hija de libro. munico atributo ubicacion
biblioteca"""
from libro import Libro


class LibroFisico(Libro):
    def __init__(self, ubicacion: str, codigo: str, titulo: str, tipoItem, autores: list):
        super().__init__(codigo, titulo, tipoItem, autores)
        self.ubicacion = ubicacion

    def __str__(self):
        return super().__str__() + (f""
                                    f" ubicacion: {self.ubicacion}")



    def donde_ubicado(self):
        """de momento por si debe usarse en el LibreriaManager"""
        return self.ubicacion
