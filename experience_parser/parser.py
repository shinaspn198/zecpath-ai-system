import re

def extract_experience(text):
    pattern = r"WORK EXPERIENCE(.*)"
    match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)

    if match:
        return match.group(1).strip()

    return None


def parse_experience(experience_text):
    lines = [line.strip() for line in experience_text.split("\n") if line.strip()]

    experiences = []

    i = 0

    while i < len(lines):

        if i + 2 < len(lines):

            role = lines[i]
            company = lines[i + 1]
            duration = lines[i + 2]

            experiences.append({
                "Job Title": role,
                "Company": company,
                "Duration": duration
            })

            i += 4

        else:
            break

    return experiences