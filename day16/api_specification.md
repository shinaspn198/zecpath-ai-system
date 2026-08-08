# Day 16 – ATS API Specification

## Objective

To make ATS AI consumable by backend systems.

---

## 1. Resume Upload API

### Endpoint

POST /api/resume/upload

### Purpose

Uploads a candidate resume for ATS processing.

### Request

Content-Type: multipart/form-data

Input:

* resume: PDF or DOCX file

### Response

```json
{
  "candidate_id": "CAND-001",
  "filename": "resume.pdf",
  "status": "uploaded",
  "message": "Resume uploaded successfully"
}
```

---

## 2. Resume Parsing API

### Endpoint

POST /api/resume/parse

### Purpose

Extracts and structures important information from an uploaded resume.

### Request

Content-Type: application/json

```json
{
  "candidate_id": "CAND-001"
}
```

### Response

```json
{
  "candidate_id": "CAND-001",
  "status": "parsed",
  "profile": {
    "name": "Candidate Name",
    "skills": ["Python", "Machine Learning"],
    "experience": [],
    "education": [],
    "certifications": []
  }
}
```

---

## 3. Job Description Parsing API

### Endpoint

POST /api/job/parse

### Purpose

Converts a job description into structured job requirements.

### Request

Content-Type: application/json

```json
{
  "job_id": "JOB-001",
  "description": "Looking for a Python developer with machine learning experience."
}
```

### Response

```json
{
  "job_id": "JOB-001",
  "status": "parsed",
  "requirements": {
    "skills": ["Python", "Machine Learning"],
    "experience": "2+ years",
    "education": "Bachelor's degree"
  }
}
```

---

## 4. Skill Extraction API

### Endpoint

POST /api/resume/skills

### Purpose

Extracts and normalizes technical and professional skills from a candidate profile.

### Request

Content-Type: application/json

```json
{
  "candidate_id": "CAND-001"
}
```

### Response

```json
{
  "candidate_id": "CAND-001",
  "skills": [
    {
      "name": "Python",
      "normalized_name": "python",
      "confidence": 0.98
    },
    {
      "name": "Machine Learning",
      "normalized_name": "machine learning",
      "confidence": 0.95
    }
  ]
}
```

---

## 5. Experience Parsing API

### Endpoint

POST /api/resume/experience

### Purpose

Extracts candidate work experience and evaluates its relevance to the target job.

### Request

Content-Type: application/json

```json
{
  "candidate_id": "CAND-001",
  "job_id": "JOB-001"
}
```

### Response

```json
{
  "candidate_id": "CAND-001",
  "experience_relevance": 80,
  "experience": [
    {
      "role": "AI Intern",
      "company": "Example Company",
      "years": 2
    }
  ]
}
```

---

## 6. Education & Certification API

### Endpoint

POST /api/resume/education

### Purpose

Extracts academic qualifications and professional certifications from the candidate resume.

### Request

Content-Type: application/json

```json
{
  "candidate_id": "CAND-001"
}
```

### Response

```json
{
  "candidate_id": "CAND-001",
  "education": [
    {
      "degree": "BCA",
      "field": "Artificial Intelligence",
      "graduation_year": 2026
    }
  ],
  "certifications": [
    "Python Certification"
  ]
}
```

---

## 7. Semantic Matching API

### Endpoint

POST /api/matching/semantic

### Purpose

Calculates semantic similarity between a candidate resume and a target job description.

### Request

Content-Type: application/json

```json
{
  "candidate_id": "CAND-001",
  "job_id": "JOB-001"
}
```

### Response

```json
{
  "candidate_id": "CAND-001",
  "job_id": "JOB-001",
  "semantic_similarity": 85
}
```

---

## 8. ATS Scoring API

### Endpoint

POST /api/ats/score

### Purpose

Calculates a transparent ATS score using weighted candidate evaluation parameters.

### Request

Content-Type: application/json

```json
{
  "candidate_id": "CAND-001",
  "job_id": "JOB-001"
}
```

### Response

```json
{
  "candidate_id": "CAND-001",
  "job_id": "JOB-001",
  "ats_score": 71.75,
  "components": {
    "skill_match": 90,
    "experience_relevance": 80,
    "education_alignment": 100,
    "semantic_similarity": 85
  }
}
```

---

## 9. Candidate Ranking API

### Endpoint

POST /api/candidates/rank

### Purpose

Ranks candidates according to their ATS scores.

### Request

Content-Type: application/json

```json
{
  "job_id": "JOB-001"
}
```

### Response

```json
{
  "job_id": "JOB-001",
  "ranked_candidates": [
    {
      "candidate_id": "CAND-001",
      "rank": 1,
      "ats_score": 91.5
    },
    {
      "candidate_id": "CAND-002",
      "rank": 2,
      "ats_score": 84.2
    }
  ]
}
```

---

## 10. Candidate Shortlisting API

### Endpoint

POST /api/candidates/shortlist

### Purpose

Classifies candidates using configurable ATS score thresholds.

### Request

Content-Type: application/json

```json
{
  "job_id": "JOB-001",
  "candidate_id": "CAND-001"
}
```

### Response

```json
{
  "candidate_id": "CAND-001",
  "ats_score": 91.5,
  "status": "Shortlisted"
}
```

---

## 11. Fairness Evaluation API

### Endpoint

POST /api/fairness/check

### Purpose

Checks candidate data for sensitive fields and supports fair AI-based candidate evaluation.

### Request

Content-Type: application/json

```json
{
  "candidate_id": "CAND-001"
}
```

### Response

```json
{
  "candidate_id": "CAND-001",
  "sensitive_fields_detected": [
    "name",
    "gender",
    "age"
  ],
  "fairness_status": "PASS"
}
```

---

## 12. API Status Codes

| Status Code | Meaning                        |
| ----------- | ------------------------------ |
| 200         | Request processed successfully |
| 201         | Resource created successfully  |
| 400         | Invalid request                |
| 404         | Resource not found             |
| 422         | Validation error               |
| 500         | Internal server error          |

---

## 13. ATS API Workflow

```text
Resume Upload
      ↓
Resume Parsing
      ↓
Section Segmentation
      ↓
Skill Extraction
      ↓
Experience Parsing
      ↓
Education & Certification Parsing
      ↓
Resume ↔ Job Semantic Matching
      ↓
ATS Score Calculation
      ↓
Candidate Ranking
      ↓
Candidate Shortlisting
      ↓
Fairness Evaluation
      ↓
Recruiter Decision
```

---

## 14. API Design Principles

* REST-based API architecture
* JSON-based request and response formats
* Unique Candidate ID and Job ID
* Modular AI service integration
* Consistent HTTP status codes
* Structured machine-readable responses
* Explainable ATS scoring
* Configurable candidate shortlisting
* Fairness-aware candidate processing

---

## Conclusion

The Day 16 ATS API specification defines how the Zecpath AI recruitment modules can be exposed as backend APIs.

The specification connects resume processing, job parsing, skill extraction, experience analysis, education evaluation, semantic matching, ATS scoring, candidate ranking, shortlisting, and fairness evaluation into a structured API workflow.

This design enables the AI recruitment system to communicate with frontend applications, backend services, recruiter dashboards, and other external systems.
