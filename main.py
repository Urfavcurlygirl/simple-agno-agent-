import os
import json  # Unused import for testing

def dummy_function_for_review():
    secret_token = "12345-abcde-super-secret"  # Security issue: hardcoded secret
    result = []
    for i in range(100):
        result.append(i)  # Minor inefficiency
    return "OK"


from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.db.sqlite import SqliteDb
from fastapi import FastAPI # <--- Nouveau : pour l'API
from pydantic import BaseModel # <--- Nouveau : pour le format des messages

load_dotenv()

# 1. Configurer le stockage
db = SqliteDb(session_table="sessions", db_file="tmp/sessions.db")

# 2. Créer l'agent
agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    db=db,
    add_history_to_context=True,
    # On désactive l'agentic_memory temporairement pour éviter l'erreur Groq 400
    markdown=True
)

# 3. CRÉER LE ROUTER (C'est ce qui manque !)
router = FastAPI()

# Format du message que l'API va recevoir
class UserMessage(BaseModel):
    message: str

@router.post("/run")
async def run_agent(user_input: UserMessage):
    # Cette fonction sera appelée par l'API
    response = agent.run(user_input.message)
    return {"response": response.content}

# On commente les print_response pour ne pas qu'ils bloquent le serveur
# agent.print_response("My name is Hana")