import os
import sys
import json

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from parsers.resume_parser import parse_resume

resume = "data/sample_resumes/sample_resume.pdf"

candidate = parse_resume(resume)

os.makedirs("output", exist_ok=True)

with open("output/candidate_profile.json", "w", encoding="utf-8") as f:
    json.dump(candidate, f, indent=4, ensure_ascii=False)

print("Candidate profile exported successfully!")