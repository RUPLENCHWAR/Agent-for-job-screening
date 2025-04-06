import re
import fitz  # PyMuPDF

def extract_text_from_pdf(path):
    doc = fitz.open(path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_name_email(text):
    email_match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    name_match = re.search(r'^[A-Z][a-z]+\s[A-Z][a-z]+', text)
    
    email = email_match.group() if email_match else "N/A"
    name = name_match.group() if name_match else "N/A"
    
    return name, email
