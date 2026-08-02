from datetime import datetime

def detect_gaps(profile):

    gaps = []

    jobs = []

    for exp in profile:

        start_str, end_str = exp["Duration"].split(" - ")

        start = datetime.strptime(start_str, "%B %Y")
        end = datetime.strptime(end_str, "%B %Y")

        jobs.append((start, end))

    # Sort by start date
    jobs.sort()

    for i in range(len(jobs) - 1):

        current_end = jobs[i][1]
        next_start = jobs[i + 1][0]

        gap_months = (next_start.year - current_end.year) * 12
        gap_months += next_start.month - current_end.month

        if gap_months > 1:
            gaps.append({
                "Gap After": current_end.strftime("%B %Y"),
                "Gap Before": next_start.strftime("%B %Y"),
                "Months": gap_months - 1
            })

    return gaps