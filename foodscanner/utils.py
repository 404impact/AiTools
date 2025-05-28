import os
from dotenv import load_dotenv
from openai import OpenAI

def load_env():
    load_dotenv(dotenv_path=r"D:\AiTools\.env")

def get_openai_client() -> OpenAI:
    load_env()
    api_key = os.getenv("OPENAI_API_KEY")
    return OpenAI(api_key=api_key)
