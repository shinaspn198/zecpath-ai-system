"""
Day 25 - Availability Extraction Engine

Purpose:
Extract candidate availability information
from HR screening answers.
"""


def extract_availability(answer: str):
    """
    Extract availability information from a candidate's answer.

    Args:
        answer: Candidate's response as text.

    Returns:
        Availability category as a string,
        or None if availability is not detected.
    """

    if not answer or not answer.strip():
        return None

    text = answer.lower().strip()

    # Immediate availability
    immediate_keywords = [
        "immediately",
        "immediate",
        "right away",
        "available now",
        "join now",
    ]

    if any(keyword in text for keyword in immediate_keywords):
        return "immediate"

    # 15 days
    if "15 days" in text or "15 day" in text:
        return "15_days"

    # 30 days
    if "30 days" in text or "30 day" in text:
        return "30_days"

    # Two weeks
    if "2 weeks" in text or "two weeks" in text:
        return "2_weeks"

    # One week
    if "1 week" in text or "one week" in text:
        return "1_week"

    # Notice period
    if "notice period" in text:
        return "notice_period"

    return None