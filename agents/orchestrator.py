from agents.concept_agent import ConceptAgent
from .code_agent import CodeAgent
from agents.planner_agent import PlannerAgent
from .motivation_agent import MotivationAgent

class OrchestratorAgent:
    def __init__(self):
        self.concept_agent = ConceptAgent()
        self.code_agent = CodeAgent()
        self.planner_agent = PlannerAgent()
        self.motivation_agent = MotivationAgent()

    def route(self, query_type, payload):
        if query_type == "concept":
            return self.concept_agent.explain_concept(payload)
        elif query_type == "code":
            return self.code_agent.get_code_help(payload)
        elif query_type == "plan":
            return self.planner_agent.create_plan(payload.get("topics", []), payload.get("duration_days", 7))
        elif query_type == "motivation":
            # Pass a default motivation query if none is provided
            query = payload if payload else "Can you motivate me to study and learn programming?"
            return self.motivation_agent.get_boost(query)
        else:
            return "Invalid query type."
