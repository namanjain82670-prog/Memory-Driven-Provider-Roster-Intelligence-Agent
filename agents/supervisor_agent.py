from agents.pipeline_agent import PipelineAgent
from agents.market_agent import MarketAgent
from memory.memory_manager import MemoryManager


class SupervisorAgent:

    def __init__(self):
        # Initialize sub-agents and memory system
        self.pipeline_agent = PipelineAgent()
        self.market_agent = MarketAgent()
        self.memory_system = MemoryManager()

    def process_query(self, user_query):
        """
        Route the user query to the appropriate agent
        and return both context and results.
        """

        # Retrieve context from memory
        memory_context = self.memory_system.retrieve_context(user_query)

        # Decide which agent should handle the query
        if "pipeline" in user_query.lower():
            response = self.pipeline_agent.investigate()

        elif "market" in user_query.lower():
            response = self.market_agent.analyze()

        else:
            response = "Unable to determine the intent of the query"

        # Store interaction in episodic memory
        self.memory_system.episodic.store(user_query, str(response))

        return {
            "memory_context": memory_context,
            "analysis_result": response
        }