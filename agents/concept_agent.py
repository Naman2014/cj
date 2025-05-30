from together import Together

class ConceptAgent:
    def __init__(self):
        self.client = Together()

    def explain_concept(self, topic):
        prompt = f"Explain the concept of {topic} in a simple, beginner-friendly way with examples."
        response = self.client.chat.completions.create(
            model="Qwen/Qwen3-235B-A22B-fp8-tput",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        return response.choices[0].message.content