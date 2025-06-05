import re
from typing import List


def decompose_task(question: str) -> List[str]:
    """Decompose a natural language question into sub-questions.

    This uses simple heuristic rules. If heuristics fail to split the
    question, the original question is returned.
    """
    if not question:
        return []
    # try splitting by question marks
    parts = [p.strip() for p in re.split(r"\?+", question) if p.strip()]
    if len(parts) > 1:
        return [p + '?' for p in parts]
    # try splitting by conjunctions
    parts = [p.strip() for p in re.split(r"\b(?:and then|then|and)\b", question) if p.strip()]
    if len(parts) > 1:
        return parts
    return [question.strip()]
