from groq import Groq
import httpx

class CodeAgent:
    def __init__(self):
        # Create a custom HTTP client without proxies
        http_client = httpx.Client(timeout=30.0)
        self.client = Groq(http_client=http_client)
        self.conversation_history = []

    def get_code_help(self, query):
        # Add user query to conversation history
        self.conversation_history.append({
            "role": "user",
            "content": query
        })

        # Create completion with conversation history
        completion = self.client.chat.completions.create(
            model="deepseek-r1-distill-llama-70b",
            messages=self.conversation_history,
            temperature=0.6,
            max_tokens=4096,
            top_p=0.95,
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