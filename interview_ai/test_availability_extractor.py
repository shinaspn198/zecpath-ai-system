from availability_extractor import extract_availability


test_answers = [
    "I can join immediately.",
    "I am available right away.",
    "I can join within 15 days.",
    "I have a 30 day notice period.",
    "I can join after two weeks.",
    "I can join in one week.",
    "I have a notice period.",
    "I am available next month.",
    "",
]


for answer in test_answers:

    availability = extract_availability(answer)

    print("Answer:", answer)
    print("Availability:", availability)
    print("-" * 60)