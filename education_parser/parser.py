import re


def extract_education(text):
    pattern = r"EDUCATION(.*?)CERTIFICATIONS"

    match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)

    if not match:
        return []

    section = match.group(1).strip()

    lines = [line.strip() for line in section.split("\n") if line.strip()]

    education = []

    for i in range(0, len(lines), 4):
        if i + 3 < len(lines):
            education.append({
                "Degree": lines[i],
                "Institution": lines[i + 1],
                "Field": lines[i + 2],
                "Graduation Year": lines[i + 3]
            })

    return education