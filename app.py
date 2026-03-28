import streamlit as st
import ollama
import base64
from gtts import gTTS
from streamlit_mic_recorder import mic_recorder
import io

# --- Page Config ---
st.set_page_config(page_title="Ollama Voice Chat", page_icon="🎙️")

def text_to_speech(text):
    """Converts text to an audio file and returns base64 string for auto-play."""
    tts = gTTS(text=text, lang='en')
    fp = io.BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    b64 = base64.b64encode(fp.read()).decode()
    # HTML5 auto-play hack for Streamlit
    return f'<audio autoplay="true" src="data:audio/mp3;base64,{b64}">'

# --- Sidebar ---
with st.sidebar:
    st.title("⚙️ Settings")
    mode = st.radio("Mode", ["Local (Port 11434)", "Ollama Cloud"])
    
    # Model Selection Logic
    if mode == "Local (Port 11434)":
        try:
            models = [m['name'] for m in ollama.list()['models']]
            selected_model = st.selectbox("Local Model", models if models else ["llama3"])
        except:
            st.error("Ollama not found.")
            selected_model = "llama3"
    else:
        selected_model = st.selectbox("Cloud Model", ["gpt-oss:120b", "deepseek-v3.1:671b"])

# --- Main UI ---
st.title("🎙️ Ollama Voice Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- Voice Input Section ---
st.write("Click to Speak:")
audio_input = mic_recorder(start_prompt="⏺️ Start Recording", stop_prompt="⏹️ Stop & Send", key='recorder')

# Process Input (Voice or Text)
user_query = None
if audio_input:
    # Note: In a production app, you'd send audio_input['bytes'] to a Whisper API/Model.
    # For this snippet, we'll assume the user typed or provide a placeholder for STT.
    st.info("Audio captured! (To fully automate STT, integrate OpenAI Whisper or SpeechRecognition library here).")

# Standard text input as fallback
if prompt := st.chat_input("Or type here..."):
    user_query = prompt

if user_query:
    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.markdown(user_query)

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""
        
        # Initialize Ollama Client
        client = ollama.Client(host='http://localhost:11434' if mode == "Local (Port 11434)" else 'https://ollama.com')
        
        stream = client.chat(model=selected_model, messages=st.session_state.messages, stream=True)
        
        for chunk in stream:
            full_response += chunk['message']['content']
            response_placeholder.markdown(full_response + "▌")
        
        response_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})

        # --- Text to Speech Playback ---
        audio_html = text_to_speech(full_response)
        st.components.v1.html(audio_html, height=0)