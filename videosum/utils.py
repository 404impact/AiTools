import os
from dotenv import load_dotenv
from openai import OpenAI

def load_env():
    """Load environment variables from .env file."""
    load_dotenv(dotenv_path=r"D:\AiTools\.env")

def get_openai_client() -> OpenAI:
    """Get configured OpenAI client."""
    load_env()
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in environment variables")
    
    return OpenAI(api_key=api_key)

def get_assemblyai_key() -> str:
    """Get AssemblyAI API key from environment variables."""
    load_env()
    api_key = os.getenv("ASSEMBLYAI_API_KEY")
    
    if not api_key:
        raise ValueError("ASSEMBLYAI_API_KEY not found in environment variables")
    
    return api_key

def generate_text_with_openai(prompt: str) -> str:
    """Generate text using OpenAI's GPT-4o model.
    
    Args:
        prompt: The prompt to send to the model
        
    Returns:
        Generated text response
    """
    client = get_openai_client()
    
    response = client.chat.completions.create(
        model="gpt-4o",  # Using GPT-4o model
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes video content accurately and concisely."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.5,
        max_tokens=1000
    )
    
    return response.choices[0].message.content.strip()
