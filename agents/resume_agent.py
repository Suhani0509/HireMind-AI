from parsers.pdf_parser import extract_pdf_text
from parsers.docx_parser import extract_docx_text

def parse_resume(file):

    if file.name.endswith(".pdf"):
        return extract_pdf_text(file)

    elif file.name.endswith(".docx"):
        return extract_docx_text(file)

    return ""