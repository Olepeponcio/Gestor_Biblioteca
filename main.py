"""modulo que ejecuta el programa desde
la máquina de estados"""

from biblioteca import Biblioteca
from biblioteca_manager import BibliotecaManager, Opciones

def main():
    # 1. Crear la biblioteca (vacía al inicio)
    biblio = Biblioteca()

    # 2. Crear el gestor de estados
    gestor = BibliotecaManager(biblio)

    # 3. Estado inicial = menú principal
    estado = Opciones.MENU

    # 4. Bucle principal de la aplicación
    while estado is not None:
        estado = gestor.manejar_estado(estado)

main()