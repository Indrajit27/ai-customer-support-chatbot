# AI-Powered Customer Support Chatbot

A lightweight customer-support chatbot built with **Python**, **Streamlit**, and the **OpenAI API**. It demonstrates prompt design, conversational context, API integration, and basic error handling.

## Features

- Chat-style interface built with Streamlit
- Context-aware replies using the conversation history
- Customer-support system instructions designed to discourage invented policies or order details
- Friendly error messages for API failures
- Clear-conversation control
- API key loaded from an environment variable rather than hard-coded in source

## Tech stack

- Python 3.10+
- Streamlit
- OpenAI Python SDK (Responses API)
- python-dotenv

## Run locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/Indrajit27/ai-customer-support-chatbot.git
   cd ai-customer-support-chatbot
   ```

2. **Create and activate a virtual environment** (recommended)
   ```bash
   python -m venv .venv
   ```

   Windows PowerShell:
   ```powershell
   .venv\Scripts\Activate.ps1
   ```

   macOS/Linux:
   ```bash
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure your API key**

   Copy `.env.example` to a file named `.env`, then replace the placeholder with your own OpenAI API key:

   ```env
   OPENAI_API_KEY=your_actual_api_key
   ```

   Keep `.env` private. It is excluded by `.gitignore`. Never paste API keys into source code or commit them to GitHub.

5. **Start the app**
   ```bash
   streamlit run app.py
   ```

   Streamlit will print a local URL (usually `http://localhost:8501`) to open in your browser.

## Try these prompts

- “How can I return an item?”
- “My delivery is late. What should I do?”
- “I need help changing my account email.”

This is a demonstration app. It does not have access to real customer records, order status, refunds, or a company's internal knowledge base.

## Suggested improvements

- Connect a retrieval-augmented generation (RAG) pipeline to approved support documents
- Add citations and links to source articles
- Add automated tests and response-quality evaluation
- Add authentication, rate limits, and monitoring before any production use
- Deploy to a hosting service with secrets configured securely

## Security and limitations

Do not enter real customer personal data or confidential information. Model responses may be inaccurate; verify important answers. API usage may incur charges, depending on your account and usage.
