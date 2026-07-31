import os
import sys

# Add the project root to Python's import path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from parsers.section_detector import SectionDetector

sample = """
John Smith

SKILLS

Python
Java
Machine Learning

WORK EXPERIENCE

ABC Technologies
AI Intern

EDUCATION

BCA Artificial Intelligence

PROJECTS

Fraud Detection System
Resume Parser

CERTIFICATIONS

Google Data Analytics
"""

detector = SectionDetector()
result = detector.detect_sections(sample)

for section, content in result.items():
    print(f"\n===== {section.upper()} =====")
    for item in content:
        print(item)