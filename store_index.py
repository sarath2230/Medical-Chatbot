from src.helper import load_single_pdf,text_split,download_hugging_face_embeddings
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os



load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
os.environ['PINECONE_API_KEY'] = PINECONE_API_KEY


pdf_documents = load_single_pdf("Data/The_GALE_ENCYCLO.pdf")
text_chunks = text_split(pdf_documents)
embeddings = download_hugging_face_embeddings()



pc = Pinecone(api_key=PINECONE_API_KEY) 

index_name = "medical-bot"   # Replace with your actual Pinecone index name

pc.create_index(
    name=index_name,
    dimension=384, # Replace with your model dimensions
    metric="cosine", # Replace with your model metric
    spec=ServerlessSpec(
        cloud="aws",
        region="us-east-1"
    ) 
)

docsearch = PineconeVectorStore.from_documents(
    documents=text_chunks,
    index_name=index_name,
    embedding= embeddings,
)






