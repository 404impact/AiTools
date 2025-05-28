from bs4 import BeautifulSoup
import requests
import os
# from openai import OpenAI
from utils import get_openai_client

def parse_barcode(barcode: str) -> str:
    """Fetch product info from OpenFoodFacts and return scraped text."""
    url = f"https://world.openfoodfacts.org/product/{barcode}"
    content = requests.get(url)
    soup = BeautifulSoup(content.content, "html.parser")
    output = [i.text for i in soup.find_all('body')]
    return " ".join(output)

def analyze_nutrition(product_info: str) -> str:
    """Send product info to OpenAI and return nutritional analysis."""
    client = get_openai_client()
    prompt = f"""
"Review the provided product information carefully, and feel free to supplement your analysis with your existing knowledge base. Then, based on the details you find, do the following:

Label the food product as 'healthy' or 'unhealthy.'

Provide a concise explanation for your decision, including any nutritional values mentioned. If a nutri-score (ranging from A to E) is provided, incorporate it into your analysis and justify how it influences your assessment.

Include the food product's name in your response.

If nutritional details are available:

Present the original nutritional chart as provided.

Provide a detailed nutritional analysis, converting the nutritional values proportionally according to the product's total weight (if mentioned) for better clarity along with the original nutritional chart.

Identify any harmful ingredients present in the product and explain their potential health impacts. Base this decision on the quantity of ingredients relative to the product's total weight, as specified in the nutrition chart. Avoid labeling a product as unhealthy solely due to the presence of an ingredient unless its quantity is significant. Also provide the result in more practical sense, for example if a product has 35g of sugar per 250ml serving, then how much sugar the person is consuming in real life like how much spoon of sugar, etc. This should be done based on the nutritional chart.

If the product has been banned in certain countries or conflicted with any country's laws, mention this along with the relevant details. Use your existing knowledge to identify this information if it's not provided.
                  
Use WHO standards to base your decision.

If no relevant product details are found, simply respond with 'no information available.'
    food product information: {product_info}
    """
    # Example OpenAI call (adjust as needed):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip() if response.choices else "No analysis returned."
