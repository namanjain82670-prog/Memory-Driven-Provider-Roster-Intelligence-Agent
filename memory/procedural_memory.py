import json
import os


class ProceduralMemory:

    def __init__(self, procedure_folder="procedures"):
        """
        Store and manage procedural knowledge used by the system.
        """
        self.storage = {}
        self.folder_path = procedure_folder

        self._load_workflows()

    def _load_workflows(self):
        """
        Load procedure definitions from JSON files in the folder.
        """

        if not os.path.exists(self.folder_path):
            return

        for filename in os.listdir(self.folder_path):

            file_path = os.path.join(self.folder_path, filename)

            with open(file_path, "r") as file:
                content = json.load(file)

                name = content.get("name")
                if name:
                    self.storage[name] = content

    def fetch_workflow(self, procedure_name):
        """
        Retrieve a stored procedure by name.
        """
        return self.storage.get(procedure_name)

    def register_workflow(self, name, description, logic):
        """
        Add a new procedure to memory.
        """

        self.storage[name] = {
            "name": name,
            "description": description,
            "logic": logic
        }