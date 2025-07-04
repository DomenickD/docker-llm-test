# docker-llm-test

A self-hosted ChatGPT-style application powered by a local LLM (Meta Llama 3.1, 8B) using llama.cpp, wrapped with FastAPI, and served through a Streamlit frontend. Everything runs in Docker containers orchestrated by Docker Compose.

---

## 🚀 Features

- **llama-server**: Builds and runs [llama.cpp](https://github.com/ggerganov/llama.cpp) with a GGUF model downloaded at build time.  
- **backend**: A FastAPI proxy that forwards chat requests to the llama-server.  
- **frontend**: A Streamlit chat UI that mimics ChatGPT’s interface.  
- **One-command launch**: `docker-compose up --build` to build and start all services.

---

## 📋 Prerequisites

- Docker & Docker Compose installed on your machine.  
- Internet access to download the GGUF model from LM Studio during the build.

---

## 🗂 Directory Structure

```text
docker-llm-test/
├── llama-server/      # llama.cpp build + model download
│   └── Dockerfile     # builds llama.cpp and downloads the .gguf
│
├── backend/           # FastAPI wrapper
│   ├── Dockerfile     # builds FastAPI service
│   ├── requirements.txt
│   └── main.py        # chat endpoint
│
├── frontend/          # Streamlit chat UI
│   ├── Dockerfile     # builds Streamlit service
│   ├── requirements.txt
│   └── app.py         # chat interface
│
├── docker-compose.yml # orchestrates all three services
├── .gitignore         # ignores .gguf, build artifacts, etc.
└── README.md          # this file
```

## ⚙️ Configuration

- **Model URL**: By default, the `llama-server` Dockerfile pulls the model from:
```dockerfile
  ARG MODEL_URL="https://model.lmstudio.ai/download/cha9ro/Meta-Llama-3.1-8B-Instruct-Q4_K_S-GGUF"
```

## 🛠️ Build & Run

1. **Clone the repo**  
   ```bash
   git clone https://github.com/your-org/docker-llm-test.git
   cd docker-llm-test
   ```

2. **Build & start all services**  
   ```bash
   docker-compose up --build
   ```
   - This will:  
     - Build the **llama-server** image (compiles llama.cpp & downloads the model)  
     - Build the **backend** image  
     - Build the **frontend** image  
     - Start containers on ports:  
       - `8000`: llama-server  
       - `8001`: FastAPI backend  
       - `8501`: Streamlit UI  

3. **Visit the chat UI**  
   Open your browser to `http://localhost:8501` and start chatting.

---

## 🔄 Overriding the Model URL

If you want to use a different GGUF model:

```bash
# Rebuild only the llama-server with a new URL
docker-compose build \
  --build-arg MODEL_URL="https://model.lmstudio.ai/download/cha9ro/Your-Other-Model-GGUF" \
  llama

docker-compose up
```

---

## 🧩 How It Works

1. **Streamlit UI** sends a POST to the FastAPI `/chat` endpoint.  
2. **FastAPI** wraps your prompt into the llama.cpp REST API format and forwards it to the llama-server.  
3. **llama-server** (built from llama.cpp) returns token-stream JSON.  
4. **FastAPI** relays it back to Streamlit.  
5. **Streamlit** displays it in the chat interface.

---

## 🤝 Contributing

1. Fork this repo  
2. Create a branch (`git checkout -b feature/YourFeature`)  
3. Commit your changes (`git commit -m "Add YourFeature"`)  
4. Push (`git push origin feature/YourFeature`)  
5. Open a Pull Request  
