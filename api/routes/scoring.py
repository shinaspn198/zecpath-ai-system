from fastapi import APIRouter, HTTPException

from api.schemas import ScoringRequest, ScoringResponse


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

    ats_score = 0

    return ScoringResponse(
        candidate_id=request.candidate_id,
        ats_score=ats_score,
        status="scored",
        message="Candidate scored successfully"
    )