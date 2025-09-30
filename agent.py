import os
from openai import OpenAI
from dotenv import load_dotenv
from knowledge_base import KnowledgeBase

class StoryAgent:
    def __init__(self, personality: str = None):
        load_dotenv()
        api_key = os.getenv("OPENAI_API_KEY")
        base_url = "https://api.ai.it.ufl.edu"

        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in .env file")

        self.client = OpenAI(api_key=api_key, base_url=base_url)
        self.personality = personality or "You are a creative storyteller. Make stories relatable to Indian youngsters."
        self.kb = KnowledgeBase()

    def create_story(self, quote: str) -> str:
        """Create a story based on a Bhagwat Gita quote/shloka"""
        context = self.kb.get_context(quote)
        prompt = (
            f"Use the following Bhagwat Gita reference and meaning:\n{context}\n\n"
            f"Create a story for an Indian youngster that relates to this quote:\n'{quote}'\n"
            "Make it fun, relatable, and modern. Use cultural references if suitable."
        )
        response = self.client.chat.completions.create(
            model="gpt-oss-120b",
            messages=[
                {"role": "system", "content": self.personality},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
