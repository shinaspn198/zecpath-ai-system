import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from parsers.resume_parser import parse_resume

sample_resume = """
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

result = parse_resume(sample_resume)

print(result)