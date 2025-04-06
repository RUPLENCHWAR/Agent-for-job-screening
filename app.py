from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
from utils import extract_text_from_pdf, extract_name_email
from agents import analyze_resume

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    resume_text = ""
    job_description = request.form.get("job_description", "")
    
    if 'resume' not in request.files or not job_description:
        return "Missing resume or job description", 400

    resume_file = request.files['resume']
    
    if resume_file.filename.endswith('.pdf'):
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(resume_file.filename))
        resume_file.save(filepath)
        resume_text = extract_text_from_pdf(filepath)
    else:
        resume_text = resume_file.read().decode("utf-8")

    name, email = extract_name_email(resume_text)
    score, explanation = analyze_resume(resume_text, job_description)

    return render_template("result.html", name=name, email=email, score=score, explanation=explanation)

if __name__ == '__main__':
    app.run(debug=True)
