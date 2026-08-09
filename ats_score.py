import json
from pathlib import Path


# Load ATS role weights
BASE_DIR = Path(__file__).resolve().parent
WEIGHTS_FILE = BASE_DIR / "config" / "weights.json"

with open(WEIGHTS_FILE, "r") as file:
    WEIGHTS = json.load(file)


def calculate_ats_score(
    role,
    skill_match,
    experience_relevance,
    education_alignment,
    semantic_similarity
):
    """
    Calculate the weighted ATS score for a candidate.
    """

    if role not in WEIGHTS:
        raise ValueError(f"Unsupported role: {role}")

    candidate = {
        "skill_match": skill_match,
        "experience_relevance": experience_relevance,
        "education_alignment": education_alignment,
        "semantic_similarity": semantic_similarity
    }

    # Handle missing values
    for key, value in candidate.items():
        if value is None:
            candidate[key] = 0

        if not 0 <= candidate[key] <= 100:
            raise ValueError(f"{key} must be between 0 and 100")

    role_weights = WEIGHTS[role]

    skill_score = (
        candidate["skill_match"]
        * role_weights["skill_match"]
        / 100
    )

    experience_score = (
        candidate["experience_relevance"]
        * role_weights["experience_relevance"]
        / 100
    )

    education_score = (
        candidate["education_alignment"]
        * role_weights["education_alignment"]
        / 100
    )

    semantic_score = (
        candidate["semantic_similarity"]
        * role_weights["semantic_similarity"]
        / 100
    )

    ats_score = (
        skill_score
        + experience_score
        + education_score
        + semantic_score
    )

    return round(ats_score, 2)


if __name__ == "__main__":

    # Test candidate
    score = calculate_ats_score(
        role="AI Engineer",
        skill_match=69.98,
        experience_relevance=69.98,
        education_alignment=69.98,
        semantic_similarity=70.02
    )

    print("========== ATS SCORE REPORT ==========")
    print("Role: AI Engineer")
    print(f"Final ATS Score: {score:.2f}%")