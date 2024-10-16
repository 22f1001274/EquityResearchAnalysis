import os 
from dotenv import load_dotenv

load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv('API_KEY')

import streamlit as st
import embedder
import langchain
from langchain_community.llms import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.chains.qa_with_sources.loading import load_qa_with_sources_chain

st.header("Data Analyst Tool 🛠️")
st.sidebar.title("Add your url's")

urls = []
for i in range(3):
    url=st.sidebar.text_input(f"URL{i+1}")
    urls.append(url)


load_button = st.sidebar.button("Load URLs")

if load_button and urls:
    st.session_state.vector_index = embedder.generate_embeddings([url for url in urls])

query = st.text_input("Ask any question in the context!")
ans_button = st.button("Answer")

if query and ans_button:
    if 'vector_index' in st.session_state:
        llm = OpenAI(temperature=0.9, max_tokens=500)
        chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=st.session_state.vector_index.as_retriever())
        langchain.debug = True
        response = chain.invoke({"question": query}, return_only_outputs=True)
        st.write(response['answer'])
        st.write(response['sources'])


        

