import streamlit as st
import requests

st.title("🔮 LLM Chat")

if "history" not in st.session_state:
    st.session_state.history = []

input_text = st.text_input("You:", key="user_input")
if st.button("Send"):
    if input_text:
        st.session_state.history.append({"role": "user", "text": input_text})
        payload = {"prompt": input_text}
        r = requests.post("http://backend:8001/chat", json=payload)
        r.raise_for_status()
        assistant = r.json().get("content", "<no content>")
        st.session_state.history.append({"role": "assistant", "text": assistant})
        st.session_state.user_input = ""

for msg in st.session_state.history:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['text']}")
    else:
        st.markdown(f"**LLM:** {msg['text']}")
