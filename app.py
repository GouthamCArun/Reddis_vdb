import redis
from langchain_community.vectorstores import Redis
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain_openai import OpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
 
 
os.environ["OPENAI_API_KEY"] = ""
REDIS_HOST = ""
REDIS_PORT = 18436
REDIS_USERNAME = "default"
REDIS_PASSWORD = ""
INDEX_NAME = "document_index" 
 
redis_connection = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    decode_responses=True,
    username=REDIS_USERNAME,
    password=REDIS_PASSWORD,
)
 
 
def load_document(file_path):
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    return documents
 
def split_document(documents):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = text_splitter.split_documents(documents)
    return chunks
 
 
def store_in_redis(documents):
    embeddings = OpenAIEmbeddings()
    redis_vector_store = Redis(
        redis_url=f"redis://{REDIS_USERNAME}:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}",
        index_name=INDEX_NAME,
        embedding=embeddings, 
    )
    redis_vector_store.add_documents(documents)
    print(f"Documents have been stored in Redis under the index: {INDEX_NAME}")
    return redis_vector_store
 
 
def create_qa_chain(vector_store):
    retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 2})
    qa_chain = RetrievalQA.from_chain_type(
        llm=OpenAI(temperature=0),
        retriever=retriever,
        return_source_documents=True,
    )
    return qa_chain
 
 
if __name__ == "__main__":
   
    document_path = "Hari Narayan Resume N.pdf"  
    documents = load_document(document_path)
    
    
    document_chunks = split_document(documents)
    
    
    vector_store = store_in_redis(document_chunks)
    
   
    qa_chain = create_qa_chain(vector_store)
    
   
    question = input("Enter your question: ")
   
    result = qa_chain.invoke(question) 
 
    
    answer = result['result']
    print(answer)
 
