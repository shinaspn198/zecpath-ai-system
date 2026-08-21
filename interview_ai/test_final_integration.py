"""
Day 25 - Final Integration Testing

Purpose:
Test the complete HR screening pipeline.
"""

from final_integration import integrate_screening_result


def test_experience_answer():
    result = integrate_screening_result(
        answer="I have 2 years of experience in Python.",
        intent="experience",
        skills=["Python"],
        experience_years=2.0,
        availability=None,
        salary_lpa=None,
        is_missing=False,
        is_vague=False,
        is_off_topic=False
    )

    assert result["intent"] == "experience"
    assert result["skills"] == ["Python"]
    assert result["experience_years"] == 2.0

    print("Experience test: PASSED")


def test_skills_answer():
    result = integrate_screening_result(
        answer="I am skilled in Python, FastAPI and Machine Learning.",
        intent="skills",
        skills=["Python", "FastAPI", "Machine Learning"],
        experience_years=None,
        availability=None,
        salary_lpa=None,
        is_missing=False,
        is_vague=False,
        is_off_topic=False
    )

    assert result["skills"] == [
        "Python",
        "FastAPI",
        "Machine Learning"
    ]

    print("Skills test: PASSED")


def test_availability_answer():
    result = integrate_screening_result(
        answer="I can join immediately.",
        intent="availability",
        skills=[],
        experience_years=None,
        availability="immediate",
        salary_lpa=None,
        is_missing=False,
        is_vague=False,
        is_off_topic=False
    )

    assert result["availability"] == "immediate"

    print("Availability test: PASSED")


def test_salary_answer():
    result = integrate_screening_result(
        answer="My expected salary is 6 LPA.",
        intent="salary_expectation",
        skills=[],
        experience_years=None,
        availability=None,
        salary_lpa=6.0,
        is_missing=False,
        is_vague=False,
        is_off_topic=False
    )

    assert result["salary_lpa"] == 6.0

    print("Salary test: PASSED")


def test_missing_answer():
    result = integrate_screening_result(
        answer="",
        intent="missing_answer",
        skills=[],
        experience_years=None,
        availability=None,
        salary_lpa=None,
        is_missing=True,
        is_vague=False,
        is_off_topic=False
    )

    assert result["is_missing"] is True

    print("Missing answer test: PASSED")


def test_off_topic_answer():
    result = integrate_screening_result(
        answer="I like watching movies.",
        intent="unknown",
        skills=[],
        experience_years=None,
        availability=None,
        salary_lpa=None,
        is_missing=False,
        is_vague=False,
        is_off_topic=True
    )

    assert result["is_off_topic"] is True

    print("Off-topic test: PASSED")


def test_vague_answer():
    result = integrate_screening_result(
        answer="Maybe I can join.",
        intent="availability",
        skills=[],
        experience_years=None,
        availability=None,
        salary_lpa=None,
        is_missing=False,
        is_vague=True,
        is_off_topic=False
    )

    assert result["is_vague"] is True

    print("Vague answer test: PASSED")


if __name__ == "__main__":

    print("=" * 60)
    print("FINAL INTEGRATION TEST")
    print("=" * 60)

    test_experience_answer()
    test_skills_answer()
    test_availability_answer()
    test_salary_answer()
    test_missing_answer()
    test_off_topic_answer()
    test_vague_answer()

    print("=" * 60)
    print("ALL FINAL INTEGRATION TESTS PASSED")
    print("=" * 60)