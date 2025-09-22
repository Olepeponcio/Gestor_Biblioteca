"""Es la clase principal que correrá el programa en el módulo main.
tiene como atributo un objeto de la clase biblioteca
define metodos para correr el programa"""

from biblioteca import Biblioteca


class BibliotecaManager:
    def __init__(self, biblioteca: Biblioteca):
        self.biblioteca = biblioteca

    def mostrar_menu(self):
        """muestra las  opciones disponibles"""
        pass

    def gestionar_entrada(self):
    #   crear objeto libro
    #   realizar busqueda?
    #   insertar en biblioteca
    #   actualizar contadores
        pass


    # opcion agregar libro

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

    # run






