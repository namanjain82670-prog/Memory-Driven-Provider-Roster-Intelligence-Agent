from tools.data_tool import DataTool
from tools.root_cause_engine import RootCauseEngine


class PipelineAgent:

    def __init__(self):

        self.data = DataTool()
        self.root = RootCauseEngine()

    def investigate(self):

        stuck = self.data.stuck_ros()

        causes = self.root.analyze(stuck)

        return {
            "stuck": stuck,
            "root_causes": causes
        }