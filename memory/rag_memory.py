from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


class RAGMemory:

    def __init__(self):

        # Embedding model
        self.embedding_model = HuggingFaceEmbeddings()

        # Store raw documents
        self.document_store = []

        # FAISS vector index
        self.vector_index = None


    def insert_document(self, content):
        """
        Add new knowledge to memory
        """

        self.document_store.append(content)

        # Rebuild FAISS index
        self.vector_index = FAISS.from_texts(
            self.document_store,
            self.embedding_model
        )


    def search(self, query):
        """
        Retrieve relevant documents
        """

        if self.vector_index is None:
            return []

        results = self.vector_index.similarity_search(query)

        return results