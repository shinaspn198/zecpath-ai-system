import re

def extract_dates(text):
    """
    Extract employment date ranges like:
    January 2022 - March 2024
    """

    pattern = r"(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4}\s*-\s*(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4}"

    matches = re.finditer(pattern, text)

    dates = []

    for match in matches:
        dates.append(match.group())

    return dates