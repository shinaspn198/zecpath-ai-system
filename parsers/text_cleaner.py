import re


class TextCleaner:
    """
    Cleans extracted resume text before section detection.
    """

    @staticmethod
    def clean(text: str) -> str:
        if not text:
            return ""

        # Normalize line endings
        text = text.replace("\r\n", "\n").replace("\r", "\n")

        # Replace multiple spaces/tabs with a single space
        text = re.sub(r"[ \t]+", " ", text)

        # Remove excessive blank lines
        text = re.sub(r"\n\s*\n+", "\n\n", text)

        # Remove leading/trailing whitespace
        text = text.strip()

        return text