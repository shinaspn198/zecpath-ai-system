TARGET_FIELDS = [
    "Artificial Intelligence",
    "Data Science",
    "Machine Learning",
    "Computer Science",
    "Software Engineering",
    "Information Technology",
]

def calculate_education_relevance(education):
    total = len(education)

    if total == 0:
        return 0

    relevant = 0

    for edu in education:
        field = edu["Field"].lower()

        for target in TARGET_FIELDS:
            if target.lower() in field:
                relevant += 1
                break

    return round((relevant / total) * 100, 2)