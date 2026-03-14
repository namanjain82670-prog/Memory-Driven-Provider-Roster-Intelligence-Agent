import plotly.express as px
import webbrowser
import os


class VisualizationTool:

    def show_market_performance(self, dataframe):
        """
        Display market performance trend over time.
        """

        chart = px.line(
            dataframe,
            x="MONTH",
            y="SCS_PERCENT",
            color="MARKET",
            title="Market Success Percentage Trend",
            markers=True
        )

        # Save chart
        file_path = "market_performance_chart.html"
        chart.write_html(file_path)

        print(f"Market performance chart saved to {file_path}")

        # Open in browser
        webbrowser.open('file://' + os.path.realpath(file_path))


    def display_retry_metrics(self, dataframe):
        """
        Visualize retry performance across markets.
        """

        chart = px.bar(
            dataframe,
            x="MARKET",
            y="retry_lift",
            title="Retry Lift Comparison by Market",
            color="MARKET"
        )

        # Save chart
        file_path = "retry_metrics_chart.html"
        chart.write_html(file_path)

        print(f"Retry metrics chart saved to {file_path}")

        # Open in browser
        webbrowser.open('file://' + os.path.realpath(file_path))