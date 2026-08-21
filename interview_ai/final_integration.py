"""
Day 25 - Final Screening Integration

Purpose:
Combine all extracted candidate information
into one structured screening result.
"""


def integrate_screening_result(
    answer,
    intent=None,
    skills=None,
    experience_years=None,
    availability=None,
    salary_lpa=None,
    is_missing=False,
    is_vague=False,
    is_off_topic=False
):
    """
    Combine all screening information into one result.
    """

    return {
        "answer": answer,
        "intent": intent,
        "skills": skills if skills else [],
        "experience_years": experience_years,
        "availability": availability,
        "salary_lpa": salary_lpa,
        "is_missing": is_missing,
        "is_vague": is_vague,
        "is_off_topic": is_off_topic
    }