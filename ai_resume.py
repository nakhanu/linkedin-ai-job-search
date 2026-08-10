# CV Customization

with open("output/cv_text.txt", "r", encoding="utf-8") as file:
    cv_text = file.read()

with open("output/ranked_jobs.json", "r", encoding="utf-8") as file:
    import json
    ranked_jobs = json.load(file)

# Select the best job
best_job = ranked_jobs[0]

job_title = best_job["title"]
company = best_job["company"]
matching_skills = best_job["skills"]
match_percentage = best_job["match"]

skills_text = ", ".join(skill.title() for skill in matching_skills)

# Create a tailored professional summary
tailored_summary = f"""
PROFESSIONAL SUMMARY – TAILORED FOR {job_title.upper()}

Electrical and Electronics Engineering graduate with experience relevant to
{skills_text}. Interested in applying technical knowledge in electrical
engineering, maintenance and related engineering environments. A strong
candidate for the {job_title} position at {company}, with a {match_percentage:.1f}%
skill match based on the available job requirements.
"""

# Save tailored CV content
tailored_cv = tailored_summary + "\n\n" + cv_text

with open("output/tailored_cv.txt", "w", encoding="utf-8") as file:
    file.write(tailored_cv)

print("Tailored CV created successfully!")
print(f"\nTarget position: {job_title}")
print(f"Company: {company}")
print(f"Match: {match_percentage:.1f}%")
print(f"Matching skills: {skills_text}")
print("\nSaved to: output/tailored_cv.txt")