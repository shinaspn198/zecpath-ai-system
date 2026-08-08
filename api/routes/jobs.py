from fastapi import APIRouter, BackgroundTasks

from api.jobs import create_job, jobs
from api.schemas import JobRequest, JobResponse


router = APIRouter(
    prefix="/api/jobs",
    tags=["Jobs"]
)


@router.post("/", response_model=JobResponse)
async def start_ats_job(
    request: JobRequest,
    background_tasks: BackgroundTasks
):
    return create_job(
        background_tasks,
        request.candidate_id
    )


@router.get("/{job_id}")
async def get_job_status(job_id: str):

    if job_id not in jobs:
        return {
            "job_id": job_id,
            "status": "not_found",
            "message": "Job not found"
        }

    return jobs[job_id]