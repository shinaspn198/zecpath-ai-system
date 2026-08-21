"""
Day 25 - Salary Extraction Engine

Purpose:
Extract candidate salary expectation
from HR screening answers.
"""

import re


def extract_salary(answer: str):
    """
    Extract expected salary from a candidate's answer.

    Args:
        answer: Candidate's response as text.

    Returns:
        Salary value in LPA as float,
        or None if salary is not detected.
    """

    if not answer or not answer.strip():
        return None

    text = answer.lower().strip()

    # Match formats like:
    # 6 LPA
    # 6.5 LPA
    # 6 lakhs
    # 6 lakh
    match = re.search(
        r"(\d+(?:\.\d+)?)\s*(?:lpa|lakhs?|lac)",
        text
    )

    if match:
        return float(match.group(1))

    return None