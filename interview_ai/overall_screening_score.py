"""
Day 26 - Step 4
Overall Screening Score Aggregation

Purpose:
Combine individual screening question scores
into one overall candidate screening score.
"""


def calculate_overall_score(question_scores):
    """
    Calculate the overall screening score.

    Args:
        question_scores:
            List of individual question scores.

    Returns:
        Dictionary containing:
        - total_score
        - maximum_score
        - overall_score
        - questions_evaluated
    """

    if not isinstance(question_scores, list):
        raise TypeError(
            "question_scores must be a list."
        )

    if not question_scores:
        raise ValueError(
            "question_scores cannot be empty."
        )

    total_score = 0
    maximum_score = 0

    for score in question_scores:

        if not isinstance(score, dict):
            raise TypeError(
                "Each question score must be a dictionary."
            )

        if "total_score" not in score:
            raise ValueError(
                "Each question score must contain total_score."
            )

        if "max_score" not in score:
            raise ValueError(
                "Each question score must contain max_score."
            )

        total_score += score["total_score"]
        maximum_score += score["max_score"]

    if maximum_score <= 0:
        raise ValueError(
            "Maximum score must be greater than 0."
        )

    overall_score = (
        total_score / maximum_score
    ) * 100

    return {
        "total_score": total_score,
        "maximum_score": maximum_score,
        "overall_score": round(overall_score, 2),
        "questions_evaluated": len(question_scores)
    }