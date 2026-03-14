class ReasoningEngine:

    # -----------------------------
    # PIPELINE REASONING
    # -----------------------------
    def pipeline_reasoning(self, pipeline_df):

        reasoning = []

        if pipeline_df["IS_STUCK"].sum() > 0:
            reasoning.append(
                "Pipeline delay detected due to stuck roster operations."
            )

        if pipeline_df["IS_FAILED"].sum() > 0:
            reasoning.append(
                "Some roster files have failed during processing."
            )

        if pipeline_df["RUN_NO"].mean() > 1:
            reasoning.append(
                "Frequent reprocessing attempts indicate upstream data quality issues."
            )

        return reasoning


    # -----------------------------
    # MARKET REASONING
    # -----------------------------
    def market_reasoning(self, market_df):

        reasoning = []

        if market_df["SCS_PERCENT"].mean() < 90:
            reasoning.append(
                "Market success rate is below expected operational benchmark."
            )

        if market_df["NEXT_ITER_FAIL_CNT"].sum() > 0:
            reasoning.append(
                "Retry processing is still failing for some transactions."
            )

        if market_df["OVERALL_FAIL_CNT"].sum() > 0:
            reasoning.append(
                "Some provider data transactions are failing even after retries."
            )

        return reasoning