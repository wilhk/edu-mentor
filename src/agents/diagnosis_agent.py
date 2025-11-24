from typing import Dict, Any
from memory.memory_bank import MemoryBank


class DiagnosisAgent:
    """Knowledge Diagnosis Agent.

    Produces a topic mastery map.
    In a real system this would analyze answers from a diagnostic quiz.
    """

    def __init__(self, memory_bank: MemoryBank):
        self.memory_bank = memory_bank

    def run(self, user_id: str, profile: Dict[str, Any] | None, mastery: Dict[str, float] | None) -> Dict[str, Any]:
        if mastery:
            return {"topic_mastery": mastery, "weak_topics": [k for k, v in mastery.items() if v < 0.5]}

        # Default starting mastery for a new learner
        topic_mastery = {
            "matrix_multiplication": 0.3,
            "vectors": 0.6,
            "eigenvalues": 0.1,
        }
        return {"topic_mastery": topic_mastery, "weak_topics": ["matrix_multiplication", "eigenvalues"]}
