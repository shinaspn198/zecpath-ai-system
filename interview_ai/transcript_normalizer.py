import re


def normalize_transcript(text):
    text = text.strip()

    filler_words = [
        "uh",
        "uhh",
        "um",
        "umm",
        "er",
        "err"
    ]

    for word in filler_words:
        text = re.sub(rf"\b{word}\b", "", text, flags=re.IGNORECASE)

    text = re.sub(r"\s+", " ", text).strip()

    # Remove dots/punctuation left at the beginning
    text = re.sub(r"^[.,!?]+\s*", "", text)

    # Remove spaces before punctuation
    text = re.sub(r"\s+([,.!?])", r"\1", text)

    # Remove repeated punctuation
    text = re.sub(r"\.{2,}", ".", text)

    if text:
        text = text[0].upper() + text[1:]

    return text