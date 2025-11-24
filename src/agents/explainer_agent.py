from typing import Dict, Any
from memory.memory_bank import MemoryBank


class ExplainerAgent:
    """Explainer Agent.

    Provides brief placeholder explanations.
    Replace `explain()` with LLM calls for personalized feedback.
    """

    def __init__(self, memory_bank: MemoryBank):
        self.memory_bank = memory_bank

    def explain(self, question: Dict[str, Any], user_answer: str, correct_answer: Any) -> Dict[str, Any]:
        return {
            "question_id": question.get("id"),
            "explanation": "(Demo) In a real system, this would contain a personalized explanation of the concept.",
            "style": "step_by_step",
        }
