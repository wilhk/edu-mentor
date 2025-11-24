import click
from rich.console import Console
from rich.panel import Panel

from orchestrator import EduMentorOrchestrator

console = Console()


@click.group()
def cli():
    """EduMentor – Multi-Agent Personalized Tutor (CLI demo)."""


@cli.command()
@click.option("--user-id", default="demo-user", help="User identifier.")
def start(user_id: str):
    """Start a new interactive study session."""
    orch = EduMentorOrchestrator(user_id=user_id)
    console.print(Panel.fit("Welcome to [bold cyan]EduMentor[/]!"))
    console.print("Let's capture or update your learning profile first.\n")

    profile = orch.collect_profile()
    console.print(Panel.fit(f"Profile for [bold]{user_id}[/]:\n{profile}"))

    console.print("\nRunning a short demo study session (3 questions)...\n")
    session_summary = orch.run_study_session(num_questions=3)

    console.print(Panel.fit("Session summary", subtitle="Demo output"))
    console.print(session_summary)
    console.print("\nRun 'python src/main.py start' again to simulate another session.")


@cli.command()
@click.option("--user-id", default="demo-user", help="User identifier.")
def weekly_review(user_id: str):
    """Run the weekly progress evaluation loop agent."""
    orch = EduMentorOrchestrator(user_id=user_id)
    result = orch.run_weekly_evaluation()
    console.print(Panel.fit("Weekly Progress Review", subtitle=user_id))
    console.print(result)


if __name__ == "__main__":
    cli()
