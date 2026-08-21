"""
Day 25 - Availability Integration

Purpose:
Integrate extracted candidate availability
into the candidate screening data.
"""


def integrate_availability(candidate_data: dict, availability):
    """
    Integrate extracted availability into candidate data.

    Args:
        candidate_data: Existing candidate information.
        availability: Extracted availability category.

    Returns:
        Updated candidate data.
    """

    if candidate_data is None:
        candidate_data = {}

    if availability is not None:
        candidate_data["availability"] = availability

    return candidate_data