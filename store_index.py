from src.helper import repo_ingestion, load_repo, text_splitter, download_hugging_face_embeddings
from dotenv import load_dotenv
from langchain.vectorstores import Chroma
import os




# url = "https://github.com/entbappy/End-to-end-Medical-Chatbot-Generative-AI"

# repo_ingestion(url)


documents = load_repo("repo/")
text_chunks = text_splitter(documents)
embeddings = download_hugging_face_embeddings()



#storing vector in choramdb
vectordb = Chroma.from_documents(text_chunks, embedding=embeddings, persist_directory='./db')
vectordb.persist()