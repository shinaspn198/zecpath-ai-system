"""
Day 25 - Skill Extraction Engine

Purpose:
Extract known technical skills from a candidate's answer.
"""

import re


KNOWN_SKILLS = [
    "Python",
    "Java",
    "JavaScript",
    "React",
    "FastAPI",
    "Flask",
    "Django",
    "SQL",
    "Machine Learning",
    "Deep Learning",
    "NLP",
    "Natural Language Processing",
    "TensorFlow",
    "PyTorch",
    "Scikit-learn",
    "Pandas",
    "NumPy",
    "LangChain",
]


def extract_skills(answer: str) -> list[str]:
    """
    Extract known technical skills from a candidate's answer.

    Args:
        answer: Candidate's response as text.

    Returns:
        List of detected skills.
    """

    if not answer or not answer.strip():
        return []

    text = answer.lower()

    detected_skills = []

    for skill in KNOWN_SKILLS:

        pattern = r"\b" + re.escape(skill.lower()) + r"\b"

        if re.search(pattern, text):
            detected_skills.append(skill)

    return detected_skills