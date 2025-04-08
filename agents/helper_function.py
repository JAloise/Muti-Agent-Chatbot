import pandas as pd
from langchain_community.document_loaders import UnstructuredPDFLoader,OnlinePDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import DirectoryLoader,CSVLoader
from langchain_chroma import Chroma
import glob
from PyPDF2 import PdfReader
from langchain.schema import Document  # Import the Document class
from langchain_ollama import OllamaEmbeddings  # Ensure this is imported

def emmbeding_data(embedding, collection_name, data_path, persist_data_path, data_type):
    ## =====ingesting=====
    global loader
    documents = []
    if data_type == "pdf":
        pdf_files = glob.glob(f"{data_path}/*.pdf")
        for pdf_file in pdf_files:
            reader = PdfReader(pdf_file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            # Wrap the text in a Document object
            documents.append(Document(page_content=text))
    elif data_type == "csv":
        loader = DirectoryLoader(data_path, glob="./*.csv", loader_cls=CSVLoader)
        documents = loader.load()

    ##=====extracting and chunking=====
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1200, chunk_overlap=300)
    text_chunks = text_splitter.split_documents(documents)

    ##=====adding vector to database =====
    embedding = OllamaEmbeddings(model="llama3.2")  # Use llama3.2 for embeddings
    vector_db = Chroma.from_documents(
        documents=text_chunks,
        embedding=embedding,
        persist_directory=persist_data_path,
        collection_name=collection_name,
    )



