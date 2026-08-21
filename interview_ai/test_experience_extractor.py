from experience_extractor import extract_experience_years


test_answers = [
    "I have 2 years of experience in Python.",
    "I have 3.5 years of experience as a Python developer.",
    "I worked for 5 years in software development.",
    "I have 1 year of experience.",
    "I am a fresher.",
    "",
]


for answer in test_answers:

    experience = extract_experience_years(answer)

    print("Answer:", answer)
    print("Experience Years:", experience)
    print("-" * 60)