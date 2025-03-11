# https://30880cbd-3d6a-44ac-9380-73cb4e646d78.us-east4-0.gcp.cloud.qdrant.io
from qdrant_client import QdrantClient, models
import json

qdrant_client = QdrantClient(
    url="https://30880cbd-3d6a-44ac-9380-73cb4e646d78.us-east4-0.gcp.cloud.qdrant.io:6333", 
    api_key="0qqkGyhVdHpfxg_4uyfztXcxFDnrtqJUGDbE3swzXD7Cj1mnCdQUwA",
)

# reference
# qdrant_client.upsert(
#     collection_name="demo",
#     points=models.Batch(
#         ids=[1, 2, 3],
#         payloads=[
#             {"color": "red"},
#             {"color": "green"},
#             {"color": "blue"},
#         ],
#         vectors=[
#             [0.9, 0.1, 0.1],
#             [0.1, 0.9, 0.1],
#             [0.1, 0.1, 0.9],
#         ],
#     ),
# )

ids = []
payloads = []
vectors = []
# politifact has 21152 data
for i in range(1, 2):
    
    print("Reading 500 data")
    for j in range(21001, 21153):
        id = j + (i - 1) * 500
        print("Reading file id : ", id)
        file = open("./factcheck_crawled_data/fact_" + str(id) + ".json")
        try:
            f = json.load(file)
        except:
            print(file)
        vec = open("./factcheck_crawled_data/fact_" + str(id) + ".json_embedding.json")
        try:
            v = json.load(vec)
        except:
            print(vec)
        
        ids.append(id)
        payloads.append(f)
        vectors.append(v)
        
    # make comment for last 21001-21152 data
    # if len(ids) != 500 or len(payloads) != 500 or len(vectors) != 500:
    #     print(len(ids))
    #     print(len(payloads))
    #     print(len(vectors))
    #     break
        
    # upload batch
    print("uploading batch : ", i)
    qdrant_client.upsert(
        collection_name="polifact_dataset",
        points=models.Batch(
            ids=ids,
            payloads=payloads,
            vectors=vectors,
        )
    )
    print("Successfully upload batch : ", i)
    
    # flush
    ids = []
    payloads = []
    vectors = []