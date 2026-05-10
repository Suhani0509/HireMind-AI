from langchain.prompts import PromptTemplate

template = """
You are an expert HR recruiter.

A candidate was evaluated for a job role.

Candidate Name:
{candidate}

Match Score:
{score}

Your task:
Write 3 professional bullet points explaining:

1. Why the candidate may fit the role
2. Missing skills or weaknesses
3. Final hiring recommendation

Keep the response concise and professional.
"""

prompt_template = PromptTemplate(
    input_variables=[
        "candidate",
        "score"
    ],
    template=template
)

def build_prompt(candidate, score):

    return prompt_template.format(
        candidate=candidate,
        score=score
    )