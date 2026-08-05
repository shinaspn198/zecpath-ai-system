import json

# Load weights
with open("config/weights.json", "r") as file:
    weights = json.load(file)

# Select the role
role = "AI Engineer"
role_weights = weights[role]

# Candidate scores
candidate = {
    "skill_match": 90,
    "experience_relevance": None,   # Try changing this to 80 later
    "education_alignment": 100,
    "semantic_similarity": 85
}

# Handle missing values
for key, value in candidate.items():
    if value is None:
        candidate[key] = 0

# Calculate contribution of each parameter
skill_score = candidate["skill_match"] * role_weights["skill_match"] / 100
experience_score = candidate["experience_relevance"] * role_weights["experience_relevance"] / 100
education_score = candidate["education_alignment"] * role_weights["education_alignment"] / 100
semantic_score = candidate["semantic_similarity"] * role_weights["semantic_similarity"] / 100

# Final ATS Score
ats_score = (
    skill_score +
    experience_score +
    education_score +
    semantic_score
)

print("========== ATS SCORE REPORT ==========")
print(f"Role: {role}\n")

print(f"Skill Match           : {candidate['skill_match']}%  -> {skill_score:.2f} points")
print(f"Experience Relevance  : {candidate['experience_relevance']}%  -> {experience_score:.2f} points")
print(f"Education Alignment   : {candidate['education_alignment']}%  -> {education_score:.2f} points")
print(f"Semantic Similarity   : {candidate['semantic_similarity']}%  -> {semantic_score:.2f} points")

print("--------------------------------------")
print(f"Final ATS Score: {ats_score:.2f}%")