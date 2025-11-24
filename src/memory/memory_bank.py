from typing import Dict, Any


class MemoryBank:
    """Simple in-memory 'long-term' memory.

    In a real project, this would be backed by a database or vector store.
    """

    def __init__(self):
        self._profiles: Dict[str, Dict[str, Any]] = {}
        self._mastery: Dict[str, Dict[str, float]] = {}
        self._history: Dict[str, str] = {}

    def get_profile(self, user_id: str) -> Dict[str, Any] | None:
        return self._profiles.get(user_id)

    def save_profile(self, user_id: str, profile: Dict[str, Any]) -> None:
        self._profiles[user_id] = profile

    def get_mastery(self, user_id: str) -> Dict[str, float] | None:
        return self._mastery.get(user_id)

    def save_mastery(self, user_id: str, mastery: Dict[str, float]) -> None:
        self._mastery[user_id] = mastery

    def get_history_summary(self, user_id: str) -> str | None:
        return self._history.get(user_id)

    def save_history_summary(self, user_id: str, summary: str) -> None:
        self._history[user_id] = summary
