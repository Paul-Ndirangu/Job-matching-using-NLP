# Cosine Similarity
#
from fastapi import FastAPI, UploadFile, File, Form
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from typing import Annotated
from docx import Document
import io



app = FastAPI()

@app.post("/upload-docx")
async def upload_docx(
        job_description_file: UploadFile = File(...),
        resume_file: UploadFile = File(...)
        ):
    
    jd_file = await job_description_file.read()
    file_data = await resume_file.read()  # Read the contents of the uploaded file
    
    
    # Process the file data using python-docx to extract text from the DOCX file
    job_doc = Document(io.BytesIO(jd_file))
    job_description = "\n".join([para.text for para in job_doc.paragraphs])
    
    resume_doc = Document(io.BytesIO(file_data))
    resume = "\n".join([para.text for para in resume_doc.paragraphs])
    
    content = [job_description, resume]
    cv = CountVectorizer()
    
    matrix = cv.fit_transform(content)
    
    similarity_matrix = cosine_similarity(matrix)
    
    match = similarity_matrix[1][0]*100
    
    score = []
    if match > 90:
        score.append(f"Candidate is a match: \nscore: {match}")
    elif match < 90 and match > 40:
        score.append(f"Candidate is an average match: \nscore: {match}")
    else:
        score.append(f"Candidate is not a match: \nscore: {match}")

    return {
            "Resume_filename": resume_file.filename, 
            "Job_Description": job_description_file.filename,
            "Resume_Matches_by": score
            }
