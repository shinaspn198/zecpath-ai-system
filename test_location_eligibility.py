from eligibility_engine.eligibility_config import get_job_rules
from eligibility_engine.eligibility_engine import check_location


rules = get_job_rules("AI Engineer")

result = check_location(
    "Bangalore",
    rules["location"]
)

print(result)