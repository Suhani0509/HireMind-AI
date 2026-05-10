# Security Risk Mitigation

## 1. Prompt Injection Risk

### Risk
Malicious users may attempt to manipulate AI reasoning using crafted resume or job description content.

### Mitigation
- Structured rubric-based scoring reduces unrestricted LLM reasoning.
- Prompt templates are controlled using LangChain PromptTemplate.
- Resume parsing is separated from scoring logic.
- Deterministic rule-based explanations reduce hallucination risks.

## 2. Data Privacy / PII

### Risk
Resumes contain personally identifiable information such as emails, phone numbers, LinkedIn URLs, and educational records.

### Mitigation
- Resume processing occurs locally within the application.
- No resume data is permanently stored.
- No external cloud database is used.
- Uploaded files are processed temporarily in memory.

## 3. API Key Exposure

### Risk
API keys may accidentally be leaked through source code or GitHub commits.

### Mitigation
- Environment variables are stored using `.env`.
- `.env` file is excluded from Git tracking.
- Sensitive credentials are never hardcoded into source files.

## 4. Hallucination Risk

### Risk
LLMs may generate inaccurate candidate assessments or misleading recommendations.

### Mitigation
- Rubric scoring is primarily rule-based and deterministic.
- Final scores are calculated mathematically.
- Explainability logic references explicit rubric dimensions.
- Human HR override allows manual correction of AI decisions.

## 5. Unauthorized Access

### Risk
Unauthorized users may access candidate evaluations.

### Mitigation
- The current prototype runs locally for demonstration purposes.
- Production deployment would require authentication and role-based access control.

## 6. Resume File Validation

### Risk
Users may upload unsupported or malicious files.

### Mitigation
- Only PDF and DOCX files are accepted.
- File parsing is isolated using dedicated parser modules.

## 7. Human-in-the-Loop Protection

### Risk
Over-reliance on automated hiring recommendations.

### Mitigation
- HR Override Hook allows recruiters to manually modify recommendations.
- Recruiters can provide override justifications before final decisions.

# Security Design Summary

The HireMind AI system prioritizes:
- explainable AI,
- human oversight,
- deterministic scoring,
- local processing,
- modular architecture,
- secure credential handling.

The system is designed as an assistive hiring tool rather than a fully autonomous decision-maker.