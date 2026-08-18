from dataclasses import dataclass
from datetime import datetime


@dataclass
class ScreeningInteraction:
    interaction_id: str
    candidate_id: str
    job_id: str
    question_id: str
    transcript_id: str
    answer_text: str
    timestamp: datetime
    confidence: float