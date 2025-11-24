# EduMentor – Multi-Agent Personalized Tutor

EduMentor is a **multi-agent tutoring system** that adapts to each student’s goals, pace, and knowledge gaps using long-term memory, scheduled evaluation, and tool-calling.

This repository is intended as a **capstone project** skeleton for an agentic systems course. It demonstrates:

- Multi-agent design (profile, diagnosis, planner, quiz generator, explainer, evaluator, memory manager)
- Tool usage (code execution hooks, metrics, storage)
- Sessions & state (short-term session store + long-term memory bank)
- Long-running operations (weekly evaluation loop agent)
- Observability (structured logs + metrics)
- Evaluation scripts
- A simple CLI “frontend” for demo purposes

---

## Project Structure

```text
edu-mentor/
  ├─ README.md
  ├─ requirements.txt
  ├─ .gitignore
  ├─ src/
  │   ├─ main.py                # CLI entrypoint
  │   ├─ orchestrator.py        # session flow & agent routing
  │   ├─ agents/
  │   │   ├─ profile_agent.py
  │   │   ├─ diagnosis_agent.py
  │   │   ├─ lesson_planner_agent.py
  │   │   ├─ quiz_agent.py
  │   │   ├─ explainer_agent.py
  │   │   ├─ evaluator_agent.py
  │   │   └─ memory_agent.py
  │   ├─ tools/
  │   │   ├─ code_execution_tool.py
  │   │   ├─ metrics_tool.py
  │   │   └─ storage_tool.py
  │   ├─ memory/
  │   │   ├─ session_store.py
  │   │   └─ memory_bank.py
  │   └─ observability/
  │       ├─ logger.py
  │       └─ metrics.py
  ├─ eval/
  │   ├─ eval_questions.py
  │   └─ eval_learning_flow.py
  └─ docs/
      ├─ architecture.md
      ├─ agents.md
      └─ demo_script.md
```

---

## Quick Start

```bash
pip install -r requirements.txt

# From repo root
python -m src.main start

# Or directly
python src/main.py start
```

This skeleton uses **simple, fake logic** (no real LLM calls) so it runs without API keys.  
You can replace the internal placeholders with your actual agent runtime.

---

## How to Plug in Your Own Agent Runtime

- Replace the “toy” logic in `src/agents/*.py` with calls to your LLM / agent framework.
- Wire real tools in `src/tools/` (code execution, storage, search, etc.).
- Use `eval/` scripts to evaluate question quality and learning flow.
- Document your prompts and evaluation strategy in `docs/`.

---

## License

MIT (or your preferred license).
# edu-mentor
