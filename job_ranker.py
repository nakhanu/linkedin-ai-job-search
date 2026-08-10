import json

# Load CV
with open("output/cv_text.txt", "r", encoding="utf-8") as file:
    cv_text = file.read().lower()

# Load jobs
with open("output/jobs_found.json", "r", encoding="utf-8") as file:
    jobs = json.load(file)

# Skills we want to detect
skills = [
    "electrical",
    "maintenance",
    "plc",
    "automation",
    "autocad",
    "excel",
    "python",
    "power bi",
    "scada",
    "hmi",
    "matlab",
    "eplan"
]

ranked_jobs = []

for job in jobs:
    job_text = (
        job.get("title", "") + " " +
        job.get("description", "")
    ).lower()

    matching_skills = []

    for skill in skills:
        if skill in cv_text and skill in job_text:
            matching_skills.append(skill)

    total_required = sum(1 for skill in skills if skill in job_text)

    if total_required > 0:
        match_percentage = (
            len(matching_skills) / total_required
        ) * 100
    else:
        match_percentage = 0

    job["skills"] = matching_skills
    job["match"] = match_percentage

    ranked_jobs.append(job)

# Highest match first
ranked_jobs.sort(
    key=lambda job: job["match"],
    reverse=True
)

# Save ranked jobs
with open(
    "output/ranked_jobs.json",
    "w",
    encoding="utf-8"
) as file:
    json.dump(ranked_jobs, file, indent=4)

print("\n=== REAL JOB RANKING RESULTS ===\n")

for i, job in enumerate(ranked_jobs, start=1):
    print(f"{i}. {job['title']}")
    print(f"   Company: {job['company']}")
    print(f"   Location: {job['location']}")
    print(f"   Match: {job['match']:.1f}%")
    print(
        "   Matching skills: "
        + ", ".join(job["skills"])
    )
    print()

print("Ranked jobs saved successfully!")
print("Saved to: output/ranked_jobs.json")