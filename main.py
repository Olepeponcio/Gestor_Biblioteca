"""┌───────────────────┐
│   Iniciar
programa│
└───────┬───────────┘
│
▼
┌──────────────────────┐
│ Instanciar
Biblioteca │
│ Instanciar
Manager    │
└─────────┬────────────┘
│
▼
┌──────────────────────┐
│ Mostrar
menú
principal│
└─────────┬────────────┘
│
┌─────────────┼──────────────────────┐
▼             ▼                      ▼
┌───────┐   ┌────────────┐        ┌───────────┐
│Añadir │   │   Buscar   │        │  Prestar  │
│libro  │   │ (titulo /   │        │ o Devolver│
│       │   │ autor / tipo)│        │   libro   │
└───┬───┘   └──────┬─────┘        └─────┬─────┘
│              │                   │
▼              ▼                   ▼
┌─────────┐  ┌────────────┐      ┌────────────┐
│ Crear   │  │ Mostrar     │      │ Actualizar │
│ objeto  │  │ resultados  │      │ estado
libro│
│ Libro   │  │ de
búsqueda │      └─────┬──────┘
└────┬────┘  └────────────┘            │
│                                 ▼
▼                          ┌────────────┐
┌────────────┐                  │ Confirmar  │
│ Insertar
en│                  │ operación  │
│ Biblioteca │                  └─────┬──────┘
└─────┬──────┘                        │
│
▼
┌───────────────┐
│ Actualizar     │
│ contadores     │
└─────┬─────────┘
│
▼
┌───────────────┐
│ Volver
a
menú │
└───────┬───────┘
│
▼
┌────────────┐
│ Salir      │
└────────────┘
"""


# # instanciar biblioteca
# biblioteca = Biblioteca()
# # instanciar manager