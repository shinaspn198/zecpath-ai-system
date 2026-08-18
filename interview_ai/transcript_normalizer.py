import re


def normalize_transcript(text: str) -> str:
    text = text.strip()

    # Remove common filler words
    filler_words = r"\b(um|uh|uhh|hmm|erm)\b"
    text = re.sub(filler_words, "", text, flags=re.IGNORECASE)

    # Remove leftover dots from filler expressions
    text = re.sub(r"\.{2,}", "", text)

    # Remove repeated spaces
    text = re.sub(r"\s+", " ", text)

    # Remove spaces before punctuation
    text = re.sub(r"\s+([,.!?])", r"\1", text)

    return text.strip()