import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from parsers.resume_parser import parse_resume

resume_path = "data/sample_resumes/sample_resume.pdf"

result = parse_resume(resume_path)

for key, value in result.items():

    print(f"\n===== {key.upper()} =====")

    if isinstance(value, list):
        for item in value:
            print(item)
    else:
        print(value)