# Job-matching-using-NLP

This project focuses on job matching by analyzing the similarity between a user's resume/CV and a job description using Natural Language Processing (NLP) techniques. The project utilizes cosine similarity to calculate the matching score, providing a quantitative measure of how well a candidate's skills and experience align with the requirements of a particular job.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)

## Overview

Job matching is a crucial aspect of the recruitment process, as it helps both job seekers and employers find suitable matches quickly and efficiently. By leveraging NLP and cosine similarity, this project aims to automate and streamline the job matching process by providing a quantitative assessment of the match between a candidate's resume/CV and a job description.

The project consists of two main components:

1. Resume/CV Parsing: The user uploads their resume/CV document, which is then processed using NLP techniques to extract relevant information such as skills, experience, and education.

2. Matching Score Calculation: The extracted information from the user's resume/CV is compared to the job description using cosine similarity. This similarity score is a numerical representation of the alignment between the candidate's profile and the job requirements.

## Features

- **Resume/CV Parsing:** The system extracts important information from the user's resume/CV, such as skills, experience, and education, to create a structured representation for matching analysis.

- **Job Description Analysis:** The project includes a pre-processing step to extract the key requirements from a job description, ensuring accurate matching against the candidate's profile.

- **Cosine Similarity Calculation:** The cosine similarity metric is used to measure the similarity between the user's resume/CV and the job description. The resulting score provides an objective measure of how well the candidate's profile aligns with the job requirements.

- **Scoring and Ranking:** The matching score is calculated for each candidate, and the candidates are ranked based on their scores, allowing employers to quickly identify the most suitable candidates for a given job.

## Getting Started

To get started with this project, follow the steps below:

1. Clone the repository:

```shell
git clone https://github.com/Paul-Ndirangu/Job-matching-using-NLP/
```

2. Create Virtual Environment
```shell
pip install virtualenv
```

3. Create env
```shell
virtualvenv venv
```

4. Activate env
```shell
source ./venv/bin/activate
```

5. You can install the required packages by running the following command:<br/>
```shell
pip install -r requirements.txt
```

> Alternative of Install Requirements<br/>
```shell
pip install fastapi uvicorn
```

```shell
pip install sklearn typing
```

```shell
pip install docx pdfminer
```

6. Run App<br/>
uvicorn main:app --reload`

7. Access the application via a web browser at
   
  [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
  
  [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) 
   
## Usage

1. Upload a resume/CV document: On the web interface, select the resume/CV document file and click the "Upload" button.

2. Specify the job description: Enter or paste the job description into the provided text field.

3. Get the matching score: Once the upload and job description submission are complete, the system will calculate the matching score using cosine similarity.

4. Review the results: The application will display the matching score and provide a ranked list of candidates based on their scores, allowing employers to assess the best-fit candidates quickly.

## Requirements

The project requires the following dependencies:

- Python 3.x
- FastAPI
- Uvicorn
- NLTK (Natural Language Toolkit)
- Scikit-learn
- Flask (for web interface)


## Contributing

Contributions to this project are welcome! If you have any suggestions, improvements, or bug fixes, please follow these steps:

1. Fork the repository.

2. Create a new branch: `git checkout -b feature/your-feature`.

3. Make the necessary changes and commit them: `git commit -m 'Add some feature'`.

4. Push to the branch: `git push origin feature/your-feature`.

5. Open a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

Make sure to replace `your-username/your-repo` with your actual GitHub username and repository name.

Feel free to modify the content to suit your specific project needs.
