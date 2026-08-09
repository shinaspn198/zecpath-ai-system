from fastapi import APIRouter, HTTPException

from api.schemas import ScoringRequest, ScoringResponse
from ats_score import calculate_ats_score


router = APIRouter(
    prefix="/api/score",
    tags=["Scoring"]
)


@router.post("/", response_model=ScoringResponse)
async def calculate_score(request: ScoringRequest):

    if not request.candidate_id:
        raise HTTPException(
            status_code=400,
            detail="Candidate ID is required"
        )

    try:
        ats_score = calculate_ats_score(
            role=request.role,
            skill_match=request.skill_match,
            experience_relevance=request.experience_relevance,
            education_alignment=request.education_alignment,
            semantic_similarity=request.semantic_similarity
        )

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

    return ScoringResponse(
        candidate_id=request.candidate_id,
        ats_score=ats_score,
        status="scored",
        message="Candidate scored successfully"
    )