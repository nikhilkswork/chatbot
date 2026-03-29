```markdown
# 🎙️ Ollama Voice Assistant

A high-performance, voice-integrated chatbot built with **Streamlit** and **Ollama**. This application allows you to chat with local LLMs on your Mac or connect to massive models via the Ollama Cloud.

---

## 🚀 Features

* **Voice-First Interface:** Record your prompts directly in the browser using the `streamlit-mic-recorder`.
* **AI Speech Back:** The assistant responds with voice using Google Text-to-Speech (gTTS).
* **Hybrid Connectivity:**
    * **Local Mode:** Hits `localhost:11434` for private, offline inference.
    * **Cloud Mode:** Connects to `ollama.com` for heavy-duty models (120B+ parameters).
* **Real-time Streaming:** Watch the AI "think" and type in real-time using Streamlit's streaming capabilities.
* **Session Management:** Keeps track of chat history and allows clearing with a single click.

---

## 🛠️ Tech Stack

| Component | Technology |
| :--- | :--- |
| **Frontend** | [Streamlit](https://streamlit.io/) |
| **Inference Engine** | [Ollama](https://ollama.com/) |
| **Voice Recording** | `streamlit-mic-recorder` |
| **Text-to-Speech** | `gTTS` (Google TTS) |
| **Language** | Python 3.12+ |

---

## 📦 Installation & Setup

### 1. Prerequisites
Ensure you have [Ollama](https://ollama.com/download) installed and running on your system.

### 2. Clone & Navigate
```zsh
git clone [https://github.com/YOUR_USERNAME/your-repo-name.git](https://github.com/YOUR_USERNAME/your-repo-name.git)
cd "new project01"
```

### 3. Environment Setup
It is recommended to use a virtual environment to avoid `pip` command conflicts:
```zsh
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install Dependencies
```zsh
pip install -r requirements.txt
```

---

## 🚦 How to Run

1.  **Start your local Ollama server:**
    ```zsh
    ollama serve
    ```
2.  **Pull your preferred model (e.g., Llama 3):**
    ```zsh
    ollama pull llama3
    ```
3.  **Launch the Web App:**
    ```zsh
    streamlit run app.py
    ```

---

## ☁️ Using Ollama Cloud

To use the Cloud functionality:
1.  Go to [ollama.com](https://ollama.com) and generate an **API Key**.
2.  In the app sidebar, switch the toggle to **Ollama Cloud**.
3.  Enter your API Key to unlock models like `gpt-oss:120b` or `deepseek-v3.1`.

---

## 📂 Project Structure

```text
.
├── app.py              # Main Streamlit logic
├── requirements.txt    # Library dependencies
├── README.md           # Documentation
└── .gitignore          # Prevents pushing .venv and cache to GitHub
```

## 📝 License
Distributed under the MIT License. See `LICENSE` for more information.

---
**Developed by [Nikhil](https://github.com/YOUR_USERNAME)**
```

**Next step:** Since your documentation is ready, would you like me to generate a clean `.gitignore` file so you don't accidentally upload 100MB of virtual environment folders to your GitHub?
