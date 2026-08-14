import json
from pathlib import Path


CONFIG_PATH = Path(__file__).parent.parent / "config" / "eligibility_rules.json"


def load_eligibility_rules():
    """Load all eligibility rules from the configuration file."""

    if not CONFIG_PATH.exists():
        raise FileNotFoundError(
            f"Eligibility configuration not found: {CONFIG_PATH}"
        )

    with open(CONFIG_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def get_job_rules(job_role):
    """Return eligibility rules for the requested job role."""

    rules = load_eligibility_rules()

    if job_role not in rules:
        raise ValueError(
            f"No eligibility rules configured for job role: {job_role}"
        )

    return rules[job_role]