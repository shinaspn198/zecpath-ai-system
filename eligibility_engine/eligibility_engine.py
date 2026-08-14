from eligibility_engine.eligibility_config import get_job_rules

def check_availability(candidate_availability, allowed_availability):
    """
    Check whether the candidate's availability
    matches the configured availability options.
    """

    allowed = {
        availability.strip().lower()
        for availability in allowed_availability
    }

    candidate_availability = candidate_availability.strip().lower()

    passed = candidate_availability in allowed

    return {
        "passed": passed,
        "status": "pass" if passed else "fail",
        "candidate_availability": candidate_availability,
        "allowed_availability": sorted(allowed)
    }

def check_location(candidate_location, allowed_locations):
    """
    Check whether the candidate location
    is allowed for the job.
    """

    allowed = {
        location.strip().lower()
        for location in allowed_locations
    }

    candidate_location = candidate_location.strip().lower()

    passed = candidate_location in allowed

    return {
        "passed": passed,
        "status": "pass" if passed else "fail",
        "candidate_location": candidate_location,
        "allowed_locations": sorted(allowed)
    }

def check_experience(experience_years, experience_rules):
    """
    Check whether candidate experience
    falls within the configured range.
    """

    min_years = experience_rules["min_years"]
    max_years = experience_rules["max_years"]

    passed = min_years <= experience_years <= max_years

    return {
        "passed": passed,
        "status": "pass" if passed else "fail",
        "candidate_experience": experience_years,
        "minimum_required": min_years,
        "maximum_allowed": max_years
    }

def check_mandatory_skills(candidate_skills, mandatory_skills):
    """
    Check whether the candidate has all mandatory skills.
    """

    candidate_skills = {
        skill.strip().lower()
        for skill in candidate_skills
    }

    mandatory_skills = {
        skill.strip().lower()
        for skill in mandatory_skills
    }

    missing_skills = mandatory_skills - candidate_skills

    return {
        "passed": len(missing_skills) == 0,
        "status": "pass" if len(missing_skills) == 0 else "fail",
        "missing_skills": sorted(missing_skills)
    }

def check_ats_score(ats_score, minimum_ats_score):
    """
    Check whether the candidate's ATS score
    meets the minimum required score.
    """

    return ats_score >= minimum_ats_score


def evaluate_ats_score(candidate_ats_score, job_role):
    """
    Evaluate a candidate's ATS score against
    the configured minimum score for the job role.
    """

    rules = get_job_rules(job_role)

    minimum_score = rules["minimum_ats_score"]

    passed = check_ats_score(
        candidate_ats_score,
        minimum_score
    )

    if passed:
        return {
            "passed": True,
            "status": "pass",
            "candidate_ats_score": candidate_ats_score,
            "minimum_required_score": minimum_score
        }

    return {
        "passed": False,
        "status": "fail",
        "candidate_ats_score": candidate_ats_score,
        "minimum_required_score": minimum_score
    }

def evaluate_candidate(candidate, job_role):
    """
    Evaluate a candidate against all configured
    eligibility rules.
    """

    rules = get_job_rules(job_role)

    ats_result = evaluate_ats_score(
        candidate["ats_score"],
        job_role
    )

    skills_result = check_mandatory_skills(
        candidate["skills"],
        rules["mandatory_skills"]
    )

    experience_result = check_experience(
        candidate["experience_years"],
        rules["experience"]
    )

    location_result = check_location(
        candidate["location"],
        rules["location"]
    )

    availability_result = check_availability(
        candidate["availability"],
        rules["availability"]
    )

    # Critical requirements
    critical_failures = []

    if not ats_result["passed"]:
        critical_failures.append("ATS score")

    if not skills_result["passed"]:
        critical_failures.append("mandatory skills")

    if not experience_result["passed"]:
        critical_failures.append("experience")

    # Recruiter-review conditions
    review_conditions = []

    if not location_result["passed"]:
        review_conditions.append("location")

    if not availability_result["passed"]:
        review_conditions.append("availability")

    # Final decision
    if critical_failures:
        decision = "Rejected"
    elif review_conditions:
        decision = "Review"
    else:
        decision = "Eligible"

    return {
        "job_role": job_role,
        "decision": decision,
        "checks": {
            "ats_score": ats_result,
            "mandatory_skills": skills_result,
            "experience": experience_result,
            "location": location_result,
            "availability": availability_result
        },
        "critical_failures": critical_failures,
        "review_conditions": review_conditions
    }
def build_eligibility_result(
    candidate_id,
    candidate,
    evaluation
):
    """
    Build the final candidate eligibility result structure.
    """

    return {
        "candidate_id": candidate_id,
        "job_role": evaluation["job_role"],
        "eligibility_status": evaluation["decision"],
        "ats_score": candidate["ats_score"],
        "critical_failures": evaluation["critical_failures"],
        "review_conditions": evaluation["review_conditions"],
        "checks": evaluation["checks"]
    }