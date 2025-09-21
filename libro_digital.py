"""esta clase no manejará un contador numero de descargas
por si escala el programa y añadimos valoraciones de libros"""
from libro import Libro

class LibroDigital(Libro):
    """define atriburos formato de la revista y tamano del archivo"""
    def __init__(self, codigo: str, titulo: str, tipoItem, autores: list, formato: str, tam: float):
        super().__init__(codigo, titulo, tipoItem, autores)
        self.formato = formato
        self.tam = tam
        self.num_descargas = 0

    def __str__(self):
        return super().__str__() + (f""
                                    f" formato: {self.formato}"
                                    f" tamaño: {self.tam}"
                                    f" descargas: {self.num_descargas}")

    def descargas(self):
        if self.es_prestado():
            self.num_descargas += 1

    def numero_descarados(self):
        return self.num_descargas






