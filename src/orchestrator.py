from typing import Dict, Any, List

from memory.session_store import InMemorySessionStore
from memory.memory_bank import MemoryBank
from agents.profile_agent import ProfileAgent
from agents.diagnosis_agent import DiagnosisAgent
from agents.lesson_planner_agent import LessonPlannerAgent
from agents.quiz_agent import QuizAgent
from agents.explainer_agent import ExplainerAgent
from agents.evaluator_agent import ProgressEvaluatorAgent
from agents.memory_agent import MemoryManagerAgent
from observability.logger import logger
from observability.metrics import metrics


class EduMentorOrchestrator:
    """Main orchestrator that wires together agents, memory, and tools.

    This keeps logic simple so you can swap in your agent runtime easily.
    """

    def __init__(self, user_id: str):
        self.user_id = user_id
        self.session_store = InMemorySessionStore()
        self.memory_bank = MemoryBank()

        # agents
        self.profile_agent = ProfileAgent(self.memory_bank)
        self.diagnosis_agent = DiagnosisAgent(self.memory_bank)
        self.lesson_planner_agent = LessonPlannerAgent(self.memory_bank)
        self.quiz_agent = QuizAgent(self.memory_bank)
        self.explainer_agent = ExplainerAgent(self.memory_bank)
        self.evaluator_agent = ProgressEvaluatorAgent(self.memory_bank)
        self.memory_manager = MemoryManagerAgent(self.memory_bank)

    # ---------------------------
    # Public orchestration flows
    # ---------------------------

    def collect_profile(self) -> Dict[str, Any]:
        logger.info("collect_profile user=%s", self.user_id)
        existing = self.memory_bank.get_profile(self.user_id)
        profile = self.profile_agent.run(user_id=self.user_id, existing_profile=existing)
        self.memory_bank.save_profile(self.user_id, profile)
        return profile

    def run_study_session(self, num_questions: int = 3) -> Dict[str, Any]:
        logger.info("run_study_session user=%s", self.user_id)
        profile = self.memory_bank.get_profile(self.user_id)
        mastery = self.memory_bank.get_mastery(self.user_id)

        diagnosis = self.diagnosis_agent.run(self.user_id, profile, mastery)
        plan = self.lesson_planner_agent.run(self.user_id, profile, diagnosis)

        topics = [t["topic"] for t in plan.get("study_plan", [])] or ["general concept"]
        quiz = self.quiz_agent.generate_quiz(
            user_id=self.user_id,
            topics=topics,
            num_questions=num_questions,
        )

        answers, explanations = self._simulate_user_answers_and_explanations(quiz)
        eval_result = self.evaluator_agent.run(self.user_id, quiz, answers)

        # update mastery + memory
        self.memory_manager.update_after_session(
            user_id=self.user_id,
            diagnosis=diagnosis,
            eval_result=eval_result,
        )

        return {
            "profile": profile,
            "diagnosis": diagnosis,
            "plan": plan,
            "quiz": quiz,
            "answers": answers,
            "explanations": explanations,
            "evaluation": eval_result,
        }

    def run_weekly_evaluation(self) -> Dict[str, Any]:
        logger.info("weekly_evaluation user=%s", self.user_id)
        mastery = self.memory_bank.get_mastery(self.user_id)
        history = self.memory_bank.get_history_summary(self.user_id)
        result = self.evaluator_agent.weekly_review(self.user_id, mastery, history)
        if "history_summary" in result:
            self.memory_bank.save_history_summary(self.user_id, result["history_summary"])
        return result

    # ---------------------------
    # Helpers (for demo only)
    # ---------------------------

    def _simulate_user_answers_and_explanations(self, quiz: Dict[str, Any]):
        """In this demo we fake user answers and explanations.

        Replace this with real UI-driven answers and on-demand explanations.
        """
        questions: List[Dict[str, Any]] = quiz.get("questions", [])
        answers = []
        explanations = []

        for q in questions:
            user_answer = "<demo answer>"
            answers.append({"id": q["id"], "user_answer": user_answer})
            explanations.append(
                self.explainer_agent.explain(
                    question=q,
                    user_answer=user_answer,
                    correct_answer=q.get("answer"),
                )
            )

        metrics.increment("questions_asked", len(questions))
        return answers, explanations
