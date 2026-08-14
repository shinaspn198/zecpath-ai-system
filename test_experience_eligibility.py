from eligibility_engine.eligibility_config import get_job_rules
from eligibility_engine.eligibility_engine import check_experience


rules = get_job_rules("AI Engineer")

result = check_experience(
    2,
    rules["experience"]
)

print(result)