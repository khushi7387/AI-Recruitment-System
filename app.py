import streamlit as st
import re
import nltk
from nltk.corpus import stopwords
from PyPDF2 import PdfReader
import docx
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# -------------------------------
# Load stopwords
# -------------------------------
@st.cache_resource
def load_stopwords():
    try:
        return set(stopwords.words('english'))
    except:
        nltk.download('stopwords')
        return set(stopwords.words('english'))

stop_words = load_stopwords()

# -------------------------------
# Clean text
# -------------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'[^a-z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    words = text.split()
    words = [w for w in words if w not in stop_words]
    return " ".join(words)

# -------------------------------
# Extract text
# -------------------------------
def extract_text(file):
    if file.type == "application/pdf":
        pdf = PdfReader(file)
        return " ".join([page.extract_text() or "" for page in pdf.pages])
    elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = docx.Document(file)
        return " ".join([p.text for p in doc.paragraphs])
    elif file.type == "text/plain":
        return file.read().decode("utf-8")
    return ""

# -------------------------------
# Skill extraction
# -------------------------------
def extract_skills(text):
    skills = ["python", "machine learning", "data analysis", "sql",
              "java", "deep learning", "nlp", "communication",
              "excel", "tableau", "power bi", "statistics"]
    return [s for s in skills if s in text]

# -------------------------------
# UI
# -------------------------------
st.title("🤖 AI Recruitment System")
st.write("Upload resumes and match them with job description")

job_desc = st.text_area("📌 Enter Job Description")

uploaded_files = st.file_uploader(
    "📄 Upload Resumes",
    type=["pdf", "docx", "txt"],
    accept_multiple_files=True
)

# -------------------------------
# Processing
# -------------------------------
if uploaded_files and job_desc:

    job_clean = clean_text(job_desc)

    texts = [job_clean]
    resume_texts = []
    names = []

    # Extract resume text
    for file in uploaded_files:
        text = extract_text(file)
        clean = clean_text(text)
        resume_texts.append(clean)
        names.append(file.name)
        texts.append(clean)

    # TF-IDF
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(texts)

    job_vector = vectors[0]
    resume_vectors = vectors[1:]

    results = []

    # MAIN LOOP (CORRECTLY INDENTED)
    for i in range(resume_vectors.shape[0]):

        similarity = cosine_similarity(resume_vectors[i], job_vector)[0][0]

        resume_skills = extract_skills(resume_texts[i])
        job_skills = extract_skills(job_clean)

        # Skill match
        if len(job_skills) > 0:
            skill_match = len(set(resume_skills) & set(job_skills)) / len(job_skills)
        else:
            skill_match = 0

        # Final score
        final_score = (0.7 * similarity) + (0.3 * skill_match)

        missing_skills = list(set(job_skills) - set(resume_skills))

        results.append({
            "Candidate": names[i],
            "Match %": round(final_score * 100, 2),
            "Skills Found": ", ".join(resume_skills),
            "Missing Skills": ", ".join(missing_skills)
        })

    # DataFrame
    df = pd.DataFrame(results)

    # Ranking
    df = df.sort_values(by="Match %", ascending=False)
    df["Rank"] = range(1, len(df) + 1)

    # Display
    st.subheader("📊 All Candidates")
    st.dataframe(df)

    st.subheader("🏆 Top 5 Candidates")
    st.dataframe(df.head(5))