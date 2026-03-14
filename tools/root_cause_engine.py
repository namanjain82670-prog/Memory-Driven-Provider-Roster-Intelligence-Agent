class RootCauseEngine:

    def identify_causes(self, dataframe):

        findings = []

        for _, record in dataframe.iterrows():

            reason = None

            if record["IS_FAILED"] == 1:
                reason = "Pipeline processing failure"

            elif record["IS_STUCK"] == 1:
                reason = "Processing stage stuck"

            if reason:
                findings.append({
                    "RO_ID": record["RO_ID"],
                    "root_cause": reason
                })

        return findings