from qdrant_client import QdrantClient
from qdrant_client.http.models import PointStruct, VectorParams
from transformers import GPT2Tokenizer, GPT2Model
import uuid

# Configura el cliente Qdrant y la colección
qdrant_client = QdrantClient(host="localhost", port=6333)
qdrant_client.recreate_collection(
    collection_name="my_collection",
    vectors_config=VectorParams(size=768, distance="Cosine")  # Asegúrate de que el tamaño del vector sea correcto
)

# Inicializa el tokenizador y el modelo GPT-2
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2Model.from_pretrained("gpt2")

def get_embedding(text):
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).detach().numpy()

def store_embedding(user_input, embedding):
    point_id = str(uuid.uuid4())  # Genera un UUID válido
    qdrant_client.upsert(
        collection_name="my_collection",
        points=[
            PointStruct(
                id=point_id,
                vector=embedding.flatten().tolist(),  # Asegúrate de convertir el vector a una lista
                payload={"user_input": user_input}
            )
        ]
    )