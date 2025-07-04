from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()


class ChatRequest(BaseModel):
    prompt: str
    n_predict: int = 128
    temperature: float = 0.7


@app.post("/chat")
def chat(req: ChatRequest):
    llama_payload = {
        "prompt": req.prompt,
        "n_predict": req.n_predict,
        "temperature": req.temperature,
        "stop": ["<|eot_id|>"],
    }
    resp = requests.post(f"{app.state.llm_url}/completion", json=llama_payload)
    resp.raise_for_status()
    return resp.json()


@app.on_event("startup")
def configure_llm_url():
    import os

    app.state.llm_url = os.getenv("LLM_URL", "http://localhost:8000")
