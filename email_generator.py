import json

# Load CV
with open("output/cv_text.txt", "r", encoding="utf-8") as file:
    cv_text = file.read().lower()

# Load ranked jobs
with open("output/ranked_jobs.json", "r", encoding="utf-8") as file:
    ranked_jobs = json.load(file)

# Select the highest-ranked job
best_job = ranked_jobs[0]

job_title = best_job["title"]
company = best_job["company"]
location = best_job["location"]
matching_skills = best_job["skills"]
match_percentage = best_job["match"]

skills_text = ", ".join(matching_skills)

# Generate application email
email = f"""Subject: Application for {job_title}

Dear Hiring Manager,

I am writing to express my interest in the {job_title} position at {company}.

My background in electrical engineering, together with my experience in
{skills_text}, aligns well with the requirements of this position.

I am eager to contribute my technical skills to your organization and
continue developing my professional experience.

Please find my CV attached for your consideration. I would appreciate the
opportunity to discuss my application further.

Kind regards,
Sophia Nakhanu
"""

# Save email
with open("output/application_email.txt", "w", encoding="utf-8") as file:
    file.write(email)

print("\n=== BEST JOB ===")
print(f"Position: {job_title}")
print(f"Company: {company}")
print(f"Location: {location}")
print(f"Match: {match_percentage:.1f}%")

print("\n=== APPLICATION EMAIL ===")
print(email)

print("Application email saved successfully!")