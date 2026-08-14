from eligibility_engine.eligibility_config import get_job_rules


rules = get_job_rules("AI Engineer")

print("Minimum ATS Score:", rules["minimum_ats_score"])
print("Mandatory Skills:", rules["mandatory_skills"])
print("Experience:", rules["experience"])
print("Location:", rules["location"])
print("Availability:", rules["availability"])