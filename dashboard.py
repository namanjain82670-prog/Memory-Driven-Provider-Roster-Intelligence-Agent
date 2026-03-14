import streamlit as st
from tools.data_tool import DataTool
from tools.visualization_tool import VisualizationTool


def launch_dashboard():
    # Initialize tools
    data_tool = DataTool()
    visualizer = VisualizationTool()

    st.title("📊 RosterIQ Analytics Dashboard")

    st.write("Explore market performance and retry effectiveness.")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Show Market Success Trend"):
            visualizer.market_trend(data_tool.market)

    with col2:
        if st.button("Analyze Retry Effectiveness"):
            retry_data = data_tool.retry_analysis()
            visualizer.retry_chart(retry_data)


if __name__ == "__main__":
    launch_dashboard()