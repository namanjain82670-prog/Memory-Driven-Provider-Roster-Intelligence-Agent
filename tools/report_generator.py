class ReportGenerator:

    # -----------------------------------
    # PIPELINE REPORT
    # -----------------------------------
    def pipeline_report(self, stuck_ros, anomalies, root_causes):

        report = {}

        report["stuck_ro_count"] = len(stuck_ros)

        report["anomaly_count"] = len(anomalies)

        report["root_causes"] = root_causes

        report["recommendations"] = [
            "Investigate pipeline bottlenecks",
            "Check provider validation errors",
            "Review DART generation performance"
        ]

        return report


    # -----------------------------------
    # MARKET REPORT
    # -----------------------------------
    def market_report(self, market_df):

        report = {}

        avg_success = market_df["SCS_PERCENT"].mean()

        low_markets = market_df[
            market_df["SCS_PERCENT"] < 85
        ]["MARKET"].tolist()

        report["average_success_rate"] = avg_success

        report["markets_below_threshold"] = low_markets

        report["recommendations"] = [
            "Investigate retry effectiveness",
            "Check provider data ingestion errors",
            "Review pipeline health for affected markets"
        ]

        return report