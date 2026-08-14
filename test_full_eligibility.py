from eligibility_engine.eligibility_engine import (
    evaluate_candidate,
    build_eligibility_result
)


candidate = {
    "ats_score": 82,
    "skills": [
        "Python",
        "Machine Learning",
        "FastAPI"
    ],
    "experience_years": 2,
    "location": "Bangalore",
    "availability": "Immediate"
}


evaluation = evaluate_candidate(
    candidate,
    "AI Engineer"
)


result = build_eligibility_result(
    "CAND-001",
    candidate,
    evaluation
)


print(result)