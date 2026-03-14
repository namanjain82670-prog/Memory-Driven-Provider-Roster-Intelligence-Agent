import pandas as pd
from config import Config


class AlertSystem:

    def __init__(self):
        pass


    # ---------------------------------------
    # PIPELINE ALERTS
    # ---------------------------------------

    def check_pipeline_alerts(self, roster_df):

        alerts = []

        # Stuck roster operations
        stuck_ros = roster_df[roster_df["IS_STUCK"] == 1]

        if len(stuck_ros) > 0:
            alerts.append(
                f"ALERT: {len(stuck_ros)} roster operations are currently stuck in the pipeline."
            )

        # Failed roster operations
        failed_ros = roster_df[roster_df["IS_FAILED"] == 1]

        if len(failed_ros) > 0:
            alerts.append(
                f"ALERT: {len(failed_ros)} roster operations have failed processing."
            )

        # Red health flags
        red_flags = roster_df[
            (roster_df["PRE_PROCESSING_HEALTH"] == "Red") |
            (roster_df["ISF_GEN_HEALTH"] == "Red") |
            (roster_df["DART_GEN_HEALTH"] == "Red") |
            (roster_df["DART_REVIEW_HEALTH"] == "Red") |
            (roster_df["SPS_LOAD_HEALTH"] == "Red")
        ]

        if len(red_flags) > 0:
            alerts.append(
                f"ALERT: {len(red_flags)} pipeline stages showing critical (Red) health flags."
            )

        return alerts


    # ---------------------------------------
    # MARKET ALERTS
    # ---------------------------------------

    def check_market_alerts(self, market_df):

        alerts = []

        threshold = Config.MARKET_SUCCESS_THRESHOLD

        low_success = market_df[
            market_df["SCS_PERCENT"] < threshold
        ]

        if len(low_success) > 0:

            markets = list(low_success["MARKET"].unique())

            alerts.append(
                f"ALERT: Markets below success threshold ({threshold}%): {markets}"
            )

        return alerts


    # ---------------------------------------
    # DURATION ANOMALY ALERTS
    # ---------------------------------------

    def check_duration_anomalies(self, roster_df):

        alerts = []

        threshold = Config.DURATION_ANOMALY_THRESHOLD

        anomalies = roster_df[
            (roster_df["DART_GEN_DURATION"] /
             roster_df["AVG_DART_GEN_DURATION"]) > threshold
        ]

        if len(anomalies) > 0:

            alerts.append(
                f"ALERT: {len(anomalies)} ROs showing abnormal DART generation delays."
            )

        return alerts


    # ---------------------------------------
    # GLOBAL ALERT CHECK
    # ---------------------------------------

    def run_all_alerts(self, roster_df, market_df):

        alerts = []

        alerts.extend(self.check_pipeline_alerts(roster_df))

        alerts.extend(self.check_market_alerts(market_df))

        alerts.extend(self.check_duration_anomalies(roster_df))

        return alerts