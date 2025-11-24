from typing import Dict, Any
from memory.memory_bank import MemoryBank


class MemoryManagerAgent:
    """Memory Manager Agent.

    Updates long-term mastery and stores summaries.
    """

    def __init__(self, memory_bank: MemoryBank):
        self.memory_bank = memory_bank

    def update_after_session(self, user_id: str, diagnosis: Dict[str, Any], eval_result: Dict[str, Any]) -> None:
        topic_mastery = diagnosis.get("topic_mastery", {})
        topic_scores = eval_result.get("topic_scores", {})

        updated: Dict[str, float] = {}
        for topic, base in topic_mastery.items():
            delta = 0.05 if topic in topic_scores else 0.0
            updated[topic] = max(0.0, min(1.0, base + delta))

        self.memory_bank.save_mastery(user_id, updated)
        self.memory_bank.save_history_summary(user_id, "(Demo) Updated after session.")
