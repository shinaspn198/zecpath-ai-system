from datetime import datetime

def detect_overlaps(profile):

    overlaps = []

    jobs = []

    for exp in profile:

        start_str, end_str = exp["Duration"].split(" - ")

        start = datetime.strptime(start_str, "%B %Y")
        end = datetime.strptime(end_str, "%B %Y")

        jobs.append({
            "job_title": exp["Job Title"],
            "company": exp["Company"],
            "start": start,
            "end": end
        })

    # Compare every job with every other job
    for i in range(len(jobs)):
        for j in range(i + 1, len(jobs)):

            if jobs[i]["start"] <= jobs[j]["end"] and jobs[j]["start"] <= jobs[i]["end"]:

                overlaps.append({
                    "Job 1": jobs[i]["job_title"],
                    "Company 1": jobs[i]["company"],
                    "Job 2": jobs[j]["job_title"],
                    "Company 2": jobs[j]["company"]
                })

    return overlaps