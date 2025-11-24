from typing import Dict, Any
from memory.memory_bank import MemoryBank


class LessonPlannerAgent:
    """Lesson Planner Agent.

    Turns profile + diagnosis into a simple weekly plan.
    """

    def __init__(self, memory_bank: MemoryBank):
        self.memory_bank = memory_bank

    def run(self, user_id: str, profile: Dict[str, Any], diagnosis: Dict[str, Any]) -> Dict[str, Any]:
        mastery = diagnosis.get("topic_mastery", {})
        hours = profile.get("weekly_hours", 4)
        minutes = hours * 60

        if not mastery:
            return {"week": 1, "study_plan": [], "quizzes_per_week": 2}

        total_weight = sum((1.0 - mastery.get(t, 0.0)) for t in mastery.keys())
        if total_weight <= 0:
            total_weight = float(len(mastery))

        study_plan = []
        for topic, score in mastery.items():
            weight = (1.0 - score) / total_weight
            topic_minutes = int(minutes * weight)
            study_plan.append({"topic": topic, "minutes": max(topic_minutes, 30)})

        return {"week": 1, "study_plan": study_plan, "quizzes_per_week": 3}
