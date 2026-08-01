from parsers.skill_extractor import SkillExtractor
from parsers.stack_detector import StackDetector
from parsers.confidence_score import ConfidenceScorer

sections = {
    "skills": "Python, JS, Docker, ML",
    "experience": "Worked with Fast API and PostgreSQL",
    "projects": "Built AI and NLP applications using TensorFlow"
}

extractor = SkillExtractor()

result = extractor.extract_skills(sections)

print("\nDetected Skills")
print(result)

detector = StackDetector()

stacks = detector.detect_stack(result["technical_skills"])

print("\nTechnology Stack")
print(stacks)

scorer = ConfidenceScorer()

confidence = scorer.score_skills(result["technical_skills"])

print("\nSkill Confidence Scores")
for item in confidence:
 print(item)