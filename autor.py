"""clase independiente. tiene atributos tipo string
nombre, apellido, nacionalidad, función que devuevle
la cadena completa. Es usada en class Libro"""

class Autor:
    """define cadena string y una lista de libros que asigna
    valor en la clase Libros. relacion mucho a muchos"""
    def __init__(self, nombre: str, apellido: str, nacionalidad: str):
        self.nombre =  nombre
        self.apellido = apellido
        self.nacionalidad = nacionalidad
        self.libros = []


    def __str__(self):
        return (f" Nombre: {self.nombre}, Apellidos: {self.apellido}"
                f" Nacionalidad: {self.nacionalidad}")


    def nombre_completo(self):
        """devuelve una cadena str"""
        return self.nombre + " " + self.apellido