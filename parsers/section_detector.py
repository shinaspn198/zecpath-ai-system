from parsers.section_rules import SECTION_RULES


class SectionDetector:
    """
    Detects and separates resume sections based on common headings.
    """

    def __init__(self):
        self.section_rules = SECTION_RULES

    def detect_sections(self, text: str):
        sections = {}
        current_section = "general"

        sections[current_section] = []

        lines = text.split("\n")

        for line in lines:
            line = line.strip()

            if not line:
                continue

            lower_line = line.lower()

            found = False

            # Check whether this line is a section heading
            for section, headings in self.section_rules.items():
                if lower_line in headings:
                    current_section = section

                    if current_section not in sections:
                        sections[current_section] = []

                    found = True
                    break

            if not found:
                sections[current_section].append(line)

        return sections