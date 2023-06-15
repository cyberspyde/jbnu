import streamlit as st
from transformers import pipeline
import fitz, io, os
from haystack.document_stores import ElasticsearchDocumentStore
from haystack.nodes import BM25Retriever, FARMReader
from haystack import Pipeline
from pprint import pprint
from haystack.utils import print_answers

st.title("Team 4 - Roberta Question Answering System")
st.write("Type in a question and some context and the system will try to answer it.")

method = st.radio(
    "Choose a method to answer the question",
    ['Upload PDF', 'Upload TXT', 'Manual entry', 'JBNU'],
    key='visibility',
    horizontal=True
)

qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2", tokenizer="deepset/roberta-base-squad2")

host = os.environ.get("ELASTICSEARCH_HOST", "localhost")

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

if method == 'Manual entry':
    question = st.text_input("Question:")
    context = st.text_area("Context:")
    if st.button("Answer"):
        currenttime = 0
        answer = qa_pipeline({"context": context, "question": question})
        st.write(f"Answer: {answer['answer']}")
elif method == 'Upload PDF':
    pdf_file = st.file_uploader("Upload PDF", type=["pdf"])
    if pdf_file is not None:
        pdf_file = fitz.open(stream=pdf_file.read(), filetype="pdf")
        with pdf_file as doc:
            text = ""
            for page in doc:
                text += page.get_text()
        question = st.text_input("Question:")
        if st.button("Answer"):
            answer = qa_pipeline({"context": text, "question": question})
            st.write(f"Answer: {answer['answer']}")
elif method == 'Upload TXT':
    txt_file = st.file_uploader("Upload TXT", type=["txt"])
    if txt_file is not None:
        txt_file = io.StringIO(txt_file.read().decode('utf-8'))
        contents = txt_file.read()
        question = st.text_input("Question:")
        if st.button("Answer"):
            answer = qa_pipeline({"context": contents, "question": question})
            st.write(f"Answer: {answer['answer']}")
elif method == 'JBNU':
    question = st.text_input("Question:")
    if st.button("Answer"):
        prediction = querying_pipeline.run(
            query=str(question),
            params={
                "Retriever": {"top_k": 10},
                "Reader": {"top_k": 5}
            }
        )
        for answer in prediction["answers"]:
            st.write(f"Answer: {answer.answer}")
            st.write(f"Context: {answer.context}")
            st.write(f"Score: {answer.score}")
            st.write("---")