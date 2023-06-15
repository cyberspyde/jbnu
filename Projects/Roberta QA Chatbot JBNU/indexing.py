from haystack.utils import fetch_archive_from_http
from haystack.document_stores import ElasticsearchDocumentStore
import os
from haystack import Pipeline
from haystack.nodes import TextConverter, PreProcessor
doc_dir = "data/JBNU-FOCUS"

host = os.environ.get("ELASTICSEARCH_HOST", "localhost")
print(host)
document_store = ElasticsearchDocumentStore(
    host='121.186.58.11',
    username="",
    password="",
    index="document"
)


indexing_pipeline = Pipeline()
text_converter = TextConverter()
preprocessor = PreProcessor(
    clean_whitespace=True,
    clean_header_footer=True,
    clean_empty_lines=True,
    split_by="word",
    split_length=200,
    split_overlap=20,
    split_respect_sentence_boundary=True,
)

import os

indexing_pipeline.add_node(component=text_converter, name="TextConverter", inputs=["File"])
indexing_pipeline.add_node(component=preprocessor, name="PreProcessor", inputs=["TextConverter"])
indexing_pipeline.add_node(component=document_store, name="DocumentStore", inputs=["PreProcessor"])

files_to_index = [doc_dir + "/" + f for f in os.listdir(doc_dir)]
indexing_pipeline.run_batch(file_paths=files_to_index)