from parser import extract_education
from certification import extract_certifications
from relevance import calculate_education_relevance

with open("sample_resume.txt", "r", encoding="utf-8") as file:
    resume = file.read()

education = extract_education(resume)
certifications = extract_certifications(resume)

print("===== EDUCATION PROFILE =====\n")

for edu in education:
    print(edu)

print("\n===== CERTIFICATIONS =====\n")

for cert in certifications:
    print(cert)

score = calculate_education_relevance(education)

print("\n===== EDUCATION RELEVANCE =====")
print(f"Relevance Score : {score}%")