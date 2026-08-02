from datetime import datetime


def calculate_experience(duration):
    """
    Example:
    January 2022 - March 2024
    """

    start_str, end_str = duration.split(" - ")

    start_date = datetime.strptime(start_str, "%B %Y")
    end_date = datetime.strptime(end_str, "%B %Y")

    months = (end_date.year - start_date.year) * 12
    months += end_date.month - start_date.month

    years = months // 12
    remaining_months = months % 12

    return years, remaining_months