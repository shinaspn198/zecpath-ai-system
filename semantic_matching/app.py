from matcher import semantic_similarity

with open("sample_resume.txt", "r", encoding="utf-8") as file:
    resume = file.read()

with open("sample_job.txt", "r", encoding="utf-8") as file:
    job = file.read()

score = semantic_similarity(resume, job)

print("\n===== SEMANTIC MATCHING ENGINE =====\n")
print(f"Resume ↔ JD Similarity : {score}%")

if score >= 80:
    print("Match Status           : Excellent Match")
elif score >= 60:
    print("Match Status           : Good Match")
elif score >= 40:
    print("Match Status           : Average Match")
else:
    print("Match Status           : Low Match")