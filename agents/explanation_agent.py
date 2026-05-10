def generate_explanation(candidate):
    
    explanation = []

    # Skills
    if candidate["Skills Match"] >= 7:

        explanation.append(
            "Strong technical skill alignment with the job description."
        )

    else:

        explanation.append(
            "Limited overlap between candidate skills and required technologies."
        )

    # Experience
    if candidate["Experience Relevance"] >= 7:

        explanation.append(
            "Candidate demonstrates relevant project or industry experience."
        )

    else:

        explanation.append(
            "Candidate lacks strong domain-specific experience."
        )

    # Projects
    if candidate["Project Portfolio"] >= 7:

        explanation.append(
            "Portfolio contains multiple practical and hands-on projects."
        )

    else:

        explanation.append(
            "Project portfolio could be strengthened with more relevant work."
        )

    # Communication
    if candidate["Communication Quality"] >= 7:

        explanation.append(
            "Resume demonstrates clear and structured communication."
        )

    else:

        explanation.append(
            "Resume formatting and communication clarity can improve."
        )

    return explanation