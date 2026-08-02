import re
import spacy
from calculator import calculate_experience

nlp = spacy.load("en_core_web_sm")


def build_experience_profile(text):

    lines = [line.strip() for line in text.split("\n") if line.strip()]

    profile = []

    date_pattern = r"(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4}\s*-\s*(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4}"

    for i in range(len(lines)):

        if re.fullmatch(date_pattern, lines[i]):

            duration = lines[i]

            job_title = lines[i-2]

            company = lines[i-1]

            years, months = calculate_experience(duration)

            profile.append({
                "Job Title": job_title,
                "Company": company,
                "Duration": duration,
                "Experience": f"{years} Years {months} Months"
            })

    return profile