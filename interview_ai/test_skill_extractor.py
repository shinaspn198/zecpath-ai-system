from skill_extractor import extract_skills


test_answers = [
    "I am skilled in Python, FastAPI and Machine Learning.",
    "I have experience working with Python and Pandas.",
    "I know React, JavaScript and SQL.",
    "I have worked with TensorFlow and PyTorch.",
    "I like watching movies.",
    "",
]


for answer in test_answers:

    skills = extract_skills(answer)

    print("Answer:", answer)
    print("Skills:", skills)
    print("-" * 60)