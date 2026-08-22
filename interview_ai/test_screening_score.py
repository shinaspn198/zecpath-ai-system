from screening_scorer import get_scoring_parameters


parameters = get_scoring_parameters()

print("=" * 60)
print("DAY 26 - STEP 1 SCORING PARAMETERS TEST")
print("=" * 60)

for name, details in parameters.items():
    print(f"{name.title()}:")
    print(f"  Maximum Score: {details['max_score']}")
    print(f"  Description: {details['description']}")
    print()

assert "clarity" in parameters
assert "relevance" in parameters
assert "completeness" in parameters
assert "consistency" in parameters

assert parameters["clarity"]["max_score"] == 25
assert parameters["relevance"]["max_score"] == 25
assert parameters["completeness"]["max_score"] == 25
assert parameters["consistency"]["max_score"] == 25

print("=" * 60)
print("STEP 1 TEST: PASSED")
print("=" * 60)