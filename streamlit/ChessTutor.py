import time
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
import base64
import os
import toml

# Configure streamlit page
st.set_page_config(
    page_title="Company Knowledge Base Chatbot"
)

# Get the OPENAI_API_KEY
openai_api_key = st.secrets["OPENAI_API_KEY"]


# Custom image for the assistant's avatar
company_logo_path = "streamlit/images/logo.png"
image_path = 'streamlit/images/wallpaper.avif'

# Function to convert image to base64
def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")


# Function to add background image using base64
def add_bg_from_base64(base64_str):
    st.markdown(
        f"""
         <style>
         .stApp {{
             background-image: url(data:image/jpg;base64,{base64_str});
             background-size: cover;
         }}
         </style>
         """,
        unsafe_allow_html=True,
    )


# Set background Image
base64_img = image_to_base64(image_path)
add_bg_from_base64(base64_img)

# Initialize the language model
llm = ChatOpenAI(model="gpt-3.5-turbo-0125")

# Load the vector store and embeddings using cache
@st.cache_resource
def load_vector_store():
    embeddings = OpenAIEmbeddings()
    return FAISS.load_local("vector_db", embeddings, allow_dangerous_deserialization=True)

@st.cache_resource
def load_embeddings():
    return OpenAIEmbeddings()

db = load_vector_store()
embeddings = load_embeddings()
retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 3})

# Define prompt templates
system_prompt = (
    "You are an assistant for question-answering tasks. "
    "Use the following pieces of retrieved context to answer "
    "the question. If you don't know the answer, say that you "
    "don't know. \n\n{context}"
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)

# Create the RAG chain
question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

# Initialize chat history
if "messages" not in st.session_state:
    # Start with first message from assistant
    st.session_state["messages"] = [
        {
            "role": "assistant",
            "content": "Hi, I am the Chess Tutor. Ask me anything about chess",
        }
    ]


for _ in range(3):
    st.markdown(""" """)

# Display chat messages from history on app rerun and put a custom avatar for the assistant, default avatar for user
for message in st.session_state.messages:
    if message["role"] == "assistant":
        with st.chat_message(message["role"], avatar=company_logo_path):
            st.text_area("", value=message["content"], height=50, max_chars=None, key=None)
    else:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Create the Chat logical sequence
# Add a base invite message in the chat box
if query := st.chat_input("Ask me anything about chess!"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": query})

    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(query)

    # Run the chain on the query and load the answer and sources to the chat message container
    with st.chat_message("assistant", avatar=company_logo_path):
        message_placeholder = st.empty()
        # Send user's question to the chain
        result = rag_chain.invoke({"input": query})
        response = result["answer"].strip()

        # Define no info messages
        no_info_message1 = "I am very sorry, I do not have any information on that topic yet."
        no_info_message2 = "I am very sorry, I am tuned to only answer questions about chess."

        if response.lower() == no_info_message1.strip().lower():
            # Display the no info message 1 without source and simulate stream of response with milliseconds delay
            full_response = ""
            for chunk in response.split():
                full_response += chunk + " "
                time.sleep(0.05)
                # Add a blinking cursor to simulate typing
                message_placeholder.text_area("", value=full_response + "▌", height=50, max_chars=None, key=None)
            message_placeholder.text_area("", value=full_response, height=50, max_chars=None, key=None)
            st.session_state.messages.append({"role": "assistant", "content": response})

        elif response.lower() == no_info_message2.strip().lower():
            # Display the no info message 2 without source and simulate stream of response with milliseconds delay
            full_response = ""
            for chunk in response.split():
                full_response += chunk + " "
                time.sleep(0.05)
                # Add a blinking cursor to simulate typing
                message_placeholder.text_area("", value=full_response + "▌", height=50, max_chars=None, key=None)
            message_placeholder.text_area("", value=full_response, height=50, max_chars=None, key=None)
            st.session_state.messages.append({"role": "assistant", "content": response})

        else:
            # Display the answer without sources and simulate stream of response with milliseconds delay
            full_response = ""
            for chunk in response.split():
                full_response += chunk + " "
                time.sleep(0.05)
                # Add a blinking cursor to simulate typing
                message_placeholder.text_area("", value=full_response + "▌", height=50, max_chars=None, key=None)
            message_placeholder.text_area("", value=full_response, height=50, max_chars=None, key=None)
            st.session_state.messages.append({"role": "assistant", "content": response})