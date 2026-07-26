def calculate_ats_score(skills):

    score = len(skills) * 20

    return min(score, 100)