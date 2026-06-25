import os
from agno.agent import Agent
from agno.models.groq import Groq  # On remplace Gemini par Groq
from dotenv import load_dotenv
from agno.tools.yfinance import YFinanceTools


# 1. Charger les clés du fichier .env
load_dotenv()

# 2. Créer l'agent
agent = Agent(
    # Ici, c'est beaucoup plus simple que dans la vidéo !
    # Groq n'a pas besoin de 'vertexai', 'project_id' ou 'location'
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions = ["use tables to display data",
    "only include the table in your response no other text ",
    ],
    # 2. Attach the skill to the agent here:
    tools=[YFinanceTools(enable_stock_price=True)],
    markdown=True
)

# 3. Poser la question
agent.print_response("What is the stock price of Apple and microsoft?", stream=True)