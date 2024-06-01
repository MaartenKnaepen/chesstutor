import streamlit as st


st.set_page_config(page_title="About Chess Tutor")

st.markdown("# About Chess Tutor")
st.write("""
Chess Tutor is a project that aims to create a conversational AI assistant specialized in teaching chess basics. The project leverages the power of the Retrieval-Augmented Generation (RAG) technique and the language model capabilities of ChatGPT 3.5 to provide an interactive and informative experience for users looking to learn or improve their chess skills.
""")

st.header("Project Overview")
st.write("""
The main objective of Chess Tutor is to adapt the general knowledge of ChatGPT 3.5 to a specific domain: chess fundamentals. By combining the language model with a retrieval component, the assistant can access relevant information from a knowledge base tailored to chess basics, enabling it to provide more accurate and context-specific responses.

The project uses the RAG approach to enhance the capabilities of ChatGPT 3.5 in the following ways:

1. **Knowledge Base Creation**: A corpus of chess-related documents, including tutorials, articles, and reference materials, is compiled and processed to create a knowledge base.

2. **Vector Embeddings**: The documents in the knowledge base are converted into dense vector representations using a pre-trained embedding model, allowing efficient retrieval of relevant information.

3. **Retrieval Component**: A retrieval component, such as a vector database or similarity search engine, is used to retrieve the most relevant documents from the knowledge base based on the user's query.

4. **Language Model Integration**: The retrieved relevant documents are then provided as context to the ChatGPT 3.5 language model, which generates a response by considering both the user's query and the retrieved information.
""")

st.header("Features")
st.write("""
- **Interactive Conversation**: Users can engage in natural language conversations with the Chess Tutor assistant, asking questions or seeking explanations about various chess concepts.
- **Context-Aware Responses**: The assistant generates responses tailored to the user's query by considering the retrieved relevant information from the chess knowledge base.
- **Progressive Learning**: As the knowledge base is expanded and improved over time, the assistant's capabilities in teaching chess basics will continue to grow.
- **User-Friendly Interface**: The project includes a user-friendly web interface built with Streamlit, allowing users to interact with the Chess Tutor assistant seamlessly.
""")

st.header("Getting Started")
st.write("""
To run the Chess Tutor project locally, follow these steps:

1. Clone the repository: `git clone https://github.com/MaartenKnaepen/chesstutor`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Obtain an OpenAI API key and set it as an environment variable or in the provided configuration file.
4. Run the Streamlit app: `streamlit run ChessTutor.py`

For more detailed instructions and information about setting up the knowledge base and configuring the project, please refer to the project's README file.
""")

st.header("Contributing")
st.write("""
Contributions to the Chess Tutor project are welcome! If you have suggestions, bug reports, or would like to contribute improvements, please feel free to open an issue or submit a pull request on the project's GitHub repository.
""")
