from agents.concept_agent import ConceptAgent
from .code_agent import CodeAgent
from agents.planner_agent import PlannerAgent
from .motivation_agent import MotivationAgent
from .central_agent import CentralAgent

class OrchestratorAgent:
    def __init__(self):
        self.concept_agent = ConceptAgent()
        self.code_agent = CodeAgent()
        self.planner_agent = PlannerAgent()
        self.motivation_agent = MotivationAgent()
        self.central_agent = CentralAgent()

    def process_request(self, user_prompt):
        """
        Main entry point for processing user requests.
        Uses CentralAgent to analyze and route the request.
        """
        return self.central_agent.analyze_and_route(user_prompt, self)

    def route(self, query_type, payload):
        """
        Internal routing method used by CentralAgent.
        Routes the request to the appropriate specialized agent.
        """
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
