import unicodedata
import re

def limpiar_texto(texto: str) -> str:
    # 1. Normalizar a forma NFD (descompone letras y acentos)
    nfkd_form = unicodedata.normalize("NFD", texto)
    # 2. Eliminar marcas de acento (categoría Mn = Mark, Nonspacing)
    sin_tildes = "".join([c for c in nfkd_form if unicodedata.category(c) != "Mn"])
    # 3. Convertir a minúsculas
    sin_tildes = sin_tildes.lower()
    # 4. Opcional: eliminar cualquier caracter que no sea letra/espacio
    limpio = re.sub(r"[^a-z\s]", "", sin_tildes)
    return limpio.strip()