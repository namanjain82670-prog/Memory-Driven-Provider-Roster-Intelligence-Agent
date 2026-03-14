import pandas as pd

# Agents
from agents.supervisor_agent import SupervisorAgent
from agents.pipeline_agent import PipelineAgent
from agents.market_agent import MarketAgent
from agents.monitoring_agent import MonitoringAgent

# Memory
from memory.memory_manager import MemoryManager

# Tools
from tools.data_tool import DataTool
from tools.visualization_tool import VisualizationTool
from tools.alert_system import AlertSystem
from tools.reasoning_engine import ReasoningEngine
from tools.report_generator import ReportGenerator
from tools.web_search_tool import WebSearchTool


class RosterIQEngine:

    def __init__(self):

        print("Starting RosterIQ Intelligence Engine...")

        # Initialize agents
        self.supervisor_agent = SupervisorAgent()
        self.pipeline_agent = PipelineAgent()
        self.market_agent = MarketAgent()
        self.monitor_agent = MonitoringAgent()

        # Initialize memory system
        self.memory_system = MemoryManager()

        # Initialize tools
        self.data_tool = DataTool()
        self.visualizer = VisualizationTool()
        self.alert_engine = AlertSystem()
        self.reason_engine = ReasoningEngine()
        self.report_builder = ReportGenerator()
        self.web_tool = WebSearchTool()

        print("RosterIQ System Initialized Successfully.")

    # --------------------------------------------------
    # PIPELINE ANALYSIS
    # --------------------------------------------------

    def run_pipeline_analysis(self):

        roster_data = self.data_tool.roster

        stuck_records = roster_data[roster_data["IS_STUCK"] == 1]

        reasoning_output = self.reason_engine.pipeline_reasoning(roster_data)

        alert_messages = self.alert_engine.check_pipeline_alerts(roster_data)

        report_output = self.report_builder.pipeline_report(stuck_records, [], [])

        return {
            "alerts": alert_messages,
            "reasoning": reasoning_output,
            "report": report_output
        }

    # --------------------------------------------------
    # MARKET ANALYSIS
    # --------------------------------------------------

    def run_market_analysis(self):

        market_data = self.data_tool.market

        reasoning_output = self.reason_engine.market_reasoning(market_data)

        alert_messages = self.alert_engine.check_market_alerts(market_data)

        report_output = self.report_builder.market_report(market_data)

        return {
            "alerts": alert_messages,
            "reasoning": reasoning_output,
            "report": report_output
        }

    # --------------------------------------------------
    # VISUALIZATION
    # --------------------------------------------------

    def display_market_trend(self):

        market_data = self.data_tool.market

        # Correct visualization function
        self.visualizer.show_market_performance(market_data)

    # --------------------------------------------------
    # WEB SEARCH
    # --------------------------------------------------

    def search_external_knowledge(self, user_query):

        search_results = self.web_tool.search(user_query)

        return search_results

    # --------------------------------------------------
    # QUERY ROUTING
    # --------------------------------------------------

    def process_query(self, user_query):

        # Retrieve context from memory
        context_data = self.memory_system.retrieve_context(user_query)

        user_query = user_query.lower()

        # IMPORTANT: chart condition first
        if "chart" in user_query:

            self.display_market_trend()
            output = "Market trend chart generated."

        elif "pipeline" in user_query or "stuck" in user_query:

            output = self.run_pipeline_analysis()

        elif "market" in user_query:

            output = self.run_market_analysis()

        elif "search" in user_query or "regulation" in user_query:

            output = self.search_external_knowledge(user_query)

        else:

            output = "Unable to interpret the query."

        # Store interaction in episodic memory
        self.memory_system.episodic.store(user_query, str(output))

        return {
            "context": context_data,
            "result": output
        }


# --------------------------------------------------
# APPLICATION ENTRY POINT
# --------------------------------------------------

def start_rosteriq():

    engine = RosterIQEngine()

    print("\nRosterIQ AI Intelligence System\n")

    while True:

        user_query = input("\nAsk RosterIQ: ")

        if user_query.lower() in ["exit", "quit"]:
            print("Stopping RosterIQ...")
            break

        response = engine.process_query(user_query)

        print("\nResult:")
        print(response["result"])


if __name__ == "__main__":
    start_rosteriq()