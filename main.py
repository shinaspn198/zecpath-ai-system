from utils.logger import get_logger
from parsers.resume_parser import parse_resume
from ats_engine.ats_model import calculate_ats_score
from scoring.score_engine import final_score


logger = get_logger()


logger.info("Starting Zecpath AI Pipeline")


# Step 1: Parse Resume
candidate = parse_resume("resume.pdf")

logger.info("Resume Parsed Successfully")


# Step 2: ATS Analysis
skills = candidate["skills"]

ats_score = calculate_ats_score(skills)

logger.info(f"ATS Score Generated: {ats_score}")


# Step 3: Interview Score (sample)
interview_score = 80


# Step 4: Final Decision Score
overall_score = final_score(
    ats_score,
    interview_score
)


logger.info(
    f"Final Candidate Score: {overall_score}"
)


print("Candidate:", candidate)
print("ATS Score:", ats_score)
print("Final Score:", overall_score)