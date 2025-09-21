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
from biblioteca import Biblioteca

autor1 = Autor("Gabriel", "Garcia Marquez", "Colombiana")
autor2  = Autor("Julio", "Cortazar", "Belga")
autores = [autor1, autor2]
var1 = LibroFisico("pasillo e", "00000", "100 anos de soledad", TipoItem.FISICO, autores)
var2 = LibroDigital("00000", "100 anos de soledad", TipoItem.DIGITAL, autores, ".pdf", 12.5)
var3 = Revista("00000", "100 anos de soledad", TipoItem.REVISTA, autores, 1, "trimestral" )
# print(var1.__str__())
# print(var2.__str__())
# print(var3.__str__())

biblio = Biblioteca()
biblio.agregar(var1)
biblio.agregar(var2)
biblio.agregar(var3)

var4 = biblio.busqueda("100 anos de soledad")
# print(var4)
var5 = biblio.prestar_devolver("00000")
print(var5)
var6 = biblio.contar_por_tipo(TipoItem.FISICO)
print(var6)