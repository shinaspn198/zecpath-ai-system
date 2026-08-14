from eligibility_engine.eligibility_config import get_job_rules
from eligibility_engine.eligibility_engine import check_availability


rules = get_job_rules("AI Engineer")

result = check_availability(
    "Immediate",
    rules["availability"]
)

print(result)