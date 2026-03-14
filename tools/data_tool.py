from config import Config
import pandas as pd

class DataTool:

    def __init__(self):

        self.roster = pd.read_csv(Config.ROSTER_DATA_PATH)

        self.market = pd.read_csv(Config.MARKET_DATA_PATH)


class RosterDataAnalyzer:

    def __init__(self, roster_path="data/roster_processing_details.csv",
                 market_path="data/aggregated_operational_metrics.csv"):

        # Load input datasets
        self.roster_df = pd.read_csv(roster_path)
        self.market_df = pd.read_csv(market_path)

    def fetch_stuck_rosters(self):
        """Identify all roster records that are marked as stuck."""

        condition = self.roster_df["IS_STUCK"] == 1
        stuck_rows = self.roster_df.loc[condition]

        return stuck_rows

    def calculate_retry_efficiency(self):
        """Calculate improvement between first iteration and retry iteration."""

        df = self.market_df.copy()

        first_iter = df["FIRST_ITER_SCS_CNT"]
        next_iter = df["NEXT_ITER_SCS_CNT"]

        df["retry_efficiency"] = next_iter / (first_iter + 1)

        return df

    def summarize_state_issues(self):
        """Generate state-level summary for stuck and failed records."""

        aggregation_map = {
            "IS_STUCK": "sum",
            "IS_FAILED": "sum"
        }

        state_summary = (
            self.roster_df
            .groupby("CNT_STATE")
            .agg(aggregation_map)
            .reset_index()
        )

        return state_summary