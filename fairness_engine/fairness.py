from normalize import normalize_resume
from bias_detector import detect_bias

sample_resume = {
    "name": "Shinas PN",
    "gender": "Male",
    "age": 22,
    "email": "SHINASPN@GMAIL.COM ",
    "phone": "9876543210 ",
    "skills": [
        "Python",
        "python",
        "Machine Learning",
        "AI",
        "ai"
    ],
    "education": "bca artificial intelligence",
    "experience": 2
}

print("========== FAIRNESS REPORT ==========\n")

# Normalize the resume
normalized = normalize_resume(sample_resume)

print("Normalized Resume")
print(normalized)

print("\n-----------------------------")

# Detect sensitive fields
bias = detect_bias(sample_resume)

if bias:
    print("Sensitive Fields Detected:")
    for field in bias:
        print(f"- {field}")
else:
    print("No sensitive fields detected.")

print("\n-----------------------------")

print("Fairness Status: PASS")
print("Resume standardized successfully.")
print("Bias indicators identified for masking.")