"""
Day 26 - Step 3
Score Normalization Testing
"""

from screening_scorer import normalize_score


print("=" * 60)
print("DAY 26 - STEP 3 SCORE NORMALIZATION TEST")
print("=" * 60)


# Test 1
score = normalize_score(93, 100)

print("Test 1 - 93/100")
print("Normalized Score:", score)

assert score == 93.0


# Test 2
score = normalize_score(45, 50)

print("\nTest 2 - 45/50")
print("Normalized Score:", score)

assert score == 90.0


# Test 3
score = normalize_score(75, 80)

print("\nTest 3 - 75/80")
print("Normalized Score:", score)

assert score == 93.75


# Test 4
score = normalize_score(0, 100)

print("\nTest 4 - 0/100")
print("Normalized Score:", score)

assert score == 0.0


# Test 5 - Invalid score
try:

    normalize_score(110, 100)

    print("\nTest 5 - Invalid Score: FAILED")

except ValueError:

    print("\nTest 5 - Invalid Score: PASSED")


# Test 6 - Invalid maximum score
try:

    normalize_score(50, 0)

    print("Test 6 - Invalid Maximum Score: FAILED")

except ValueError:

    print("Test 6 - Invalid Maximum Score: PASSED")


print("=" * 60)
print("STEP 3 TEST: PASSED")
print("=" * 60)