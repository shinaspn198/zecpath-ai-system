from eligibility_engine.eligibility_config import get_job_rules
from eligibility_engine.eligibility_engine import check_mandatory_skills


rules = get_job_rules("AI Engineer")

candidate_skills = [
    "Python",
    "Machine Learning",
    "FastAPI"
]

result = check_mandatory_skills(
    candidate_skills,
    rules["mandatory_skills"]
)

print(result)