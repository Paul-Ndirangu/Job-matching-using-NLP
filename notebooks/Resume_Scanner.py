import sys
import pandas as pd
import PyPDF2
import sklearn
import docx2txt
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from PyPDF2 import PdfFileReader
from io import BytesIO


# Getting Text from Pdf
def extract_text_from_pdf(pdf_file: str) -> [str]:
    with open(pdf_file, 'rb') as pdf:
        reader = PyPDF2.PdfReader(pdf, strict=False)
        pdf_text = []

        for page in reader.pages:
            content = page.extract_text()
            pdf_text.append(content)

        return pdf_text


if __name__ == '__main__':
    resume_extract = extract_text_from_pdf('ADAM_JONES.pdf')
    # for text in resume_extract:
    #     split_message = re.split(r'\s+|[,;?!.-]\s*', text.lower())
    print(resume_extract)


# Getting Text from Docx
job_description = docx2txt.process('sampledesc.docx')
# print(job_description)



#
#
# cv = TfidfVectorizer()
# job_vectorized = cv.fit_transform([job_description])
# resume_vectorized = cv.fit_transform([resume_extract])
