import json
from pathlib import Path


DATA_FILE = Path("data/hr_screening_questions.json")


def load_questions():
    """Load HR screening questions from the dataset."""
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    return data["questions"]


def get_questions_by_category(category):
    """Return questions belonging to a specific category."""
    questions = load_questions()

    return [
        question
        for question in questions
        if question["category"].lower() == category.lower()
    ]


def get_mandatory_questions():
    """Return only mandatory screening questions."""
    questions = load_questions()

    return [
        question
        for question in questions
        if question["mandatory"] is True
    ]


def build_conversation_objects():
    """Convert dataset questions into AI conversation-ready objects."""
    questions = load_questions()

    conversation_objects = []

    for question in questions:
        conversation_objects.append({
            "question_id": question["question_id"],
            "category": question["category"],
            "prompt": question["question"],
            "expected_answer_type": question["expected_answer_type"],
            "mandatory": question["mandatory"],
            "scoring_importance": question["scoring_importance"]
        })

    return conversation_objects


if __name__ == "__main__":
    conversation = build_conversation_objects()

    print("AI Conversation Objects:", len(conversation))

    for question in conversation[:5]:
        print(question)