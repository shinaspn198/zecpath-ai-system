import re

from parsers.skill_dictionary import (
    TECHNICAL_SKILLS,
    BUSINESS_SKILLS,
    CREATIVE_SKILLS,
)

from parsers.skill_synonyms import SKILL_SYNONYMS


class SkillExtractor:
    """
    Extracts categorized skills from segmented resume sections.
    """

    def __init__(self):
        self.technical = TECHNICAL_SKILLS
        self.business = BUSINESS_SKILLS
        self.creative = CREATIVE_SKILLS

    def extract_skills(self, sections):
        """
        Extract skills from the segmented resume.
        """

        text = " ".join([
            sections.get("skills", ""),
            sections.get("experience", ""),
            sections.get("projects", "")
        ]).lower()

        # Normalize synonyms
        for alias, canonical in SKILL_SYNONYMS.items():
            pattern = r"\b" + re.escape(alias.lower()) + r"\b"
            text = re.sub(pattern, canonical.lower(), text)

        print("\nNormalized Resume Text:")
        print(text)

        technical = []
        business = []
        creative = []

        # Technical Skills
        for skill in self.technical:
            pattern = r"\b" + re.escape(skill.lower()) + r"\b"
            if re.search(pattern, text):
                technical.append(skill)

        # Business Skills
        for skill in self.business:
            pattern = r"\b" + re.escape(skill.lower()) + r"\b"
            if re.search(pattern, text):
                business.append(skill)

        # Creative Skills
        for skill in self.creative:
            pattern = r"\b" + re.escape(skill.lower()) + r"\b"
            if re.search(pattern, text):
                creative.append(skill)

        return {
            "technical_skills": sorted(set(technical)),
            "business_skills": sorted(set(business)),
            "creative_skills": sorted(set(creative)),
        }