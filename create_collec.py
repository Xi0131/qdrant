from qdrant_client import QdrantClient, models

qdrant_client = QdrantClient(
    url="https://30880cbd-3d6a-44ac-9380-73cb4e646d78.us-east4-0.gcp.cloud.qdrant.io:6333", 
    api_key="0qqkGyhVdHpfxg_4uyfztXcxFDnrtqJUGDbE3swzXD7Cj1mnCdQUwA",
)

def create_collec(name: str, size: int):
    qdrant_client.create_collection(
        collection_name=name,
        vectors_config=models.VectorParams(size=size, distance=models.Distance.COSINE),
        optimizers_config=models.OptimizersConfigDiff(
            indexing_threshold=0,
        ),
    ) 

def del_collec(name: str):
    qdrant_client.delete_collection(collection_name=name)

# qdrant_client.create_collection(
#     collection_name="demo",
#     vectors_config=models.VectorParams(size=3, distance=models.Distance.COSINE),
# ) 

# print(qdrant_client.get_collections())

# del_collec("polifact_dataset")
# create_collec("polifact_dataset", 384)

info = qdrant_client.get_collection(collection_name="polifact_dataset")
print(info)

# print(qdrant_client.count(collection_name="demo"))

# scroll = qdrant_client.scroll(
#     collection_name="demo",
#     # scroll_filter=models.Filter(
#     #     must=[
#     #         models.FieldCondition(key="color", match=models.MatchValue(value="red")),
#     #     ]
#     # ),
#     # limit=1,
#     with_payload=True,
#     with_vectors=False,
# )

# print(scroll)