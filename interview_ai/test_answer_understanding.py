from answer_understanding import understand_answer


test_answers = [
    "I have 2 years of experience in Python.",
    "I am skilled in Python, FastAPI and Machine Learning.",
    "I can join immediately.",
    "My expected salary is 6 LPA.",
    "My name is Shinas and I am an AI Engineer.",
    "",
    "I like watching movies.",
]


for answer in test_answers:

    result = understand_answer(answer)

    print("Answer:", answer)
    print("Understanding:", result)
    print("-" * 60)