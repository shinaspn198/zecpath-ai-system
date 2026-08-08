from fastapi import APIRouter, HTTPException

from api.schemas import ShortlistingRequest, ShortlistingResponse


router = APIRouter(
    prefix="/api/shortlist",
    tags=["Shortlisting"]
)


@router.post("/", response_model=ShortlistingResponse)
async def shortlist_candidate(request: ShortlistingRequest):

    if not request.candidate_id:
        raise HTTPException(
            status_code=400,
            detail="Candidate ID is required"
        )

    if request.ats_score < 0 or request.ats_score > 100:
        raise HTTPException(
            status_code=400,
            detail="ATS score must be between 0 and 100"
        )

    if request.ats_score >= 70:
        status = "shortlisted"
    elif request.ats_score >= 50:
        status = "review"
    else:
        status = "rejected"

    return ShortlistingResponse(
        candidate_id=request.candidate_id,
        ats_score=request.ats_score,
        status=status,
        message="Candidate shortlisting completed"
    )