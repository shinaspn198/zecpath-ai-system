"""
Day 26 - Step 6
Final Screening Scoring Integration

Combines:

1. Per-question scoring
2. Overall score aggregation
3. Score normalization
4. Score interpretation

Produces one final candidate screening result.
"""

from screening_scorer import calculate_question_score
from overall_screening_score import calculate_overall_score
from score_interpreter import interpret_screening_score


def calculate_final_screening_result(question_scores):
    """
    Generate the final screening result for a candidate.

    Args:
        question_scores:
            List containing individual question score dictionaries.

    Returns:
        Complete structured screening result.
    """

    if not isinstance(question_scores, list):
        raise TypeError(
            "question_scores must be a list."
        )

    if not question_scores:
        raise ValueError(
            "question_scores cannot be empty."
        )

    # --------------------------------------------------------
    # Step 1 - Validate individual question scores
    # --------------------------------------------------------

    validated_scores = []

    for score in question_scores:

        if not isinstance(score, dict):
            raise TypeError(
                "Each question score must be a dictionary."
            )

        required_fields = [
            "clarity",
            "relevance",
            "completeness",
            "consistency"
        ]

        for field in required_fields:

            if field not in score:
                raise ValueError(
                    f"Missing required field: {field}"
                )

        validated_score = calculate_question_score(
            clarity=score["clarity"],
            relevance=score["relevance"],
            completeness=score["completeness"],
            consistency=score["consistency"]
        )

        validated_scores.append(validated_score)

    # --------------------------------------------------------
    # Step 2 - Calculate overall score
    # --------------------------------------------------------

    overall_result = calculate_overall_score(
        validated_scores
    )

    # --------------------------------------------------------
    # Step 3 - Normalize overall score
    # --------------------------------------------------------

    normalized_score = overall_result["overall_score"]

    # --------------------------------------------------------
    # Step 4 - Interpret score
    # --------------------------------------------------------

    interpretation = interpret_screening_score(
        normalized_score
    )

    # --------------------------------------------------------
    # Step 5 - Build final result
    # --------------------------------------------------------

    return {
        "question_scores": validated_scores,
        "total_score": overall_result["total_score"],
        "maximum_score": overall_result["maximum_score"],
        "overall_score": normalized_score,
        "questions_evaluated": overall_result["questions_evaluated"],
        "category": interpretation["category"],
        "label": interpretation["label"],
        "description": interpretation["description"]
    }