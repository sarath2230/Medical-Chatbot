from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader, PyMuPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings

from langchain.text_splitter import RecursiveCharacterTextSplitter




def load_single_pdf(pdf_path):

    loader = PyMuPDFLoader(pdf_path)
    documents = loader.load()
        
    return documents

def text_split(pdf_documents):
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=20)
    text_chunks=text_splitter.split_documents(pdf_documents)
    return text_chunks


def download_hugging_face_embeddings():
    embeddings=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return embeddings

