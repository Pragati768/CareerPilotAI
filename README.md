\# CareerPilot AI – AI-Powered Career Preparation Copilot



CareerPilot AI is a web-based career preparation tool that helps students and job seekers compare their resumes with job descriptions. It identifies matching skills, missing skills, and additional skills, then provides learning recommendations, project suggestions, and interview practice questions.



\## Problem Statement



Students often find it difficult to identify which technical skills are missing from their resumes when applying for specific job roles. CareerPilot AI addresses this problem by comparing resume skills with the technical requirements mentioned in a job description.



\## Features



\- \*\*Resume Upload:\*\* Upload a text-based PDF resume.

\- \*\*Resume Text Extraction:\*\* Extract readable text from PDF files.

\- \*\*Skill Extraction:\*\* Identify recognized technical skills from resumes and job descriptions.

\- \*\*Skill Matching:\*\* Categorize skills into matching, missing, and additional skills.

\- \*\*Match Percentage:\*\* Calculate a transparent percentage based on matching required skills.

\- \*\*Learning Recommendations:\*\* Suggest learning topics for missing skills.

\- \*\*Project Suggestions:\*\* Provide project ideas related to missing skills.

\- \*\*Interview Preparation:\*\* Generate relevant interview practice questions.

\- \*\*Interactive Dashboard:\*\* Display analysis results through a web interface.



\## Technology Stack



| Technology | Purpose |

|---|---|

| Python | Core application logic |

| Flask | Web application framework |

| HTML | Frontend structure |

| CSS | User interface styling |

| pypdf | PDF text extraction |

| pytest | Automated testing |



\## Project Structure



```text

CareerPilot.ai/

│

├── app/

│   ├── \_\_init\_\_.py

│   ├── main.py

│   ├── resume\_parser.py

│   ├── skill\_extractor.py

│   ├── job\_analyzer.py

│   ├── matcher.py

│   └── recommendations.py

│

├── templates/

│   └── index.html

│

├── static/

│   └── style.css

│

├── tests/

│   ├── \_\_init\_\_.py

│   ├── test\_resume\_parser.py

│   ├── test\_skill\_extractor.py

│   ├── test\_job\_analyzer.py

│   ├── test\_matcher.py

│   └── test\_recommendations.py

│

├── sample\_data/

├── requirements.txt

├── README.md

└── .gitignore

```



\## Installation and Setup



\### 1. Clone the repository



```bash

git clone YOUR\_GITHUB\_REPOSITORY\_URL

cd CareerPilot.ai

```



\### 2. Create a virtual environment



```bash

python -m venv venv

```



\### 3. Activate the virtual environment



\*\*Windows PowerShell:\*\*



```powershell

.\\venv\\Scripts\\Activate.ps1

```



\### 4. Install dependencies



```bash

pip install -r requirements.txt

```



\### 5. Run the application



```bash

python -m app.main

```



Open the following address in your browser:



```text

http://127.0.0.1:5000

```



\## Running Tests



Run the automated test suite:



```bash

python -m pytest -v

```



The current test suite contains 18 tests covering resume parsing, skill extraction, job description analysis, skill matching, and recommendations.



\## How Skill Matching Works



1\. Extract readable text from the uploaded resume.

2\. Identify technical skills using a predefined skill list and regular expressions.

3\. Extract recognized technical skills from the job description.

4\. Compare both skill sets.

5\. Identify matching, missing, and additional skills.

6\. Calculate the match percentage.



\*\*Match percentage formula:\*\*



Matching required skills / Total recognized required skills × 100



This percentage represents keyword overlap only. It does not predict interview selection, hiring probability, or actual job suitability.



\## Current Limitations



\- Skill extraction is based on predefined keywords and regular expressions.

\- Scanned PDFs and image-based resumes are not supported because OCR is not implemented.

\- The application recognizes only skills included in its predefined skill list.

\- Recommendations are based on predefined guidance and generic fallback content.

\- The match percentage does not represent an employer's ATS score.



\## Future Enhancements



\- Add semantic skill extraction using NLP.

\- Integrate an LLM for more contextual career recommendations.

\- Implement Retrieval-Augmented Generation (RAG) for personalized interview preparation.

\- Add OCR support for scanned resumes.

\- Introduce user accounts and saved analysis history.

\- Deploy the application to a cloud platform.



\## Testing Status



The current automated test suite has \*\*18 passing tests\*\*.



\## Author



Developed as a final-year engineering project focused on resume analysis and career preparation.

