from utils.gemini_client import openai

def parse_jd(jd_text):

    prompt = f"""
    Analyze this Job Description and extract:

    1. Required Skills
    2. Preferred Skills
    3. Experience Required
    4. Education Requirements
    5. Important Technologies

    Job Description:
    {jd_text}
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content