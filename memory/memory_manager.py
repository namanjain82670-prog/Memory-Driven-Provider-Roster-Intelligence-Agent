from memory.episodic_memory import EpisodicMemory
from memory.procedural_memory import ProceduralMemory
from memory.semantic_memory import SemanticMemory
from memory.rag_memory import RAGMemory


class MemoryManager:

    def __init__(self):

        self.episodic = EpisodicMemory()
        self.procedural = ProceduralMemory()
        self.semantic = SemanticMemory()
        self.rag = RAGMemory()


    def retrieve_context(self, query):
        """
        Retrieve relevant information from all memory types
        """

        episodic_data = self.episodic.search(query)

        semantic_data = self.semantic.search(query)

        rag_data = self.rag.search(query)

        return {
            "episodic": episodic_data,
            "semantic": semantic_data,
            "rag": rag_data
        }