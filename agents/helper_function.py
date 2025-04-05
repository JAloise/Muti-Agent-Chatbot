import pandas as pd
from langchain_community.document_loaders import UnstructuredPDFLoader,OnlinePDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import DirectoryLoader,CSVLoader
from langchain_chroma import Chroma
import glob

def emmbeding_data(embedding,collection_name,data_path,persist_data_path,data_type):
    ## =====ingesting=====
    global loader
    if data_type =="pdf":
        loader = DirectoryLoader(data_path,glob="./*.pdf",loader_cls=UnstructuredPDFLoader)
    elif data_type =="csv":
        loader = DirectoryLoader(data_path, glob="./*.csv", loader_cls=CSVLoader)
    documents = loader.load()
    ##=====extracting and chunking=====
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1200,chunk_overlap=300)
    text_chunks = text_splitter.split_documents(documents)
    #print(documents)
    ##=====adding vector to database =====
    vector_db = Chroma.from_documents(
        documents=text_chunks,
        embedding=embedding,
        persist_directory=persist_data_path,
        collection_name=collection_name,
    )



# quetions = ["what is SOEN 423","can you give me description of its course material","then what is SOEN 422","Compare soen 423 and soen 422",
#             "what are the preriqusites of computer science", "How many credits is the program","how logn does it take to finish the program",
#             "which courses cover embedded systems","which courses cover programing", "what si soen 390","what are its preriquisites","do I need to take it",
#             "which programs cover math","how many credits do i need to complete computer science"]
