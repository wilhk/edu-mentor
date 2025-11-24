def evaluate_expression(expr: str) -> str:
    """Placeholder for a safe math/code execution tool."""
    try:
        result = eval(expr, {"__builtins__": {}}, {})
        return str(result)
    except Exception as e:
        return f"error: {e}"
