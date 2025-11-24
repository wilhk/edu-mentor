from typing import Dict, Any
from memory.memory_bank import MemoryBank


class ProfileAgent:
    """Profile & Goal Agent.

    Captures and updates the learner's profile and goals.
    For now this returns a default profile if none exists.
    Replace `run()` with a conversational LLM-driven flow.
    """

    def __init__(self, memory_bank: MemoryBank):
        self.memory_bank = memory_bank

    def run(self, user_id: str, existing_profile: Dict[str, Any] | None = None) -> Dict[str, Any]:
        if existing_profile:
            return existing_profile

        # TODO: replace with interactive questions to the learner.
        return {
            "subject": "Linear Algebra",
            "level": "Beginner",
            "goal": "Pass midterm in 6 weeks",
            "weekly_hours": 5,
            "deadline": None,
            "preferences": ["example-heavy", "short explanations"],
        }
