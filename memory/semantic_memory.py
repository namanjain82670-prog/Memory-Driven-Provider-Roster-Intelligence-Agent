from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


class SemanticMemory:

    def __init__(self):

        knowledge = [
            "Pre-processing validates roster files before pipeline processing.",
            "ISF generation converts roster data into structured internal format.",
            "DART generation prepares provider data for validation.",
            "DART review is manual verification of provider data.",
            "SPS load loads validated provider data into production systems.",
            "Green health flag means the stage is performing normally.",
            "Yellow health flag indicates a warning or slower performance.",
            "Red health flag indicates a critical issue in the pipeline stage.",
            "IS_STUCK indicates the pipeline stage has stalled.",
            "IS_FAILED indicates the roster operation failed."
        ]

        embeddings = HuggingFaceEmbeddings()

        self.vector_db = FAISS.from_texts(knowledge, embeddings)

    def search(self, query):
        """
        Search semantic knowledge base
        """

        results = self.vector_db.similarity_search(query)

        return results