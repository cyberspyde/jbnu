import streamlit as st
from transformers import pipeline
import fitz, io, os
from haystack.document_stores import ElasticsearchDocumentStore
from haystack.nodes import BM25Retriever, FARMReader
from haystack import Pipeline
from pprint import pprint
from haystack.utils import print_answers

# Set page configuration
st.set_page_config(
    page_title="Team 4 - Roberta Question Answering System",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Set custom CSS styles
st.markdown(
    """
    <style>
    .title {
        text-align: center;
        font-size: 36px;
        padding: 20px 0;
        color: #336699;
    }

    .description {
        text-align: center;
        font-size: 18px;
        margin-bottom: 20px;
        color: #555555;
    }

    .example-image {
        text-align: center;
        margin-top: 40px;
    }

    .answer {
        background-color: #f5f5f5;
        border-radius: 8px;
        padding: 20px;
        margin-top: 20px;
        color: #333333;
    }

    .footer {
        text-align: center;
        font-size: 12px;
        margin-top: 40px;
        color: #888888;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Page title and description
st.markdown("<h1 class='title'>Team 4 - Roberta Question Answering System</h1>", unsafe_allow_html=True)
st.markdown("<p class='footer'><b>Research</b> is done by <br> Pardinov Firdavs - 201923196, <br> Kobilov Ilkhomjon - 201923250</p>", unsafe_allow_html=True)
st.markdown("<p class='description'><u>Type in a question and some context, and the system will try to answer it.</u></p>", unsafe_allow_html=True)

# Example image
example_image = "image2.jpg"  # Replace with your example image path
st.image(example_image, caption="Freedom, Justice and Creativity", use_column_width=True)
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
        answer = qa_pipeline({"context": context, "question": question})
        st.markdown("<div class='answer'><b>Answer:</b> " + answer['answer'] + "</div>", unsafe_allow_html=True)
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
            st.markdown("<div class='answer'><b>Answer:</b> " + answer['answer'] + "</div>", unsafe_allow_html=True)
elif method == 'Upload TXT':
    txt_file = st.file_uploader("Upload TXT", type=["txt"])
    if txt_file is not None:
        txt_file = io.StringIO(txt_file.read().decode('utf-8'))
        contents = txt_file.read()
        question = st.text_input("Question:")
        if st.button("Answer"):
            answer = qa_pipeline({"context": contents, "question": question})
            st.markdown("<div class='answer'><b>Answer:</b> " + answer['answer'] + "</div>", unsafe_allow_html=True)
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
            st.markdown("<div class='answer'><b>Answer:</b> " + answer.answer + "</div>", unsafe_allow_html=True)
            st.markdown("<div class='answer'><b>Context:</b> " + answer.context + "</div>", unsafe_allow_html=True)
            st.markdown("<div class='answer'><b>Score:</b> " + str(answer.score) + "</div>", unsafe_allow_html=True)
            st.markdown("---")
