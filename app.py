# Entry point for Render deployment (Streamlit)
import streamlit as st
from agents.orchestrator import OrchestratorAgent
import time

# Set page config
st.set_page_config(
    page_title="Coding Ninjas Learning Assistant",
    page_icon="👨‍💻",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main {
        background-color: #f5f5f5;
    }
    .stTextInput>div>div>input {
        background-color: #ffffff;
    }
    .title {
        color: #2c3e50;
        font-size: 2.5em;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .subtitle {
        color: #34495e;
        font-size: 1.2em;
        margin-bottom: 30px;
    }
    .user-message {
        background-color: #2b313e;
        color: white;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    .assistant-message {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'orchestrator' not in st.session_state:
    st.session_state.orchestrator = OrchestratorAgent()
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

def display_chat_history():
    for message in st.session_state.chat_history:
        if message["role"] == "user":
            st.markdown(f'<div class="user-message"><strong>You:</strong> {message["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="assistant-message"><strong>Assistant:</strong> {message["content"]}</div>', unsafe_allow_html=True)

def main():
    # Header
    st.markdown('<div class="title">Coding Ninjas Learning Assistant</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Your AI-powered programming learning companion</div>', unsafe_allow_html=True)

    # Sidebar
    with st.sidebar:
        st.markdown("### What I can help you with:")
        st.markdown("""
        - 📚 Understanding programming concepts
        - 💻 Getting help with code
        - 📅 Creating study plans
        - 🚀 Providing motivation
        """)
        
        st.markdown("### How to use:")
        st.markdown("""
        1. Type your question or request
        2. I'll analyze and route it to the appropriate helper
        3. Get detailed, streaming responses
        """)

    # Main chat interface
    st.markdown("### Chat with me")
    
    # Display chat history
    display_chat_history()
    
    # Input area
    with st.form(key='chat_form', clear_on_submit=True):
        user_input = st.text_input("Type your message here:", key="user_input")
        submit_button = st.form_submit_button(label='Send')
    
    if submit_button and user_input:
        # Add user message to chat history
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        
        # Process the request
        try:
            # Get response from orchestrator
            response = st.session_state.orchestrator.process_request(user_input)
            
            # Add assistant response to chat history
            st.session_state.chat_history.append({"role": "assistant", "content": response})
            
            # Rerun to update the chat history display
            st.rerun()
            
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            st.info("Please try again or refresh the page.")

if __name__ == "__main__":
    main() 