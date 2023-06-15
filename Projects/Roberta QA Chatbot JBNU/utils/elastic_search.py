import os
from haystack.document_stores import ElasticsearchDocumentStore
from haystack.nodes import FARMReader
from haystack.nodes import BM25Retriever
from haystack import Pipeline
# Get the host where Elasticsearch is running, default to localhost
host = os.environ.get("ELASTICSEARCH_HOST", "localhost")
print(host)
document_store = ElasticsearchDocumentStore(
    host='121.186.58.11',
    username="",
    password="",
    index="document"
)

retriever = BM25Retriever(document_store=document_store)
reader = FARMReader(model_name_or_path="deepset/roberta-base-squad2", use_gpu=True)

querying_pipeline = Pipeline()
querying_pipeline.add_node(component=retriever, name="Retriever", inputs=["Query"])
querying_pipeline.add_node(component=reader, name="Reader", inputs=["Retriever"])

prediction = querying_pipeline.run(
    query="what is the university name?",
    params={
        "Retriever": {"top_k": 10},
        "Reader": {"top_k": 5}
    }
)

for a in prediction['answers']:
    print(a.answer)