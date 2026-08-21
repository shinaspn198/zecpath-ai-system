"""
Day 25 - Vague Answer Detection

Purpose:
Detect vague or unclear answers
during HR screening.
"""


def detect_vague_answer(answer: str):
    """
    Detect whether a candidate's answer is vague.

    Args:
        answer: Candidate's response as text.

    Returns:
        True if the answer is vague, otherwise False.
    """

    if not answer or not answer.strip():
        return False

    text = answer.lower().strip()

    vague_phrases = [
        "maybe",
        "not sure",
        "i don't know",
        "don't know",
        "anything is fine",
        "anything",
        "depends",
        "it depends",
        "somewhere",
        "a lot",
        "good experience",
        "some experience",
        "i think",
        "probably",
        "perhaps",
    ]

    if any(phrase in text for phrase in vague_phrases):
        return True

    return False