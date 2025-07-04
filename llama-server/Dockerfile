# llama-server/Dockerfile
FROM debian:stable-slim

# 1. Install build tools, CMake, Git, curl, Python (if you need it later)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    cmake \
    git \
    curl \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# 2. Clone & build llama.cpp
WORKDIR /app
RUN git clone https://github.com/ggerganov/llama.cpp.git
WORKDIR /app/llama.cpp
RUN cmake -B build -S . -DCMAKE_BUILD_TYPE=Release -DLLAMA_CURL=OFF \
    && cmake --build build -- -j$(nproc)

# 3. Download your GGUF model from LM Studio
WORKDIR /app
ARG MODEL_URL="https://model.lmstudio.ai/download/cha9ro/Meta-Llama-3.1-8B-Instruct-Q4_K_S-GGUF"
RUN curl -L "$MODEL_URL" -o Meta-Llama-3.1-8B-Instruct-Q4_K_S.gguf

# 4. Expose port & launch llama-server
EXPOSE 8000
CMD ["/app/llama.cpp/build/bin/llama-server", \
    "-m", "Meta-Llama-3.1-8B-Instruct-Q4_K_S.gguf", \
    "--host", "0.0.0.0", \
    "--port", "8000", \
    "-c", "2048"]



#     # Build (uses the default MODEL_URL)
# docker build -t llama-server:latest ./llama-server

# # Or override the URL if needed:
# docker build \
#   --build-arg MODEL_URL="https://model.lmstudio.ai/download/cha9ro/Your-New-Model.gguf" \
#   -t llama-server:latest \
#   ./llama-server
