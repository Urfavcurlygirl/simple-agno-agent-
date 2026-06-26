# Simple Agno Agent

A simple AI agent built using [Agno](https://github.com/agno-ai/agno) (formerly Phidata) and FastAPI. The agent leverages the Groq API for fast LLM inference and SQLite for maintaining session history and context.

## Features

- **Agno Agent:** An intelligent agent configured to remember context and chat history.
- **Groq Integration:** Uses the blazing fast `llama-3.3-70b-versatile` model via Groq.
- **SQLite Database:** Stores conversation sessions locally to maintain context across requests.
- **FastAPI Backend:** Provides a simple REST API to interact with the agent.

## Prerequisites

- Python 3.9+
- [uv](https://github.com/astral-sh/uv) (for dependency management)
- Groq API Key

## Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Urfavcurlygirl/simple-agno-agent-.git
   cd simple-agno-agent-
   ```

2. **Set up environment variables:**
   Create a `.env` file in the root directory and add your Groq API key:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

3. **Install dependencies:**
   ```bash
   uv venv
   # Activate the virtual environment (.venv\Scripts\activate on Windows or source .venv/bin/activate on Mac/Linux)
   uv add agno groq fastapi uvicorn python-dotenv sqlalchemy
   ```

## Running the Application

To start the FastAPI development server, run:
```bash
uv run uvicorn main:router --reload
```
The server will start on `http://127.0.0.1:8000`.

## API Usage

You can interact with the agent via the `/run` endpoint.

**Endpoint:** `POST /run`

**Request Body:**
```json
{
  "message": "Hello, my name is Hana"
}
```

**Response:**
```json
{
  "response": "Hello Hana! How can I help you today?"
}
```

## Project Structure

- `main.py`: Contains the Agno agent configuration and the FastAPI router.
- `sessions.db`: (Auto-generated) SQLite database to store chat histories.
- `.env`: Environment variables configuration (should not be tracked by git).

## License

MIT License
