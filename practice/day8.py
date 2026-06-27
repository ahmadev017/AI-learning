from sentence_transformers import SentenceTransformer
import numpy as np
texts = [

"he works at apple company",

"Apple is my favourite fruit",

"He is an employee of Apple.",

"I enjoy kittens",

"My favorite animal is a cat"
]

model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(texts)

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

print(
    "Similarity (Apple vs Apple(fruit)):",
    round(cosine_similarity(embeddings[0], embeddings[1]), 4)
)

print(
    "Similarity (Apple vs Apple):",
    round(cosine_similarity(embeddings[0], embeddings[2]), 4)
)
#print(embeddings.shape)
#print(embeddings[0])