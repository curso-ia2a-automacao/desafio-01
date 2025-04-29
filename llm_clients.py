# llm_clients.py
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def call_openai(prompt: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
    )
    return response.choices[0].message.content.strip()

def call_anthropic(prompt: str) -> str:
    # Exemplo fictício
    return "Resposta do Claude baseada no prompt."

def call_cohere(prompt: str) -> str:
    return "Resposta do Cohere baseada no prompt."

def call_mistral(prompt: str) -> str:
    return "Resposta do Mistral baseada no prompt."

