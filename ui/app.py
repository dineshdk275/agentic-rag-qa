# ui/app.py

import streamlit as st

def launch_ui():
    st.set_page_config(page_title="Agentic RAG QA Bot", layout="wide")
    st.title("📄 Agentic RAG Chatbot for Multi-Format QA")

    query = st.text_input("Ask a question based on your document:")
    if query:
        # Dummy response for now
        st.success(f"Answering: {query}")
