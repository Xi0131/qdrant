# from typing import List
import json
import numpy as np

from fastembed import TextEmbedding

np.set_printoptions(suppress=True)

embedding_model = TextEmbedding()
print("The model BAAI/bge-small-en-v1.5 is ready to use.")

for i in range(1, 21553):
    f = open("./factcheck_crawled_data/fact_" + str(i) + ".json")
    data = json.load(f)
    text = f"{data['statement']} \n{data['title']} \n{data['body']}"

    embeddings_generator = embedding_model.embed(text)

    embeddings_list = list(embeddings_generator)
    # print(len(embeddings_list))

    # print("Embeddings:\n", embeddings_list[0])
    w = open("./factcheck_crawled_data/fact_" + str(i) + ".json_embedding.json", "w")

    w.write(str(embeddings_list[0]).replace("\n", "").replace(" ", "").replace("0.", ", 0.").replace("-, ", ", -").replace("[, ", "["))

    f.close()
    w.close()
    print("Generated " + str(i) + ".json_embedding.json")
