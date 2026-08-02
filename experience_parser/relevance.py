from difflib import SequenceMatcher


def calculate_relevance(target_role, experience_profile):

    scores = []

    for exp in experience_profile:

        ratio = SequenceMatcher(
            None,
            target_role.lower(),
            exp["Job Title"].lower()
        ).ratio()

        scores.append(ratio)

    if not scores:
        return 0

    return round(max(scores) * 100, 2)