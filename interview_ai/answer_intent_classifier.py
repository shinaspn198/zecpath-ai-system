"""
Day 25 - Answer Intent Classification Engine

Purpose:
Classify the intent of a candidate's answer during
AI-powered HR screening.
"""


def classify_intent(answer: str) -> str:
    """
    Classify the candidate's answer into a basic intent category.

    Args:
        answer: Candidate's response as text.

    Returns:
        Intent category as a string.
    """

    if not answer or not answer.strip():
        return "missing_answer"

    text = answer.lower().strip()

    # Introduction intent
    introduction_keywords = [
    "my name is",
    "myself",
    "about me",
    "let me introduce",
    "i would like to introduce",
    ]

    if any(keyword in text for keyword in introduction_keywords):
     return "introduction"

    # Availability intent
    availability_keywords =[
        "available",
        "availability",
        "join",
        "joining",
        "notice period",
        "immediately",
        "immediate",
        "days",
        "weeks",
    ]

    if any(keyword in text for keyword in availability_keywords):
        return "availability"

    # Salary intent
    salary_keywords = [
        "salary",
        "expected salary",
        "expect",
        "package",
        "lpa",
        "ctc",
        "compensation",
    ]

    if any(keyword in text for keyword in salary_keywords):
        return "salary_expectation"

    # Experience intent
    experience_keywords = [
        "experience",
        "years",
        "worked",
        "working",
        "internship",
        "intern",
        "developer",
        "engineer",
    ]

    if any(keyword in text for keyword in experience_keywords):
        return "experience"

    # Skills intent
    skill_keywords = [
        "python",
        "java",
        "javascript",
        "machine learning",
        "deep learning",
        "fastapi",
        "react",
        "sql",
        "skills",
        "programming",
        "developer",
    ]

    if any(keyword in text for keyword in skill_keywords):
        return "skills"

    # Unknown intent
    return "unknown"