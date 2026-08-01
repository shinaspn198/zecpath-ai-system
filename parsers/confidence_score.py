class ConfidenceScorer:
    """
    Assigns confidence scores to extracted skills.
    """

    def score_skills(self, skills):

        scores = []

        for skill in skills:

            # Default confidence
            confidence = 0.90

            # Higher confidence for well-known technologies
            if skill in [
                "Python",
                "Java",
                "JavaScript",
                "SQL",
                "React",
                "TensorFlow",
                "Docker",
                "FastAPI",
                "PostgreSQL"
            ]:
                confidence = 0.99

            elif skill in [
                "Machine Learning",
                "Artificial Intelligence",
                "Natural Language Processing"
            ]:
                confidence = 0.97

            scores.append({
                "skill": skill,
                "confidence": round(confidence, 2)
            })

        return scores