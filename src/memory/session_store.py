from typing import Dict, Any


class InMemorySessionStore:
    """Very simple in-memory session store.

    For demo only; replace with Redis/DB for real deployments.
    """

    def __init__(self):
        self._store: Dict[str, Dict[str, Any]] = {}

    def get(self, session_id: str) -> Dict[str, Any] | None:
        return self._store.get(session_id)

    def set(self, session_id: str, state: Dict[str, Any]) -> None:
        self._store[session_id] = state

    def clear(self, session_id: str) -> None:
        self._store.pop(session_id, None)
