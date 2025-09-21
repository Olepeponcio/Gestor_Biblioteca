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
from autor import Autor
from libro_fisico import LibroFisico
from libro_digital import LibroDigital
from revista import Revista
from tipo_item import TipoItem

autor1 = Autor("Gabriel", "Garcia Marquez", "Colombiana")
autor2  = Autor("Julio", "Cortazar", "Belga")
autores = [autor1, autor2]
var1 = LibroFisico("pasillo e", "00000", "100 anos de soledad", TipoItem.FISICO, autores)
print(var1.__str__())
