import fitz  # PyMuPDF
import re


def extraer_texto_pdf(ruta_pdf):
    """Extrae y limpia el texto de un PDF."""
    texto_completo = []

    with fitz.open(ruta_pdf) as pdf:
        for num_pagina in range(len(pdf)):
            pagina = pdf[num_pagina]
            texto = pagina.get_text("text")
            texto = limpiar_texto(texto)
            texto_completo.append(texto)

    return "\n".join(texto_completo)


def limpiar_texto(texto):
    """Limpia el texto eliminando caracteres innecesarios."""
    texto = re.sub(r'\s+', ' ', texto)  # Eliminar saltos de línea excesivos
    texto = re.sub(r'[^A-Za-zÁÉÍÓÚáéíóúñÑ0-9.,;:\s]', '', texto)  # Eliminar caracteres raros
    return texto.strip()


# Prueba con un PDF
ruta_pdf = "codigopenalEC.pdf" # Reemplázalo con tu archivo
texto = extraer_texto_pdf(ruta_pdf)

# Guarda el texto en un archivo
with open("codigo_penal.txt", "w", encoding="utf-8") as f:
    f.write(texto)

print("✅ Extracción y limpieza completadas. Texto guardado en 'codigo_penal.txt'.")
