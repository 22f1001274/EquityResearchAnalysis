# split into chunks 
# create vector db
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

def load(urls):
    url_loader = UnstructuredURLLoader(urls=[url for url in urls])
    docs = url_loader.load()
    return docs

def splitter(data):
    r_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 200
    )
    return r_splitter.split_documents(data)

def generate_embeddings(urls):
    # generate documents from url
    docs = load(urls)
    # create chunks
    doc_chunks = splitter(docs)
    # create embeddings and store it to vector database
    embeddings = OpenAIEmbeddings()
    vectorindex_openai=FAISS.from_documents(doc_chunks, embeddings)
    return vectorindex_openai



    
