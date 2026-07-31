import re


class CandidateExtractor:
    """
    Extracts candidate information from parsed resume sections.
    """

    EMAIL_PATTERN = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

    PHONE_PATTERN = r"(?:\+91[- ]?)?[6-9]\d{9}"

    @staticmethod
    def extract(sections):

        candidate = {
            "name": "",
            "email": "",
            "phone": "",
            "location": "",
            "summary": "",
            "skills": [],
            "experience": [],
            "education": [],
            "projects": [],
            "certifications": [],
            "languages": []
        }

        # ---------- General Section ----------
        general = sections.get("general", [])

        if general:
            candidate["name"] = general[0]

        general_text = "\n".join(general)

        # Email
        email = re.search(CandidateExtractor.EMAIL_PATTERN, general_text)
        if email:
            candidate["email"] = email.group()

        # Phone
        phone = re.search(CandidateExtractor.PHONE_PATTERN, general_text)
        if phone:
            candidate["phone"] = phone.group()

        # Location
        location = re.search(r"Location:\s*(.*)", general_text)

        if location:
            candidate["location"] = location.group(1)

        # ---------- Other Sections ----------

        candidate["summary"] = "\n".join(sections.get("summary", []))

        candidate["skills"] = sections.get("skills", [])

        candidate["experience"] = sections.get("experience", [])

        candidate["education"] = sections.get("education", [])

        candidate["projects"] = sections.get("projects", [])

        candidate["certifications"] = sections.get("certifications", [])

        candidate["languages"] = sections.get("languages", [])

        return candidate