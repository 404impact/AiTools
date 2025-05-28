import os
from dotenv import load_dotenv
from openai import OpenAI

def load_env():
    load_dotenv(dotenv_path=r"D:\AiTools\.env")

def get_openai_client() -> OpenAI:
    load_env()
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in environment variables")
    
    return OpenAI(api_key=api_key)

def generate_text_with_openai(prompt: str) -> str:
    client = get_openai_client()
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes web content accurately and concisely."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.5,
        max_tokens=1000
    )
    
    return response.choices[0].message.content.strip()
