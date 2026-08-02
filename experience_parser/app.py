from parser import extract_experience
from experience_engine import build_experience_profile
from relevance import calculate_relevance
from gap_detector import detect_gaps
from overlap_detector import detect_overlaps

with open("sample_resume.txt", "r", encoding="utf-8") as file:
    resume = file.read()

experience = extract_experience(resume)

profile = build_experience_profile(experience)

print("\n===== EXPERIENCE PROFILE =====\n")

for item in profile:
    print(item)

target_role = "AI Engineer"

score = calculate_relevance(target_role, profile)

print("\n===== EXPERIENCE RELEVANCE =====")
print(f"Target Role     : {target_role}")
print(f"Relevance Score : {score}%")

gaps = detect_gaps(profile)

print("\n===== EMPLOYMENT GAPS =====")

if gaps:
    for gap in gaps:
        print(gap)
else:
    print("No employment gaps detected.")


overlaps = detect_overlaps(profile)

print("\n===== EMPLOYMENT OVERLAPS =====")

if overlaps:
    for overlap in overlaps:
        print(overlap)
else:
    print("No overlapping employment detected.")