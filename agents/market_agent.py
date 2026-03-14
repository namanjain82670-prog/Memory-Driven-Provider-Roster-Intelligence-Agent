from tools.data_tool import DataTool

class MarketAgent:

    def __init__(self):
        # Initialize data processing tool
        self.data_tool = DataTool()

    def generate_market_insights(self):
        """
        Perform analysis on market data to evaluate retry performance
        and state-level correlations.
        """

        retry_metrics = self.data_tool.retry_analysis()
        state_metrics = self.data_tool.market_correlation()

        insights = {
            "retry_metrics": retry_metrics,
            "state_metrics": state_metrics
        }

        return insights