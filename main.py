"""modulo que ejecuta el programa desde
la máquina de estados"""
import os
import sys
import json
from pathlib import Path

from biblioteca import Biblioteca
from biblioteca_manager import BibliotecaManager, Opciones
from tipo_item import TipoItem
from autor import Autor
from libro import Libro
from revista import Revista


# lecutra de archvio y construir objetos añadiendolos a su lista_items
def construir_item(item_dict):
    """Recibe un diccionario del JSON y devuelve un objeto de la clase correcta."""
    aux = item_dict["tipo"].upper()
    tipo = None

    if aux == "FISICO":
        tipo = TipoItem.FISICO
    elif aux == "DIGITAL":
        tipo = TipoItem.DIGITAL
    elif aux == "REVISTA":
        tipo = TipoItem.REVISTA

    codigo = item_dict["codigo"].lower()
    titulo = item_dict["titulo"].lower()
    autores = [Autor(a["nombre"].lower(), a["apellidos"].lower(), a["nacionalidad"].lower())
               for a in item_dict["autores"]]

    if tipo == "REVISTA":
        return Revista(codigo, titulo, tipo, autores,
                       item_dict["num_edi"], item_dict["periodicidad"].lower())
    elif tipo in TipoItem:
        # return TIPO_MAP[tipo](codigo, titulo, tipo, autores)
        return Libro(codigo, titulo, tipo, autores)
    else:
        raise ValueError(f"Tipo desconocido: {tipo}")


def cargar_desde_json(ruta_archivo, biblioteca):
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as f:
            datos = json.load(f)

        for item_dict in datos:
            objeto = construir_item(item_dict)
            biblioteca.agregar(objeto)  # lo añadimos a la colección

        print(f"📚 {len(biblioteca.lista_items)} items cargados desde {ruta_archivo}")

    except Exception as e:
        print(f"⚠️ Error cargando biblioteca: {e}")


# Ruta absoluta del archivo actual
ruta_catalogo = r"C:\Users\PEPIN\D_JOSE\FORMACION\PYTHON_Autodidacta\Biblioteca\Gestor_Biblioteca\catalogo.json"


def main():
    # 1. Crear la biblioteca (vacía al inicio)
    biblio = Biblioteca()

    # 2. Crear el gestor de estados
    gestor = BibliotecaManager(biblio)

    # construir el catalogo previo
    cargar_desde_json(ruta_catalogo, gestor.biblioteca)
    for i in gestor.biblioteca.lista_items:
        print(i.__str__())


    # 3. Estado inicial = menú principal
    estado = Opciones.MENU

    # 4. Bucle principal de la aplicación
    while estado is not None:
        estado = gestor.manejar_estado(estado)


main()
