with open("output/cv_text.txt", "r", encoding="utf-8") as file:
    cv_text = file.read().lower()


with open("job.txt", "r", encoding="utf-8") as file:
    job_description = file.read()


skills = [
    "electrical",
    "maintenance",
    "plc",
    "automation",
    "autocad",
    "excel",
    "python",
    "power bi",
]

matches = []
missing = []

for skill in skills:
    if skill in job_description.lower():
        if skill in cv_text:
            matches.append(skill)
        else:
            missing.append(skill)

total_required = len(matches) + len(missing)
match_percentage = (len(matches) / total_required) * 100

print("JOB MATCHING RESULTS")
print("--------------------")

print("\nMatching skills:")
for skill in matches:
    print("-", skill)

print("\nMissing skills:")
for skill in missing:
    print("-", skill)

print(f"\nJob Match: {match_percentage:.1f}%")