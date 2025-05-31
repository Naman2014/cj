from google import genai
import os
from dotenv import load_dotenv

class CentralAgent:
    def __init__(self):
        # Load environment variables
        load_dotenv()
        
        # Initialize Gemini client
        self.client = genai.Client(api_key=os.getenv("GEMINI_KEY"))
        self.conversation_history = []

    def analyze_and_route(self, user_prompt, orchestrator):
        # Create a prompt to analyze the user's request
        analysis_prompt = f"""Analyze the following user request and determine which type of help is needed. 
        Respond with exactly one of these types: 'concept', 'code', 'plan', or 'motivation'.
        
        User request: {user_prompt}
        
        Respond with just the type, nothing else."""

        # Get the analysis from Gemini
        response = self.client.models.generate_content(
            model="gemini-2.0-flash",
            contents=analysis_prompt
        )
        
        # Get the query type from the response
        query_type = response.text.strip().lower()

        # Route to the appropriate agent through the orchestrator
        if query_type == "plan":
            # For plan type, we need to extract topics and duration
            plan_prompt = f"""Extract learning topics and duration from this request. 
            Format the response as a JSON with 'topics' (list) and 'duration_days' (number).
            If duration is not specified, use 7 days as default.
            
            Request: {user_prompt}
            
            Respond with just the JSON, nothing else."""

            response = self.client.models.generate_content(
                model="gemini-2.0-flash",
                contents=plan_prompt
            )

            import json
            try:
                payload = json.loads(response.text)
            except:
                # Fallback if JSON parsing fails
                payload = {"topics": [user_prompt], "duration_days": 7}
        else:
            # For other types, use the original prompt as payload
            payload = user_prompt

        # Route through orchestrator
        return orchestrator.route(query_type, payload) 