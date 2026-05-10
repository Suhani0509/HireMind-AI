import streamlit as st
import pandas as pd

from agents.resume_agent import parse_resume
from embeddings.semantic_matcher import get_similarity
from agents.scoring_agent import calculate_dimension_scores
from agents.explanation_agent import generate_explanation

st.set_page_config(
    page_title="HireMind AI",
    layout="wide"
)

st.title("HireMind AI")

st.subheader(
    "Explainable Multi-Agent Hiring Copilot"
)

# Upload JD
jd_file = st.file_uploader(
    "Upload Job Description (.txt)"
)

# Upload Resumes
resume_files = st.file_uploader(
    "Upload Resume PDFs/DOCX",
    accept_multiple_files=True
)

if jd_file:

    st.success(
        "Job Description Uploaded Successfully"
    )

    jd_text = jd_file.read().decode("utf-8")

    st.subheader(
        "Job Description Content"
    )

    st.text_area(
        "JD Text",
        jd_text,
        height=200
    )

    if resume_files:

        st.success(
            f"{len(resume_files)} Resume(s) Uploaded"
        )

        # ---------------------------------
        # STORE ALL CANDIDATE RESULTS
        # ---------------------------------

        candidate_results = []

        for resume in resume_files:

            # Parse Resume
            resume_text = parse_resume(resume)

            # Semantic Similarity
            similarity = get_similarity(
                jd_text,
                resume_text
            )

            # Rubric Scores
            scores = calculate_dimension_scores(
                jd_text,
                resume_text,
                similarity
            )

            final_score = scores["Final Score"]

            recommendation = scores[
                "Recommendation"
            ]

            # Save Result
            candidate_results.append({

                "Candidate": resume.name,

                "Final Score": final_score,

                "Recommendation": recommendation,

                "Skills Match":
                    scores["Skills Match"],

                "Experience Relevance":
                    scores["Experience Relevance"],

                "Education & Certs":
                    scores["Education & Certs"],

                "Project Portfolio":
                    scores["Project Portfolio"],

                "Communication Quality":
                    scores["Communication Quality"],

                "Resume Text": resume_text
            })

        # ---------------------------------
        # SORT CANDIDATES
        # ---------------------------------

        candidate_results = sorted(
            candidate_results,
            key=lambda x: x["Final Score"],
            reverse=True
        )

        # ---------------------------------
        # RANKING DASHBOARD
        # ---------------------------------

        st.header(
            "🏆 Candidate Ranking Dashboard"
        )

        ranking_df = pd.DataFrame([
            {
                "Rank": idx + 1,
                "Candidate": c["Candidate"],
                "Final Score": c["Final Score"],
                "Recommendation": c["Recommendation"]
            }

            for idx, c in enumerate(candidate_results)
        ])

        st.dataframe(
            ranking_df,
            use_container_width=True
        )
        
        # ---------------------------------
# DOWNLOAD CSV REPORT
# ---------------------------------

        csv = ranking_df.to_csv(
            index=False
        )

        st.download_button(

            label="📥 Download Shortlist Report",

            data=csv,

            file_name="hiremind_shortlist_report.csv",

            mime="text/csv"
        )

        # ---------------------------------
        # DETAILED ANALYSIS
        # ---------------------------------

        st.header(
            "📊 Detailed Candidate Analysis"
        )

        for candidate in candidate_results:

            st.divider()

            st.header(
                f"Candidate: {candidate['Candidate']}"
            )

            # Final Score
            st.metric(
                "Final Match Score",
                f"{candidate['Final Score']}%"
            )

            st.progress(
                candidate["Final Score"] / 100
            )

            # Recommendation
            st.success(
                f"Recommendation: {candidate['Recommendation']}"
            )

            # Rubric Table
            st.subheader(
                "Rubric Evaluation"
            )

            st.table({

                "Dimension": [

                    "Skills Match",

                    "Experience Relevance",

                    "Education & Certs",

                    "Project Portfolio",

                    "Communication Quality"
                ],

                "Score (/10)": [

                    candidate["Skills Match"],

                    candidate["Experience Relevance"],

                    candidate["Education & Certs"],

                    candidate["Project Portfolio"],

                    candidate["Communication Quality"]
                ]
            })

            # ---------------------------------
            # AI EXPLANATION
            # ---------------------------------

            explanation = generate_explanation(
                candidate
            )

            st.subheader(
                "AI Explanation"
            )

            for point in explanation:

                st.write("•", point)

            # ---------------------------------
            # HR OVERRIDE HOOK
            # ---------------------------------

            st.subheader(
                "HR Override Decision"
            )

            override_decision = st.selectbox(

                f"Override Recommendation for {candidate['Candidate']}",

                [
                    "Strong Hire",
                    "Hire",
                    "Consider",
                    "Reject"
                ],

                index=[
                    "Strong Hire",
                    "Hire",
                    "Consider",
                    "Reject"
                ].index(candidate["Recommendation"])
            )

            override_reason = st.text_area(

                f"Reason for Override ({candidate['Candidate']})",

                placeholder="Enter HR comments or justification..."
            )

            st.info(
                f"Final HR Decision: {override_decision}"
            )

            if override_reason:

                st.write(
                    "HR Notes:",
                    override_reason
                )

            # ---------------------------------
            # RESUME TEXT
            # ---------------------------------

            with st.expander(
                "View Extracted Resume Text"
            ):

                st.text_area(
                    "Resume Text",
                    candidate["Resume Text"][:4000],
                    height=300
                )

else:

    st.info(
        "Please upload a Job Description first."
    )