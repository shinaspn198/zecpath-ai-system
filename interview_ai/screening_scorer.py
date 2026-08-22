"""
Day 26 - Screening Scoring Engine

Step 1:
Define scoring parameters for candidate screening responses.

Step 2:
Calculate score for an individual screening question.

Step 3:
Normalize screening scores to a 0-100 scale.

Scoring parameters:
- Clarity
- Relevance
- Completeness
- Consistency
"""


# ============================================================
# STEP 1 - SCORING PARAMETERS
# ============================================================

SCORING_PARAMETERS = {
    "clarity": {
        "max_score": 25,
        "description": "Measures how clearly the candidate communicates the answer."
    },

    "relevance": {
        "max_score": 25,
        "description": "Measures how relevant the answer is to the screening question."
    },

    "completeness": {
        "max_score": 25,
        "description": "Measures whether the candidate provides sufficient information."
    },

    "consistency": {
        "max_score": 25,
        "description": "Measures whether the answer is consistent with the candidate's other responses."
    }
}


def get_scoring_parameters():
    """
    Return the configured screening scoring parameters.
    """

    return SCORING_PARAMETERS


# ============================================================
# STEP 2 - PER-QUESTION SCORING
# ============================================================

def calculate_question_score(
    clarity,
    relevance,
    completeness,
    consistency
):
    """
    Calculate the score for one screening question.

    Each parameter is scored from 0 to 25.

    Returns:
        Dictionary containing individual scores and total score.
    """

    scores = {
        "clarity": clarity,
        "relevance": relevance,
        "completeness": completeness,
        "consistency": consistency
    }

    # Validate scores
    for parameter, score in scores.items():

        if not isinstance(score, (int, float)):
            raise TypeError(
                f"{parameter} score must be a number."
            )

        if score < 0 or score > 25:
            raise ValueError(
                f"{parameter} score must be between 0 and 25."
            )

    total_score = sum(scores.values())

    return {
        "clarity": clarity,
        "relevance": relevance,
        "completeness": completeness,
        "consistency": consistency,
        "total_score": total_score,
        "max_score": 100
    }


# ============================================================
# STEP 3 - SCORE NORMALIZATION
# ============================================================

def normalize_score(score, max_score=100):
    """
    Normalize a raw screening score to a 0-100 scale.

    Args:
        score: Raw screening score.
        max_score: Maximum possible raw score.

    Returns:
        Normalized score between 0 and 100.
    """

    # Validate score type
    if not isinstance(score, (int, float)):
        raise TypeError("Score must be a number.")

    # Validate maximum score type
    if not isinstance(max_score, (int, float)):
        raise TypeError("Maximum score must be a number.")

    # Maximum score cannot be zero or negative
    if max_score <= 0:
        raise ValueError(
            "Maximum score must be greater than 0."
        )

    # Score cannot exceed allowed range
    if score < 0 or score > max_score:
        raise ValueError(
            f"Score must be between 0 and {max_score}."
        )

    # Normalize score
    normalized_score = (score / max_score) * 100

    return round(normalized_score, 2)