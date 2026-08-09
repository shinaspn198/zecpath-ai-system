from pydantic import BaseModel
from typing import List, Optional


class ResumeUploadResponse(BaseModel):
    candidate_id: str
    filename: str
    status: str
    message: str


class ResumeParseRequest(BaseModel):
    candidate_id: str


class ResumeParseResponse(BaseModel):
    candidate_id: str
    status: str
    profile: dict


class ScoringRequest(BaseModel):
    candidate_id: str
    role: str = "AI Engineer"
    skill_match: float
    experience_relevance: float
    education_alignment: float
    semantic_similarity: float


class ScoringResponse(BaseModel):
    candidate_id: str
    ats_score: float
    status: str
    message: str


class ShortlistingRequest(BaseModel):
    candidate_id: str
    ats_score: float


class ShortlistingResponse(BaseModel):
    candidate_id: str
    ats_score: float
    status: str
    message: str


class JobRequest(BaseModel):
    candidate_id: str


class JobResponse(BaseModel):
    job_id: str
    candidate_id: str
    status: str
    message: str