import os

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

st.set_page_config(
    page_title="AI Customer Support Chatbot",
    page_icon="💬",
    layout="centered",
)

SYSTEM_PROMPT = """
You are a helpful, professional customer support assistant.
- Be friendly, clear, and concise.
- Ask a clarifying question when the request is ambiguous.
- Do not invent company policies, order details, refunds, or delivery updates.
- If you do not have enough information to resolve an issue, explain that clearly
  and recommend contacting a human support representative.
- Never ask users to share passwords, full payment card numbers, or other secrets.
"""

st.title("💬 AI-Powered Customer Support")
st.caption("A demo support assistant powered by the OpenAI API.")

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error(
        "OpenAI API key not found. Add OPENAI_API_KEY to your local .env file "
        "and restart the app. See the README for setup instructions."
    )
    st.stop()

client = OpenAI(api_key=api_key)

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.subheader("About this demo")
    st.write(
        "Ask a general customer-support question. This demo does not connect "
        "to real orders, customer accounts, or company systems."
    )
    if st.button("Clear conversation", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("How can I help you today?")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = client.responses.create(
                    model="gpt-4.1-mini",
                    instructions=SYSTEM_PROMPT,
                    input=st.session_state.messages,
                    max_output_tokens=500,
                )
                answer = response.output_text.strip()
                if not answer:
                    answer = (
                        "I couldn't generate a response just now. "
                        "Please try asking in a different way."
                    )
                st.markdown(answer)
                st.session_state.messages.append(
                    {"role": "assistant", "content": answer}
                )
            except Exception as exc:
                st.error(
                    "Sorry, I couldn't reach the AI service. Check your API key "
                    "and connection, then try again."
                )
                # Keep technical details out of the user-facing chat.
                st.caption(f"Technical detail: {type(exc).__name__}")
