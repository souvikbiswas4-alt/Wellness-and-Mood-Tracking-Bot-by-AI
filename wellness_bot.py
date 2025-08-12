import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class WellnessBot:
    """
    A bot that uses Generative AI to provide wellness support.
    """
    def __init__(self):
        self.api_key = os.getenv("GOOGLE_API_KEY")
        if not self.api_key:
            raise ValueError("GOOGLE_API_KEY not found in environment variables.")
        
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('gemini-pro')

    def _generate_content(self, prompt: str) -> str:
        """Helper function to generate content from a prompt."""
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"An error occurred: {e}. Please check your API key and network connection."

    def generate_coping_strategy(self, mood: str) -> str:
        """
        Generates a personalized coping strategy based on the user's mood.
        """
        prompt = (
            "You are a supportive and empathetic wellness assistant. "
            f"A user is feeling '{mood}'. Provide one short, practical, and safe coping strategy. "
            "Frame your response as a gentle suggestion. Do not give medical advice. "
            "Start directly with the suggestion."
        )
        return self._generate_content(prompt)

    def generate_calming_exercise(self) -> str:
        """
        Generates a short, text-based calming exercise or meditation.
        """
        prompt = (
            "You are a calm and soothing meditation guide. "
            "Generate a short, text-based calming exercise or a simple breathing meditation script "
            "that a user can follow right now. The exercise should be 3-4 paragraphs long."
        )
        return self._generate_content(prompt)

    def generate_journal_prompt(self) -> str:
        """
        Generates a thoughtful journaling prompt.
        """
        prompt = (
            "You are a thoughtful and empathetic journaling assistant. "
            "Generate one insightful and open-ended journal prompt to help a user reflect on their feelings or experiences. "
            "The prompt should encourage self-exploration without being intrusive."
        )
        return self._generate_content(prompt)