"""
Day 26 - Step 5
Screening Score Interpretation

Purpose:
Convert the overall screening score into
an understandable candidate performance category.
"""


# ============================================================
# SCORE THRESHOLDS
# ============================================================

SCORE_CATEGORIES = {
    "excellent": {
        "minimum_score": 85,
        "label": "Excellent",
        "description": "Candidate demonstrates a very strong screening performance."
    },

    "good": {
        "minimum_score": 70,
        "label": "Good",
        "description": "Candidate demonstrates a strong screening performance."
    },

    "average": {
        "minimum_score": 50,
        "label": "Average",
        "description": "Candidate demonstrates an acceptable but improvable screening performance."
    },

    "weak": {
        "minimum_score": 0,
        "label": "Weak",
        "description": "Candidate demonstrates a weak screening performance."
    }
}


def interpret_screening_score(overall_score):
    """
    Interpret an overall screening score.

    Args:
        overall_score: Candidate's overall score from 0 to 100.

    Returns:
        Dictionary containing category, label and description.
    """

    if not isinstance(overall_score, (int, float)):
        raise TypeError(
            "Overall score must be a number."
        )

    if overall_score < 0 or overall_score > 100:
        raise ValueError(
            "Overall score must be between 0 and 100."
        )

    if overall_score >= 85:

        category = "excellent"

    elif overall_score >= 70:

        category = "good"

    elif overall_score >= 50:

        category = "average"

    else:

        category = "weak"

    result = SCORE_CATEGORIES[category]

    return {
        "score": overall_score,
        "category": category,
        "label": result["label"],
        "description": result["description"]
    }