"""
Day 25 - Experience Extraction Engine

Purpose:
Extract years of professional experience from
a candidate's answer.
"""

import re


def extract_experience_years(answer: str):
    """
    Extract the number of years of experience
    mentioned in the candidate's answer.

    Args:
        answer: Candidate's response as text.

    Returns:
        Experience years as a float, or None if not found.
    """

    if not answer or not answer.strip():
        return None

    text = answer.lower().strip()

    patterns = [
        r"(\d+(?:\.\d+)?)\s*\+?\s*years?\s+of\s+experience",
        r"(\d+(?:\.\d+)?)\s*\+?\s*years?",
    ]

    for pattern in patterns:
        match = re.search(pattern, text)

        if match:
            return float(match.group(1))

    return None