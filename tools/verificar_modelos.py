from google import genai
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(".") / ".env")
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

print("Perguntando ao Google quais modelos estão disponíveis...")

try:
    for m in client.models.list():
        if 'generateContent' in m.supported_actions:
            print(f"✅ Disponível: {m.name}")
except Exception as e:
    print(f"❌ Erro ao listar: {e}")