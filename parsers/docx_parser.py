from docx import Document
import io

def extract_docx_text(file):

    doc = Document(io.BytesIO(file.read()))

    text = ""

    for para in doc.paragraphs:
        text += para.text + "\n"

    return text