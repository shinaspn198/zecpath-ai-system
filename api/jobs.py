from fastapi import BackgroundTasks
import uuid


jobs = {}


def process_ats_job(job_id: str, candidate_id: str):
    """
    Background task for ATS processing.
    """

    jobs[job_id] = {
        "job_id": job_id,
        "candidate_id": candidate_id,
        "status": "completed"
    }


def create_job(background_tasks: BackgroundTasks, candidate_id: str):

    job_id = f"JOB-{uuid.uuid4().hex[:8].upper()}"

    jobs[job_id] = {
        "job_id": job_id,
        "candidate_id": candidate_id,
        "status": "processing"
    }

    background_tasks.add_task(
        process_ats_job,
        job_id,
        candidate_id
    )

    return {
        "job_id": job_id,
        "candidate_id": candidate_id,
        "status": "processing",
        "message": "ATS job started successfully"
    }