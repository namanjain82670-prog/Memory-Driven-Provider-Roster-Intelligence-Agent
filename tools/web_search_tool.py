import google.generativeai as genai
from config import Config


class WebSearchTool:

    def __init__(self):

        genai.configure(api_key=Config.GEMINI_API_KEY)

        self.model = genai.GenerativeModel("gemini-2.0-flash")

    def search(self, query):

        prompt = f"""
        Provide factual information related to the following query:

        {query}

        Focus on healthcare provider roster operations, regulations, 
        or provider data validation standards if applicable.
        """

        response = self.model.generate_content(prompt)

        return response.text