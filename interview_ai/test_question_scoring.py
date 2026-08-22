from screening_scorer import calculate_question_score


print("=" * 60)
print("DAY 26 - STEP 2 PER-QUESTION SCORING TEST")
print("=" * 60)


# Test 1: Strong candidate answer
result = calculate_question_score(
    clarity=23,
    relevance=24,
    completeness=22,
    consistency=24
)

print("Test 1 - Strong Answer")
print(result)

assert result["total_score"] == 93
assert result["max_score"] == 100


# Test 2: Average candidate answer
result = calculate_question_score(
    clarity=18,
    relevance=17,
    completeness=16,
    consistency=18
)

print("\nTest 2 - Average Answer")
print(result)

assert result["total_score"] == 69


# Test 3: Weak candidate answer
result = calculate_question_score(
    clarity=10,
    relevance=8,
    completeness=9,
    consistency=7
)

print("\nTest 3 - Weak Answer")
print(result)

assert result["total_score"] == 34


# Test 4: Invalid score
try:
    calculate_question_score(
        clarity=30,
        relevance=20,
        completeness=20,
        consistency=20
    )

    assert False, "Invalid score should raise ValueError"

except ValueError:
    print("\nTest 4 - Invalid Score: PASSED")


print("=" * 60)
print("STEP 2 TEST: PASSED")
print("=" * 60)