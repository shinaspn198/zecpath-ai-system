"""
Day 26 - Step 5
Score Interpretation Testing
"""

from score_interpreter import interpret_screening_score


print("=" * 60)
print("DAY 26 - STEP 5 SCORE INTERPRETATION TEST")
print("=" * 60)


# Test 1 - Excellent
result = interpret_screening_score(92)

print("Test 1 - Excellent")
print(result)

assert result["category"] == "excellent"
assert result["label"] == "Excellent"


# Test 2 - Good
result = interpret_screening_score(78)

print("\nTest 2 - Good")
print(result)

assert result["category"] == "good"
assert result["label"] == "Good"


# Test 3 - Average
result = interpret_screening_score(65)

print("\nTest 3 - Average")
print(result)

assert result["category"] == "average"
assert result["label"] == "Average"


# Test 4 - Weak
result = interpret_screening_score(40)

print("\nTest 4 - Weak")
print(result)

assert result["category"] == "weak"
assert result["label"] == "Weak"


# Test 5 - Boundary: Excellent
result = interpret_screening_score(85)

print("\nTest 5 - Excellent Boundary")
print(result)

assert result["category"] == "excellent"


# Test 6 - Boundary: Good
result = interpret_screening_score(70)

print("\nTest 6 - Good Boundary")
print(result)

assert result["category"] == "good"


# Test 7 - Boundary: Average
result = interpret_screening_score(50)

print("\nTest 7 - Average Boundary")
print(result)

assert result["category"] == "average"


# Test 8 - Invalid score
try:

    interpret_screening_score(120)

    print("\nTest 8 - Invalid Score: FAILED")

except ValueError:

    print("\nTest 8 - Invalid Score: PASSED")


print("=" * 60)
print("STEP 5 TEST: PASSED")
print("=" * 60)