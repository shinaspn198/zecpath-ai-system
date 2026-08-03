import re

def extract_certifications(text):
    pattern = r"CERTIFICATIONS(.*)"

    match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)

    if not match:
        return []

    section = match.group(1).strip()

    certifications = [
        line.strip()
        for line in section.split("\n")
        if line.strip()
    ]

    return certifications