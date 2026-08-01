from parsers.technology_stack import TECHNOLOGY_STACK


class StackDetector:

    def detect_stack(self, skills):

        stacks = {}

        for category, technologies in TECHNOLOGY_STACK.items():

            detected = []

            for tech in technologies:

                if tech in skills:
                    detected.append(tech)

            if detected:
                stacks[category] = detected

        return stacks