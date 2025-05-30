from agents.orchestrator import OrchestratorAgent
from dotenv import load_dotenv
load_dotenv()

def main():
    orchestrator = OrchestratorAgent()

    # Example Usage
    print("\n--- Concept Explanation ---")
    print(orchestrator.route("concept", "Dynamic Programming"))

    print("\n--- Code Assistance ---")
    print(orchestrator.route("code", "Write a function to detect a cycle in a directed graph."))

    print("\n--- Study Plan ---")
    print(orchestrator.route("plan", {"topics": ["Arrays", "Trees", "Graphs"], "duration_days": 5}))

    print("\n--- Motivation ---")
    print(orchestrator.route("motivation", None))

if __name__ == "__main__":
    main()