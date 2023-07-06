# Extracting skills from the resumes
# pip install docx2txt
# pip install nltk
#

import docx2txt
import nltk
 
nltk.download('stopwords')
 
# you may read the database from a csv file or some other database
SKILLS_DB = [
    'data science',
    'machine learning',
    'Los Angeles',
    'Cardio Training',
    'python',
    'word',
    'excel',
    'English',
]
 
 
def extract_text_from_docx(docx_path):
    txt = docx2txt.process(docx_path)
    if txt:
        return txt.replace('\t', ' ')
    return None
 
 
def extract_skills(input_text):
    stop_words = set(nltk.corpus.stopwords.words('english'))
    word_tokens = nltk.tokenize.word_tokenize(input_text)
 
    # remove the stop words
    filtered_tokens = [w for w in word_tokens if w not in stop_words]
 
    # remove the punctuation
    filtered_tokens = [w for w in word_tokens if w.isalpha()]
 
    # generate bigrams and trigrams (such as artificial intelligence)
    bigrams_trigrams = list(map(' '.join, nltk.everygrams(filtered_tokens, 2, 3)))
 
    # we create a set to keep the results in.
    found_skills = set()
 
    # we search for each token in our skills database
    for token in filtered_tokens:
        if token.lower() in SKILLS_DB:
            found_skills.add(token)
 
    # we search for each bigram and trigram in our skills database
    for ngram in bigrams_trigrams:
        if ngram.lower() in SKILLS_DB:
            found_skills.add(ngram)
 
    return found_skills
 
 
if __name__ == '__main__':
    text = extract_text_from_docx('./files/Text-Resume-Bootcamp-Instructor.docx')
    skills = extract_skills(text)
 
    print(skills) 
