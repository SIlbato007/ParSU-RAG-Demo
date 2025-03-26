import streamlit as st
from src.backend_config import PSUChatBackend

def initialize_backend():
    """Initializes the backend system."""
    if 'backend' not in st.session_state:
        st.session_state.backend = PSUChatBackend()
        with st.spinner("Initializing system. Please Wait..."):
            success, message = st.session_state.backend.initialize_system()
            st.session_state.initialized = success
            if not success:
                st.session_state.init_error = message

def initialize_session_state():
    """Initializes session state variables."""
    if 'messages' not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hello! I'm the ParSU Citicharbot. I can help you with information about Partido State University services and transactions. What would you like to know?"}
        ]

    if 'clicked_example' not in st.session_state:
        st.session_state.clicked_example = None
