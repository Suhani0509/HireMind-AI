import re

def calculate_dimension_scores(
    jd_text,
    resume_text,
    similarity
):

    resume_lower = resume_text.lower()
    jd_lower = jd_text.lower()

    # -----------------------------
    # Skills Match
    # -----------------------------

    tech_keywords = [
        "python",
        "java",
        "react",
        "node",
        "mongodb",
        "docker",
        "aws",
        "machine learning",
        "sql",
        "flask",
        "django",
        "javascript",
        "c++",
        "tensorflow",
        "pytorch",
        "devops",
        "kubernetes"
    ]

    matched_skills = 0

    for skill in tech_keywords:

        if skill in jd_lower and skill in resume_lower:
            matched_skills += 1

    skills_score = min(matched_skills, 10)

    # -----------------------------
    # Experience Relevance
    # -----------------------------

    experience_keywords = [
        "intern",
        "experience",
        "developer",
        "engineer",
        "project",
        "research"
    ]

    exp_matches = 0

    for word in experience_keywords:

        if word in resume_lower:
            exp_matches += 1

    experience_score = min(exp_matches + 3, 10)

    # -----------------------------
    # Education Score
    # -----------------------------

    education_keywords = [
        "btech",
        "bachelor",
        "computer science",
        "cgpa",
        "certification"
    ]

    edu_matches = 0

    for word in education_keywords:

        if word in resume_lower:
            edu_matches += 1

    education_score = min(edu_matches + 4, 10)

    # -----------------------------
    # Project Portfolio
    # -----------------------------

    project_keywords = [
        "project",
        "developed",
        "built",
        "github",
        "application",
        "ai",
        "ml",
        "web"
    ]

    proj_matches = 0

    for word in project_keywords:

        if word in resume_lower:
            proj_matches += 1

    project_score = min(proj_matches, 10)

    # -----------------------------
    # Communication Quality
    # -----------------------------

    words = resume_text.split()

    sentences = re.split(r'[.!?]', resume_text)

    avg_sentence_length = len(words) / max(len(sentences), 1)

    if avg_sentence_length > 12:
        communication_score = 8
    else:
        communication_score = 6

    # -----------------------------
    # Weighted Final Score
    # -----------------------------

    final_score = (
        skills_score * 0.30 +
        experience_score * 0.25 +
        education_score * 0.15 +
        project_score * 0.20 +
        communication_score * 0.10
    ) * 10

    final_score = round(final_score)

    # -----------------------------
    # Recommendation
    # -----------------------------

    if final_score >= 80:
        recommendation = "Strong Hire"

    elif final_score >= 60:
        recommendation = "Hire"

    elif final_score >= 40:
        recommendation = "Consider"

    else:
        recommendation = "Reject"

    return {
        "Skills Match": skills_score,
        "Experience Relevance": experience_score,
        "Education & Certs": education_score,
        "Project Portfolio": project_score,
        "Communication Quality": communication_score,
        "Final Score": final_score,
        "Recommendation": recommendation
    }