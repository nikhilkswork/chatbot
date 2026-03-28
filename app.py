import streamlit as st
import ollama
import os

# --- Page Config ---
st.set_page_config(page_title="Ollama Hybrid Chat", page_icon="☁️", layout="wide")

# --- Sidebar: Configuration ---
with st.sidebar:
    st.title("⚙️ Settings")
    
    # 1. Choose Mode
    mode = st.radio("Connection Mode", ["Local (Port 11434)", "Ollama Cloud"])
    
    # 2. API Key (Only shown for Cloud)
    api_key = "01fec69b11f142eb95e046f129c44d61.VFSGh_beym2VnFHOCC9jYVfl"
    if mode == "Ollama Cloud":
        api_key = st.text_input("Ollama API Key", type="password", help="Get this from ollama.com settings")
        if not api_key:
            st.warning("Please enter your API Key to use Cloud models.")
    
    # 3. Model Selection
    if mode == "Local (Port 11434)":
        try:
            local_models = [m['name'] for m in ollama.list()['models']]
            selected_model = st.selectbox("Select Local Model", local_models if local_models else ["llama3"])
        except:
            st.error("Could not connect to local Ollama. Is 'ollama serve' running?")
            selected_model = "llama3"
    else:
        # High-performance cloud models available in 2026
        selected_model = st.selectbox("Select Cloud Model", ["gpt-oss:120b", "deepseek-v3.1:671b", "qwen3-coder:480b"])

    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()

# --- Main Chat UI ---
st.title(f"💬 Chatting with {selected_model}")
st.caption(f"Currently using **{mode}** mode")

# Initialize Session State
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- Chat Logic ---
if prompt := st.chat_input("Type your message..."):
    # Display User Message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate Assistant Response
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""
        
        try:
            # Initialize Client based on Mode
            if mode == "Local (Port 11434)":
                client = ollama.Client(host='http://localhost:11434')
            else:
                if not api_key:
                    st.error("Missing API Key!")
                    st.stop()
                client = ollama.Client(
                    host='https://ollama.com',
                    headers={'Authorization': f'Bearer {api_key}'}
                )

            # Stream the response
            stream = client.chat(
                model=selected_model,
                messages=st.session_state.messages,
                stream=True,
            )

            for chunk in stream:
                content = chunk['message']['content']
                full_response += content
                response_placeholder.markdown(full_response + "▌")
            
            response_placeholder.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})

        except Exception as e:
            st.error(f"Error: {e}")