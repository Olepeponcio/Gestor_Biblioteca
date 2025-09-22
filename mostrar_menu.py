"""modulo para importar los metodos que pintan en pantalla
menus de opciones. Lo usa Biblioteca Manager"""


def mostrar_menu_principal():
    """Mostrar las opciones disponibles (estado = (n,))"""
    print("=" * 40)
    print("📚  Bienvenido al Gestor de Bibliotecas")
    print("=" * 40)
    print("[1] ➕ Agregar libro")            # Opciones.AGREGAR = (1,)
    print("[2] 🔍 Buscar en la biblioteca")  # Opciones.BUSCAR = (2,)
    print("[3] 🔄 Prestar / Devolver libro") # Opciones.PRESTAR_DEVOLVER = (3,)
    print("[4] 🚪 Salir")                    # Opciones.SALIR = (4,)
    print("-" * 40)
    # print("👉 Selecciona una opción:")


def mostrar_submenu_busqueda():
    """Mostrar opciones del submenú de búsqueda (estado = (2, sub))"""
    print("=" * 40)
    print("🔍  Búsqueda en la Biblioteca")
    print("=" * 40)
    print("[1] Buscar por Autor")   # Opciones.BUSCAR_AUTOR = (2,1)
    print("[2] Buscar por Título")  # Opciones.BUSCAR_TITULO = (2,2)
    print("[3] Buscar por Codigo")    # Opciones.BUSCAR_TIPO = (2,3)
    print("-" * 40)
    print("[0] ⬅️  Volver al Menú Principal") # Opciones.VOLVER_MENU = (0,)
    print("-" * 40)


def mostrar_submenu_prestamos():
    """Mostrar opciones del submenú de préstamos (estado = (3, sub))"""
    print("=" * 40)
    print("🔄  Prestar / Devolver")
    print("=" * 40)
    print("[1] Prestar libro")     # Opciones.PRESTAR = (3,1)
    print("[2] Devolver libro")    # Opciones.DEVOLVER = (3,2)
    print("-" * 40)
    print("[0] ⬅️  Volver al Menú Principal") # Opciones.VOLVER_MENU = (0,)
    print("-" * 40)


def mostrar_submenu_agregar():
    print("\n📚 Submenú AGREGAR")
    print("1. Agregar Libro Físico")
    print("2. Agregar Libro Digital")
    print("3. Agregar Revista")
    print("0. Volver al menú principal")
