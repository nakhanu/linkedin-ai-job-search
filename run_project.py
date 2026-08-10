import subprocess
import os
import sys

print("=" * 60)
print("       LINKEDIN AI JOB SEARCH SYSTEM")
print("=" * 60)

steps = [
    ("Searching for jobs", "job_search.py"),
    ("Ranking jobs", "job_ranker.py"),
    ("Creating tailored CV", "ai_resume.py"),
    ("Generating application email", "email_generator.py"),
    ("Preparing application package", "prepare_application.py")
]

for description, script in steps:
    print(f"\n>>> {description}...")
    subprocess.run([sys.executable, script], check=True)

print("\n" + "=" * 60)
print("       PROJECT COMPLETED SUCCESSFULLY")
print("=" * 60)

print("\nGenerated files:")

files = [
    "output/cv_text.txt",
    "output/jobs_found.json",
    "output/ranked_jobs.json",
    "output/tailored_cv.txt",
    "output/application_email.txt",
    "output/application_package"
]

for file in files:
    if os.path.exists(file):
        print(f"✓ {file}")
    else:
        print(f"✗ Missing: {file}")

print("\nYour application package is ready for review.")