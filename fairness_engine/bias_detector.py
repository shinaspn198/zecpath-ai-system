import json

# Fields that should not influence AI hiring decisions
SENSITIVE_FIELDS = [
    "name",
    "gender",
    "age",
    "date_of_birth",
    "religion",
    "nationality",
    "marital_status",
    "photo"
]

def detect_bias(resume):
    detected = []

    for field in SENSITIVE_FIELDS:
        if field in resume:
            detected.append(field)

    return detected


if __name__ == "__main__":

    sample_resume = {
        "name": "Shinas PN",
        "age": 22,
        "gender": "Male",
        "skills": ["Python", "Machine Learning"],
        "education": "BCA",
        "experience": 2
    }

    bias_fields = detect_bias(sample_resume)

    print("===== BIAS DETECTION REPORT =====")

    if bias_fields:
        print("Sensitive fields detected:")
        print(json.dumps(bias_fields, indent=4))
    else:
        print("No sensitive fields detected.")