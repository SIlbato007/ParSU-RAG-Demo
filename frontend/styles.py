import streamlit as st

def apply_custom_styles():
    """Applies custom CSS styles."""
    st.markdown(
        """
        <style>
        [data-testid="stAppViewContainer"] {
            background-color: #ebf6f7 !important;
            color: #111827;
        }
        [data-testid="stquery"] {
            background-color: #000080 !important;
        }
        [data-testid="stChatMessageContainer"] {
            max-height: calc(100vh - 200px);
            overflow-y: auto;
            scroll-behavior: smooth;
            border: 1px solid red;
        }
        .stChatMessage[data-testid="stChatMessage-user"] {
            background-color: #fd7e14 !important;
            border-radius: 25% !important;
            padding: 1.5rem 0 !important;
            border-bottom: 1px solid rgba(0, 0, 0, 0.05);
            margin-bottom: 0 !important;
        }
        .stChatMessage[data-testid="stChatMessage-assistant"] {
            background-color: #f3f4f6 !important;
            border-bottom: 1px solid rgba(0, 0, 0, 0.05);
        }
        .stChatMessage p, .stChatMessage span, .stChatMessage div {
            color: #374151 !important;
            font-size: 1rem !important;
            line-height: 1.5 !important;
        }
        [data-testid="stSidebar"] {
            background-color: #fd7e14 !important;
            color: #000000 !important;
            padding: 1rem;
        }
        [data-testid="stSidebar"] button {
            background-color: #fd7e14 !important;
            color: #000000 !important;
            border: 1px solid #000000 !important;
            border-radius: 4px !important;
            margin-bottom: 0.5rem !important;
            text-align: left !important;
            transition: background-color 0.2s !important;
            width: 100%;
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
        }
        [data-testid="stSidebar"] button:hover {
            background-color: #001b4c !important;
            color: white !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
