# Day 16 – ATS API Architecture

## Objective

To define how the Zecpath AI ATS APIs communicate with frontend applications,
backend services, AI processing modules, databases, and recruiter interfaces.

---

## 1. Architecture Overview

The Zecpath AI ATS uses a modular API architecture where frontend
applications communicate with backend APIs.

The backend APIs connect the request to the appropriate AI processing
module and return structured responses.

---

## 2. High-Level Architecture

```text
                    Recruiter / User
                           |
                           ↓
                  Frontend Application
                           |
                           ↓
                    REST API Layer
                           |
        +------------------+------------------+
        |                  |                  |
        ↓                  ↓                  ↓
 Resume APIs         Job APIs          Candidate APIs
        |                  |                  |
        ↓                  ↓                  ↓
 Resume AI          Job Parsing AI     Candidate AI
 Processing          Processing         Processing
        |                  |                  |
        +------------------+------------------+
                           |
                           ↓
                    ATS AI Pipeline
                           |
        +------------------+------------------+
        |                  |                  |
        ↓                  ↓                  ↓
   Skill Engine      Matching Engine    Scoring Engine
        |                  |                  |
        +------------------+------------------+
                           |
                           ↓
                  Ranking & Shortlisting
                           |
                           ↓
                    Recruiter Report