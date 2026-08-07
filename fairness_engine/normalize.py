import json

def normalize_resume(resume):
    """
    Standardizes resume fields into a consistent format.
    """

    normalized = {
        "name": resume.get("name", "").strip().title(),
        "email": resume.get("email", "").strip().lower(),
        "phone": resume.get("phone", "").strip(),
        "skills": sorted(
            list(set(skill.strip().lower() for skill in resume.get("skills", [])))
        ),
        "education": resume.get("education", "").strip().title(),
        "experience": max(0, resume.get("experience", 0))
    }

    return normalized


if __name__ == "__main__":

    sample_resume = {
        "name": "shinas pn",
        "email": "SHINASPN@GMAIL.COM ",
        "phone": "9876543210 ",
        "skills": [
            "Python",
            "python",
            " Machine Learning ",
            "AI",
            "ai"
        ],
        "education": "bca artificial intelligence",
        "experience": 2
    }

    normalized_resume = normalize_resume(sample_resume)

    print("===== NORMALIZED RESUME =====")
    print(json.dumps(normalized_resume, indent=4))