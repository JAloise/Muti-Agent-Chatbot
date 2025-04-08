## PDF rag
from jupyter_server.auth.security import persist_config
from langchain_community.document_loaders import UnstructuredPDFLoader,OnlinePDFLoader
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate,PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import  RunnablePassthrough
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain_community.document_loaders import DirectoryLoader
from langchain_chroma import Chroma
import ollama
from pathlib import Path
import os
import glob


DIRECTORY_PATH = str(Path.cwd())
CONCORDIA_FULL_PATH = DIRECTORY_PATH + r"\data\concordia\\"
STORAGE_PATH_CONCORDIA = CONCORDIA_FULL_PATH + r"db\\"
if os.system == "Darwin" or os.system == "Linux":
    CONCORDIA_FULL_PATH = DIRECTORY_PATH+ r"/data/concordia//"
    STORAGE_PATH_CONCORDIA = CONCORDIA_FULL_PATH + r"db//"

print(CONCORDIA_FULL_PATH+ "*")
print(glob.glob(CONCORDIA_FULL_PATH+ "*.csv"))
print(glob.glob(CONCORDIA_FULL_PATH+ "*.pdf"))

def emmbeded_pdf_data():
    #pdf_list = glob.glob(CONCORDIA_FULL_PATH+ "*.pdf")
    ## =====ingesting pdf=====
    loader = DirectoryLoader(CONCORDIA_FULL_PATH,glob="./*.pdf",loader_cls=UnstructuredPDFLoader)
    documents = loader.load()
    #print(documents)
    ##=====extracting pdf and chunking=====
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1200,chunk_overlap=300)
    text_chunks = text_splitter.split_documents(documents)
    print(documents)
    ##=====adding vector to database =====
    local_embedding = OllamaEmbeddings(model="mxbai-embed-large")
    vector_db = Chroma.from_documents(
        documents = text_chunks,
        embedding=local_embedding,
        persist_directory= STORAGE_PATH_CONCORDIA,
        collection_name="concordia",
    )
    #print("%%%%%%%%%%%%%%%%%%%%%%%%% DONE %%%%%%%%%%%%%%%%%%%%%%%%%")


def retrieve_pdf_data():
    local_embedding = OllamaEmbeddings(model="llama3.2")
    vectordb =Chroma(persist_directory=STORAGE_PATH_CONCORDIA,
                     embedding_function=local_embedding)
    retriever = vectordb.as_retriever()
    docs = retriever.invoke("get concordai info")
    print(vectordb)
    return docs

#emmbeded_pdf_data()
retrieve_pdf_data()
