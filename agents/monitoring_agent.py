from tools.data_tool import DataTool


class MonitoringAgent:

    def __init__(self):
        # Initialize data access tool
        self.data_tool = DataTool()

    def check_pipeline_status(self):
        """
        Scan the roster data and report pipeline health.
        """

        stuck_records = self.data_tool.stuck_ros()
        stuck_count = len(stuck_records)

        if stuck_count > 0:
            message = f"ALERT: {stuck_count} roster operations are currently stuck"
        else:
            message = "Pipeline status: healthy"

        return message