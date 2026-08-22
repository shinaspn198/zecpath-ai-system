"""
Day 26 - Step 4
Overall Screening Score Testing
"""

from overall_screening_score import calculate_overall_score


print("=" * 60)
print("DAY 26 - STEP 4 OVERALL SCREENING SCORE TEST")
print("=" * 60)


# Test 1 - Strong candidate
question_scores = [
    {
        "total_score": 93,
        "max_score": 100
    },
    {
        "total_score": 90,
        "max_score": 100
    },
    {
        "total_score": 95,
        "max_score": 100
    }
]

result = calculate_overall_score(question_scores)

print("Test 1 - Strong Candidate")
print(result)

assert result["total_score"] == 278
assert result["maximum_score"] == 300
assert result["overall_score"] == 92.67
assert result["questions_evaluated"] == 3


# Test 2 - Average candidate
question_scores = [
    {
        "total_score": 70,
        "max_score": 100
    },
    {
        "total_score": 65,
        "max_score": 100
    },
    {
        "total_score": 75,
        "max_score": 100
    }
]

result = calculate_overall_score(question_scores)

print("\nTest 2 - Average Candidate")
print(result)

assert result["total_score"] == 210
assert result["maximum_score"] == 300
assert result["overall_score"] == 70.0


# Test 3 - Weak candidate
question_scores = [
    {
        "total_score": 40,
        "max_score": 100
    },
    {
        "total_score": 35,
        "max_score": 100
    },
    {
        "total_score": 45,
        "max_score": 100
    }
]

result = calculate_overall_score(question_scores)

print("\nTest 3 - Weak Candidate")
print(result)

assert result["total_score"] == 120
assert result["maximum_score"] == 300
assert result["overall_score"] == 40.0


# Test 4 - Empty list validation
try:

    calculate_overall_score([])

    print("\nTest 4 - Empty Scores: FAILED")

except ValueError:

    print("\nTest 4 - Empty Scores: PASSED")


# Test 5 - Invalid input validation
try:

    calculate_overall_score("invalid")

    print("Test 5 - Invalid Input: FAILED")

except TypeError:

    print("Test 5 - Invalid Input: PASSED")


print("=" * 60)
print("STEP 4 TEST: PASSED")
print("=" * 60)