from dataclasses import dataclass
from datetime import datetime


@dataclass
class Transcript:
    transcript_id: str
    candidate_id: str
    job_id: str
    question_id: str
    speaker: str
    transcript_text: str
    timestamp: datetime
    confidence: float