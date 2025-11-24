from typing import Dict, Any, List
from memory.memory_bank import MemoryBank


class QuizAgent:
    """Quiz & Practice Generator Agent.

    Generates toy questions. Replace with LLM-based question generation.
    """

    def __init__(self, memory_bank: MemoryBank):
        self.memory_bank = memory_bank

    def generate_quiz(self, user_id: str, topics: List[str], num_questions: int = 3) -> Dict[str, Any]:
        if not topics:
            topics = ["general concept"]

        questions = []
        for i in range(num_questions):
            topic = topics[i % len(topics)]
            qid = f"q{i+1}"
            questions.append(
                {
                    "id": qid,
                    "topic": topic,
                    "difficulty": "medium",
                    "type": "short_answer",
                    "question": f"(Demo) Explain the key idea of {topic}.",
                    "answer": "<expected demo answer>",
                    "rubric": "Checks if core concept is mentioned.",
                    "hint": "Think about the definition and a simple example.",
                }
            )
        return {"questions": questions}
