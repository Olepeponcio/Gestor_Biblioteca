"""hereda de ItemBiblioteca. Tiene los métodos prestar y devolver
que modifican el atributo de la clase heredadd"""
from item_biblioteca import ItemBiblioteca
from autor import Autor

class Libro(ItemBiblioteca):
    """asigna valor a sus atributos y define dos metodos de estado"""
    def __init__(self, codigo: str, titulo: str, tipoItem, autores: list):
        super().__init__(codigo, titulo, tipoItem)
        self.numero_librs = 0
        self.prestado = False
        self.autores = autores

        for autor in self.autores:
            try:
                autor.libros.append(self)
            except AttributeError:
                # Si el autor no tiene lista de libros, la creamos
                # autor.libros = [self]
                print ("Algo salió mal añadiendo el libro a la lista")



    def __str__(self):
        """es una lista de Autores"""
        var = ""
        for autor in self.autores:
            var += autor.__str__()

        return super().__str__() + var


    def prestar_devolver(self):
        self.prestado = not self.prestado

    def es_prestado(self):
        return self.prestado





