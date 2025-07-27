import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import JSONLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import create_history_aware_retriever
from langchain_core.prompts import MessagesPlaceholder
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
import json
from pathlib import Path
from pprint import pprint



st.title("💬 Laboratory Company Chatbot")
st.caption("Chatbot that answers questions about UV detector catalog ")

# Sidebar for API key input
with st.sidebar:
    OPENAI_API_KEY = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View the source code](https://github.com/franconti/context_aware_chatbot)"

# Check for API key
if not OPENAI_API_KEY:
    st.info("Please add your OpenAI API key to continue.")
    st.stop()

# Set the OpenAI API key
#import os 
#os.environ['OPENAI_API_KEY'] = openai_api_key

# Initialize the LangChain components
llm = ChatOpenAI(openai_api_key= OPENAI_API_KEY, model_name="gpt-3.5-turbo")

# Load and process the data
loader = JSONLoader(
    file_path='UVdetectors.json',
    jq_schema='.UVDetectors.models[]',
    text_content=False)
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter()
documents = text_splitter.split_documents(docs)

embeddings = OpenAIEmbeddings(openai_api_key= OPENAI_API_KEY)
vector = FAISS.from_documents(documents, embeddings)
retriever = vector.as_retriever()

# Create the retrieval chain
retrieval_chain_prompt = ChatPromptTemplate.from_messages([
    MessagesPlaceholder(variable_name="chat_history"),
    ("user", "{input}"),
    ("user", "Given the above conversation, generate a search query to look up in order to get information relevant to the conversation")
])
retriever_chain = create_history_aware_retriever(llm, retriever, retrieval_chain_prompt)

# Create the document chain
document_chain_prompt = ChatPromptTemplate.from_messages([
    ("system",
     "This is a chatbot for BiologyArte, a laboratory supplies company.\
      The chatbot's goal is to provide information and assistance to potential and existing BiologyArte customers.. \
      The chatbot should decline to answer any question not related to the company goal. \
      The chatbot should be friendly, polite, and helpful. \
      The chatbot should refer the user to the official website or a human representative if it cannot answer the question or handle the request. \
      Answer the user's questions based on the below context:\n\n{context}"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("user", "{input}"),
])
document_chain = create_stuff_documents_chain(llm, document_chain_prompt)

# Combine both chains
combined_chain = create_retrieval_chain(retriever_chain, document_chain)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

# Display chat messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Handle user input
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = combined_chain.invoke({"input": prompt, "chat_history": st.session_state.messages})
    msg = response["answer"]
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
