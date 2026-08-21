"""
Day 25 - Answer Understanding Engine

Purpose:
Understand a candidate's answer and combine
intent classification with extracted information.
"""

from answer_intent_classifier import classify_intent
from skill_extractor import extract_skills
from experience_extractor import extract_experience_years
from availability_extractor import extract_availability


def understand_answer(answer: str) -> dict:
    """
    Analyze a candidate's answer and return a structured
    understanding object.
    """

    intent = classify_intent(answer)

    result = {
        "answer": answer,
        "intent": intent,
        "is_missing": False,
        "is_vague": False,
        "is_off_topic": False,
        "skills": [],
        "experience_years": None,
        "availability": None,
    }

    # Missing answer
    if intent == "missing_answer":
        result["is_missing"] = True
        return result

    # Unknown / off-topic answer
    if intent == "unknown":
        result["is_off_topic"] = True
        return result

    # Extract technical skills
    result["skills"] = extract_skills(answer)

    # Extract years of experience
    result["experience_years"] = extract_experience_years(answer)

    # Extract availability
    result["availability"] = extract_availability(answer)

    return result