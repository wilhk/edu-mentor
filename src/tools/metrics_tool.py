from observability.metrics import metrics


def log_question_asked():
    metrics.increment("questions_asked", 1)
