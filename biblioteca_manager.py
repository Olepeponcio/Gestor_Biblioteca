from enum import Enum
from biblioteca import Biblioteca
from tipo_item import TipoItem
from autor import Autor
from mostrar_menu import mostrar_menu_principal, mostrar_submenu_busqueda, mostrar_submenu_prestamos, mostrar_submenu_agregar
# from libro_fisico import LibroFisico
# from libro_digital import LibroDigital
# from item_biblioteca import ItemBiblioteca
from libro import Libro
from revista import Revista



from enum import Enum

class Opciones(Enum):
    # Menú principal
    MENU = (1,)
    AGREGAR = (1,)

    # Submenú AGREGAR
    AGREGAR_LIBRO = (1, 1)
    AGREGAR_LIBRO_DIGITAL = (1, 2)
    AGREGAR_REVISTA = (1, 3)

    # Menú principal
    BUSCAR = (2,)
    BUSCAR_AUTOR = (2, 1)
    BUSCAR_TITULO = (2, 2)
    BUSCAR_TIPO = (2, 3)

    PRESTAR_DEVOLVER = (3,)
    PRESTAR = (3, 1)
    DEVOLVER = (3, 2)

    SALIR = (4,)


class BibliotecaManager:
    def __init__(self, biblioteca: Biblioteca):
        self.biblioteca = biblioteca

        # Diccionario de menús (pintado)
        self.menus = {
            Opciones.MENU: mostrar_menu_principal,
            Opciones.AGREGAR: mostrar_submenu_agregar,
            Opciones.BUSCAR: mostrar_submenu_busqueda,
            Opciones.PRESTAR_DEVOLVER: mostrar_submenu_prestamos,
        }

        # Diccionario de acciones
        self.acciones = {
            # Submenú AGREGAR
            Opciones.AGREGAR_LIBRO: self.gestionar_entrada_libro,
            Opciones.AGREGAR_LIBRO_DIGITAL: self.gestionar_entrada_libro_digital,
            Opciones.AGREGAR_REVISTA: self.gestionar_entrada_revista,

            # Submenú BUSCAR
            Opciones.BUSCAR_AUTOR: lambda: self.opcion_buscar("autor"),
            Opciones.BUSCAR_TITULO: lambda: self.opcion_buscar("titulo"),
            Opciones.BUSCAR_TIPO: lambda: self.opcion_buscar("tipo"),

            # Submenú PRESTAR/DEVOLVER
            Opciones.PRESTAR: lambda: self.opcion_prestar(input("Código a prestar: ")),
            Opciones.DEVOLVER: lambda: self.opcion_devolver(input("Código a devolver: ")),
        }

    # -------------------------
    #   Gestión de opciones
    # -------------------------
    def opciones_seleccion(self, estado_actual: Opciones):
        """Traducir input → Opciones, en función del contexto"""
        entrada = input("👉 Elige una opción: ").strip()

        if not entrada.isdigit():
            print("⚠️ Entrada inválida.")
            return Opciones.MENU

        n = int(entrada)

        # Menú principal
        if estado_actual == Opciones.MENU:
            if n == 0:
                return Opciones.MENU
            try:
                # 1→(1,), 2→(2,), 3→(3,), 4→(4,)
                return Opciones((n,))
            except ValueError:
                print("⚠️ Opción inexistente.")
                return Opciones.MENU

        # Submenú AGREGAR
        if estado_actual == Opciones.AGREGAR:
            if n == 0:
                return Opciones.MENU
            return Opciones((1, n)) if (1, n) in [o.value for o in Opciones] else Opciones.AGREGAR

        # Submenú BUSCAR
        if estado_actual == Opciones.BUSCAR:
            if n == 0:
                return Opciones.MENU
            return Opciones((2, n)) if (2, n) in [o.value for o in Opciones] else Opciones.BUSCAR

        # Submenú PRESTAR/DEVOLVER
        if estado_actual == Opciones.PRESTAR_DEVOLVER:
            if n == 0:
                return Opciones.MENU
            return Opciones((3, n)) if (3, n) in [o.value for o in Opciones] else Opciones.PRESTAR_DEVOLVER

        return Opciones.MENU

    def manejar_estado(self, estado_actual: Opciones):
        """Pinta menú y devuelve siguiente estado"""
        # 1. Pintar menú si corresponde
        if estado_actual in self.menus:
            self.menus[estado_actual]()

        # 2. Si hay acción asociada → ejecutar y volver al menú principal
        elif estado_actual in self.acciones:
            self.acciones[estado_actual]()
            return Opciones.MENU

        # 3. Estado especial SALIR
        if estado_actual == Opciones.SALIR:
            print("👋 Saliendo...")
            return None

        # 4. Pedir input y calcular siguiente estado
        return self.opciones_seleccion(estado_actual)

    # -------------------------
    #   Acciones
    # -------------------------
    def crear_item_desde_input(self, tipo_item, es_revista=False):
        """Generar un ItemBiblioteca o Revista a partir del input"""

        try:
            codigo = input("Código: ").strip()
            titulo = input("Título: ").strip()

            print("Autores (Nombre|Apellidos|Nacionalidad, separados por coma)")
            autores_str = input("> ").strip()
            autores = []
            if autores_str:
                for datos in autores_str.split(","):
                    partes = [p.strip() for p in datos.split("|")]
                    if len(partes) == 3:
                        autores.append(Autor(*partes))
                    else:
                        raise ValueError(f"Formato inválido: '{datos}'")

            # Caso especial: Revista
            if es_revista:
                num_edi = int(input("Número de edición: ").strip())
                periodicidad = input("Periodicidad (semanal/mensual/etc): ").strip()
                return Revista(codigo, titulo, tipo_item, autores, num_edi, periodicidad)

            # Caso general: Libro o Libro Digital → ItemBiblioteca
            return Libro(codigo, titulo, tipo_item, autores)

        except Exception as e:
            print(f"Error: {e}")
            return None

    def gestionar_entrada_libro(self):
        item = self.crear_item_desde_input(TipoItem.FISICO)
        if item:
            self.biblioteca.agregar(item)
            print("✅ Libro físico agregado.")
    # wrappers de acciones
    def gestionar_entrada_libro_digital(self):
        item = self.crear_item_desde_input(TipoItem.DIGITAL)
        if item:
            self.biblioteca.agregar(item)
            print("✅ Libro digital agregado.")

    def gestionar_entrada_revista(self):
        item = self.crear_item_desde_input(TipoItem.REVISTA, es_revista=True)
        if item:
            self.biblioteca.agregar(item)
            print("✅ Revista agregada.")

    def gestionar_entrada(self):
        item = self.crear_item_desde_input()
        if item:
            self.biblioteca.agregar(item)
            print("✅ Libro agregado.")

    def opcion_buscar(self, clave):
        if not self.biblioteca.lista_items:  # asumiendo que biblioteca guarda los libros en .items
            print("📭 No hay libros en la biblioteca.")
            return
        resultado = self.biblioteca.busqueda(clave)
        if not resultado:
            print("📚 Ningún libro encontrado con esa búsqueda.")
        else:
            print(resultado)

    def opcion_prestar(self, clave):
        """usa buscar de la clase Biblioteca que itera en la lista de items.
        Si el codigo está mal introducido o el libro no está lanzará un print"""
        if self.biblioteca.prestar_devolver(clave, "prestar") is not None:
            pass
        else:
            print("📚 Ningún libro encontrado con esa búsqueda.")


    def opcion_devolver(self, clave):
        """usa buscar de la clase Biblioteca que itera en la lista de items.
        Si el codigo está mal introducido o el libro no está lanzará un print"""
        self.biblioteca.prestar_devolver(clave, "devolver")

