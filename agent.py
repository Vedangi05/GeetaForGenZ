import os
from openai import OpenAI
from dotenv import load_dotenv

class AIAgent:
    def __init__(self):
        # Load environment variables
        load_dotenv()
        api_key = os.getenv("OPENAI_API_KEY")
        base_url="https://api.ai.it.ufl.edu"

        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in .env file")

        # Initialize OpenAI client
        self.client = OpenAI(api_key=api_key,base_url=base_url)
        

    def ask(self, prompt: str) -> str:
        """Send a prompt to OpenAI and get a response"""
        response = self.client.chat.completions.create(
            model="gpt-oss-120b",   # Use GPT-4o-mini for efficiency
            # base_url="https://api.ai.it.ufl.edu",
            messages=[
            
                # {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "system", "content": "You are a rude comedian ho loves to insult people and make fun of them. You never talk straight. You always make jokes and puns. You never apologize."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
