# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance
# with the License. You may obtain a copy of
# the License at @copyright@apache.org/licenses/L
# @copyright
# Strathmore University
#
# pip install pdfminer 
# pip install docx2txt

from pdfminer.high_level import extract_text 
import docx2txt 

# Extracting text from PDF files
def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)
 
# Extracting text from docx files
def extract_text_from_docx(docx_path):
    txt = docx2txt.process(docx_path)
    if txt:
        return txt.replace('\t', ' ')
    return None
 
 
if __name__ == '__main__':
    print(extract_text_from_pdf('./files/London-Resume-Template-Professional.pdf'))  # noqa: T001
    # print(extract_text_from_docx('./files/Text-Resume-Bootcamp-Instructor.docx'))  # noqa: T001
    
    