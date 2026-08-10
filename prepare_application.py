import json
import os
import shutil

# Load the best-ranked job
with open("output/ranked_jobs.json", "r", encoding="utf-8") as file:
    ranked_jobs = json.load(file)

best_job = ranked_jobs[0]

# Create application package folder
package_folder = "output/application_package"
os.makedirs(package_folder, exist_ok=True)

# Copy tailored CV
shutil.copy(
    "output/tailored_cv.txt",
    f"{package_folder}/tailored_cv.txt"
)

# Copy application email
shutil.copy(
    "output/application_email.txt",
    f"{package_folder}/application_email.txt"
)

# Create job information file
with open(
    f"{package_folder}/job_information.txt",
    "w",
    encoding="utf-8"
) as file:
    file.write(f"Job Title: {best_job['title']}\n")
    file.write(f"Company: {best_job['company']}\n")
    file.write(f"Location: {best_job['location']}\n")
    file.write(f"Match: {best_job['match']:.1f}%\n")
    file.write(
        "Matching Skills: "
        + ", ".join(best_job["skills"])
        + "\n"
    )

print("=== APPLICATION PACKAGE ===")
print(f"Job: {best_job['title']}")
print(f"Company: {best_job['company']}")
print(f"Match: {best_job['match']:.1f}%")

print("\nApplication package created successfully!")
print(f"Location: {package_folder}")