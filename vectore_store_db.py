from dotenv import load_dotenv
from src.loader import loader_function,embedding_function,recursive_function
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from pinecone import Pinecone,ServerlessSpec
from langchain_pinecone import PineconeVectorStore


import cassio
import os

load_dotenv()


file_path = r"C:\Users\iamda\OneDrive\Desktop\Gen ai\LLMops-Project\data\Medical_book.pdf"

# load the data
loader = loader_function(file_path=file_path)
# recursive text splitter
docs = recursive_function(loader)
# now loading embedding function
hf_embedding = embedding_function()



# cassio.init(
#     token=os.getenv("token"),
#     database_id=os.getenv("End_point")
# )


# vectore_store_db = Cassandra(
#         embedding=hf_embedding,
#           session=None,
#           keyspace=None,
#           table_name="medical_rag"
#           )


# vectore_store_db.add_documents(docs)

# vectore_store_index = VectorStoreIndexWrapper(vectorstore=vectore_store_db)

# retriever = vectore_store_db.as_retriever()


# Here using the pinecone vector database

ps = Pinecone(api_key=os.getenv("Pinecone_API_KEY"))

index_name = "medical-rag-project-2"

if index_name not in ps.list_indexes().names():
    ps.create_index(
        name=index_name,
        dimension=384,
        metric="dotproduct",
        spec=ServerlessSpec(cloud="aws",region="us-east-1")
    )


vectore_store = PineconeVectorStore(index_name=index_name,embedding=hf_embedding)
vectore_store.add_documents(documents=docs)
