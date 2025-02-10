import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Cargar el índice FAISS
indice_faiss = faiss.read_index("codigo_penal_faiss.index")

# Cargar el modelo de embeddings
modelo = SentenceTransformer("distiluse-base-multilingual-cased-v2")


def realizar_consulta(query, k=5):
    # Generar el embedding de la consulta
    embedding_query = modelo.encode([query], convert_to_numpy=True)

    # Buscar los k artículos más cercanos en el índice FAISS
    distancias, indices = indice_faiss.search(embedding_query, k)

    # Mostrar los resultados
    print(f"Consulta: {query}")
    print(f"Resultados más cercanos:")

    for i in range(k):
        print(f"\nArtículo {indices[0][i]} (Distancia: {distancias[0][i]}):")
        print(fragmentos[indices[0][i]])  # Muestra el fragmento correspondiente al artículo
        print("=" * 50)

# Realizar una consulta ejemplo
consulta = "¿Qué dice el código penal sobre el robo?"
realizar_consulta(consulta)
