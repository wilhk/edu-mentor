from typing import Dict, Any, List
from memory.memory_bank import MemoryBank


class ProgressEvaluatorAgent:
    """Progress Evaluator / Loop Agent."""

    def __init__(self, memory_bank: MemoryBank):
        self.memory_bank = memory_bank

    def run(self, user_id: str, quiz: Dict[str, Any], answers: List[Dict[str, Any]]) -> Dict[str, Any]:
        # Toy evaluation: assign fixed accuracy; plug in real grading logic later
        questions = quiz.get("questions", [])
        topics = {q["topic"] for q in questions}
        topic_scores = {t: 0.6 for t in topics}
        return {
            "accuracy": 0.6,
            "topic_scores": topic_scores,
        }

    def weekly_review(self, user_id: str, mastery: Dict[str, float] | None, history_summary: str | None) -> Dict[str, Any]:
        mastery = mastery or {}
        return {
            "history_summary": history_summary or "(Demo) Weekly review summary.",
            "mastery_snapshot": mastery,
            "recommendations": [
                "Focus on weakest topics next week.",
                "Add one extra quiz session.",
            ],
        }
