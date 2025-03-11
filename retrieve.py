from qdrant_client import QdrantClient
import json
import numpy as np
from fastembed import TextEmbedding

np.set_printoptions(suppress=True)

qdrant_client = QdrantClient(
    url="https://30880cbd-3d6a-44ac-9380-73cb4e646d78.us-east4-0.gcp.cloud.qdrant.io:6333", 
    api_key="0qqkGyhVdHpfxg_4uyfztXcxFDnrtqJUGDbE3swzXD7Cj1mnCdQUwA",
)

text='''
Says Maggie Hassan was \"out of state on 30 days over the last three months
'''

embedding_model = TextEmbedding()
embeddings_generator = embedding_model.embed(text)
embeddings_list = list(embeddings_generator)

print(embeddings_list[0])
vector = embeddings_list[0]
print(len(vector))
vector = str(embeddings_list[0]).replace("\n", "").replace(" ", "").replace("0.", ", 0.").replace("-, ", ", -").replace("[, ", "[")
print(vector)
print(list(vector))

reply = qdrant_client.query_points(
    collection_name="polifact_dataset",
    query=vector, # <--- Dense vector
    score_threshold=0.7,
    limit=3,
    with_payload=True,
).points
print(reply)
if len(reply) == 0:
    print("hailat")
else:
    print(reply[0].payload['url'])
    urls = []
    for i in range(len(reply)):
        urls.append(reply[i-1].payload['url'])
    print(urls)