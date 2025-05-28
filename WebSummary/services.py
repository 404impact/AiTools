from bs4 import BeautifulSoup
import requests
from utils import generate_text_with_openai
from typing import Dict, Any, Optional

def parse_url(url: str) -> str:
    try:
        content = requests.get(url, timeout=10)
        content.raise_for_status()  # Raise exception for HTTP errors
        
        soup = BeautifulSoup(content.content, "html.parser")
        output = [i.text for i in soup.find_all('p')]
        scraped_text = " ".join(output)
        
        return scraped_text
    except requests.RequestException as e:
        print(f"Error fetching URL: {e}")
        return f"Error fetching URL: {e}"

def generate_summary(url: str) -> Dict[str, Any]:
    try:
        scraped_text = parse_url(url)
        
        if not scraped_text or scraped_text.startswith("Error"):
            return {"result": f"Could not summarize. {scraped_text}"}
        
        prompt = f"""
        Go through the entire content from the following text and create a summary 
        in easy-to-understand words. Stick to paragraph format. 
        Include all important information from the content.
        
        Content: {scraped_text}
        """
        
        summary = generate_text_with_openai(prompt)
        
        return {"result": summary}
    except Exception as e:
        print(f"Error generating summary: {e}")
        return {"result": f"Error generating summary: {str(e)}"}
