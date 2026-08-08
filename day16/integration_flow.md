# Day 16 – ATS API Integration Flow

## Objective

To define how the ATS APIs work together as an end-to-end recruitment processing flow.

---

## 1. Integration Flow

The Zecpath AI ATS API processes a candidate through the following sequence:

```text
Candidate Resume
       ↓
Resume Upload API
       ↓
Candidate ID Generated
       ↓
Resume Parsing API
       ↓
Structured Candidate Profile
       ↓
ATS Scoring API
       ↓
ATS Score Generated
       ↓
Shortlisting API
       ↓
Candidate Classification
       ↓
Hiring Decision