Absolutely. Add a file named README.md in your project folder and paste this:

# LinkedIn AI Job Search

A prototype of an AI-powered job search and application preparation system.

## Project Overview

This project helps job seekers find relevant job opportunities based on their CV and skills. It retrieves job listings, matches and ranks jobs according to the candidate's skills, and prepares application materials.

## Features

- CV text extraction
- Job search using the Adzuna API
- CV-to-job skill matching
- Job ranking based on skill matches
- Tailored CV generation
- Application email generation
- Application package preparation

## Technologies Used

- Python
- Pandas
- Requests
- BeautifulSoup
- PyPDF
- Selenium
- Adzuna API
- JSON
- Python-dotenv

## Project Workflow

```text
CV
 ↓
CV Text Extraction
 ↓
Job Search
 ↓
Skill Matching
 ↓
Job Ranking
 ↓
Tailored CV
 ↓
Application Email
 ↓
Application Package
Project Structure
linkedin-ai-job-search/
│
├── ai_resume.py
├── email_generator.py
├── job_matcher.py
├── job_ranker.py
├── job_search.py
├── prepare_application.py
├── run_project.py
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── job.txt
Setup

Clone the repository:

git clone https://github.com/nakhanu/linkedin-ai-job-search.git
cd linkedin-ai-job-search

Create a virtual environment:

python -m venv venv

Activate it on Windows:

venv\Scripts\Activate.ps1

Install the required packages:

pip install -r requirements.txt
API Configuration

Create a .env file in the project directory and add your Adzuna API credentials:

ADZUNA_APP_ID=your_app_id
ADZUNA_APP_KEY=your_app_key

Do not upload your .env file or API keys to GitHub.

Running the Project

Run the complete workflow with:

python run_project.py

The system generates:

cv_text.txt
jobs_found.json
ranked_jobs.json
tailored_cv.txt
application_email.txt
application_package
Project Status

Prototype completed successfully.

This project demonstrates the core workflow of an automated job-search and application preparation system. Future improvements could include integration with generative AI, more advanced job matching, a web interface, and automated application tracking.

Author

Sophia Nakhanu

GitHub: https://github.com/nakhanu
