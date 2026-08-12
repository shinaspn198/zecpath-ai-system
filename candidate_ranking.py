candidates = [
    {"name": "John", "score": 88},
    {"name": "Alice", "score": 95},
    {"name": "David", "score": 76},
    {"name": "Sarah", "score": 84},
    {"name": "Michael", "score": 68}
]

# Sort candidates by score
ranked_candidates = sorted(
    candidates,
    key=lambda candidate: candidate["score"],
    reverse=True
)

print("=" * 60)
print("          CANDIDATE RANKING REPORT")
print("=" * 60)

shortlisted = []
review = []
rejected = []

for rank, candidate in enumerate(ranked_candidates, start=1):

    score = candidate["score"]

    # Use the same thresholds as the Shortlisting API
    if score >= 70:
        status = "Shortlisted"
        shortlisted.append(candidate["name"])

    elif score >= 50:
        status = "Review"
        review.append(candidate["name"])

    else:
        status = "Rejected"
        rejected.append(candidate["name"])

    print(f"{rank}. {candidate['name']:<10} {score}%   {status}")

print("\n" + "=" * 60)

print(f"Total Candidates : {len(candidates)}")
print(f"Shortlisted      : {len(shortlisted)}")
print(f"Review           : {len(review)}")
print(f"Rejected         : {len(rejected)}")

print("\nTop Candidate :", ranked_candidates[0]["name"])
print("=" * 60)