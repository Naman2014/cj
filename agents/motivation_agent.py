from groq import Groq
import httpx
import os
from dotenv import load_dotenv

class MotivationAgent:
    def __init__(self):
        # Load environment variables
        load_dotenv()
        
        # Create a custom HTTP client without proxies
        http_client = httpx.Client(timeout=30.0)
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"), http_client=http_client)
        self.conversation_history = []

    def get_boost(self, query):
        # Add user query to conversation history
        self.conversation_history.append({
            "role": "user",
            "content": query
        })

        # Create completion with conversation history
        completion = self.client.chat.completions.create(
            model="gemma2-9b-it",
            messages=self.conversation_history,
            temperature=1,
            max_tokens=1024,
            top_p=1,
            stream=True,
            stop=None,
        )
        
        # Collect the streamed response
        full_response = ""
        for chunk in completion:
            content = chunk.choices[0].delta.content or ""
            full_response += content
            print(content, end="")  # Print in real-time
        
        # Add assistant's response to conversation history
        self.conversation_history.append({
            "role": "assistant",
            "content": full_response
        })
        
        return full_response