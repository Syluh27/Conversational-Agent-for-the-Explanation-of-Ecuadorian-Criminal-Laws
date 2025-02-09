import re
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Cargar el modelo de embeddings
modelo = SentenceTransformer("distiluse-base-multilingual-cased-v2")

# Leer el texto del código penal
with open("codigo_penal.txt", "r", encoding="utf-8") as f:
    texto = f.read()

# Dividir el texto en artículos usando expresión regular
fragmentos = re.split(r'(Art\.\s*\d+[°o\.]?[\s\W]*)', texto)
fragmentos = ["".join(fragmentos[i:i+2]).strip()
             for i in range(1, len(fragmentos), 2)]

# Filtrar fragmentos vacíos y limpiar formato
fragmentos = [f.replace("\n", " ").replace("  ", " ")
             for f in fragmentos if f.strip()]

# Generar embeddings para cada fragmento
embeddings = modelo.encode(fragmentos, convert_to_numpy=True)

# Crear el índice FAISS
dimension = embeddings.shape[1]
indice_faiss = faiss.IndexFlatL2(dimension)
indice_faiss.add(embeddings)

# Guardar el índice
faiss.write_index(indice_faiss, "codigo_penal_faiss.index")

print(f"✅ Indexación completada. {len(fragmentos)} artículos procesados.")