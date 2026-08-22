"""
Day 26 - Step 6
Final Screening Scoring Integration Test
"""

from final_screening_scorer import calculate_final_screening_result


print("=" * 60)
print("DAY 26 - STEP 6 FINAL SCREENING INTEGRATION TEST")
print("=" * 60)


# ============================================================
# Test 1 - Strong Candidate
# ============================================================

question_scores = [

    {
        "clarity": 23,
        "relevance": 24,
        "completeness": 22,
        "consistency": 24
    },

    {
        "clarity": 22,
        "relevance": 23,
        "completeness": 24,
        "consistency": 23
    },

    {
        "clarity": 24,
        "relevance": 24,
        "completeness": 23,
        "consistency": 24
    }
]


result = calculate_final_screening_result(
    question_scores
)

print("Test 1 - Strong Candidate")
print(result)

assert result["total_score"] == 280
assert result["maximum_score"] == 300
assert result["overall_score"] == 93.33
assert result["category"] == "excellent"
assert result["label"] == "Excellent"
assert result["questions_evaluated"] == 3


# ============================================================
# Test 2 - Average Candidate
# ============================================================

question_scores = [

    {
        "clarity": 18,
        "relevance": 17,
        "completeness": 16,
        "consistency": 18
    },

    {
        "clarity": 17,
        "relevance": 18,
        "completeness": 16,
        "consistency": 17
    },

    {
        "clarity": 18,
        "relevance": 17,
        "completeness": 17,
        "consistency": 18
    }
]


result = calculate_final_screening_result(
    question_scores
)

print("\nTest 2 - Average Candidate")
print(result)

assert result["total_score"] == 207
assert result["maximum_score"] == 300
assert result["overall_score"] == 69.0
assert result["category"] == "average"
assert result["label"] == "Average"
assert result["questions_evaluated"] == 3


# ============================================================
# Test 3 - Weak Candidate
# ============================================================

question_scores = [

    {
        "clarity": 10,
        "relevance": 8,
        "completeness": 9,
        "consistency": 7
    },

    {
        "clarity": 9,
        "relevance": 8,
        "completeness": 8,
        "consistency": 7
    },

    {
        "clarity": 8,
        "relevance": 9,
        "completeness": 7,
        "consistency": 8
    }
]


result = calculate_final_screening_result(
    question_scores
)

print("\nTest 3 - Weak Candidate")
print(result)

assert result["total_score"] == 98
assert result["maximum_score"] == 300
assert result["overall_score"] == 32.67
assert result["category"] == "weak"
assert result["label"] == "Weak"
assert result["questions_evaluated"] == 3


# ============================================================
# Test 4 - Empty Scores
# ============================================================

try:

    result = calculate_final_screening_result([])

    print("\nTest 4 - Empty Scores: FAILED")

    raise AssertionError(
        "Empty question scores should raise ValueError."
    )

except ValueError:

    print("\nTest 4 - Empty Scores: PASSED")


# ============================================================
# Test 5 - Invalid Input
# ============================================================

try:

    calculate_final_screening_result("invalid")

    print("Test 5 - Invalid Input: FAILED")

    raise AssertionError(
        "Invalid input should raise an exception."
    )

except (TypeError, ValueError):

    print("Test 5 - Invalid Input: PASSED")


# ============================================================
# Final Result
# ============================================================

print("=" * 60)
print("STEP 6 TEST: PASSED")
print("=" * 60)