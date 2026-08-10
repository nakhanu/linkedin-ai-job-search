import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.getenv("ADZUNA_APP_ID")
APP_KEY = os.getenv("ADZUNA_APP_KEY")

# Search settings
COUNTRY = "gb"
QUERY = "electrical engineer"
LOCATION = "London"

url = f"https://api.adzuna.com/v1/api/jobs/{COUNTRY}/search/1"

params = {
    "app_id": APP_ID,
    "app_key": APP_KEY,
    "results_per_page": 10,
    "what": QUERY,
    "where": LOCATION,
    "content-type": "application/json"
}

print("=== SEARCHING REAL JOB LISTINGS ===")
print(f"Search: {QUERY}")
print(f"Location: {LOCATION}\n")

response = requests.get(url, params=params, timeout=30)

if response.status_code != 200:
    print("Job search failed.")
    print("Status code:", response.status_code)
    print(response.text)
    raise SystemExit

data = response.json()

jobs = []

for job in data.get("results", []):
    jobs.append({
        "title": job.get("title", "Unknown"),
        "company": job.get("company", {}).get("display_name", "Unknown"),
        "location": job.get("location", {}).get("display_name", "Unknown"),
        "description": job.get("description", ""),
        "url": job.get("redirect_url", ""),
        "skills": []
    })

# Save results
os.makedirs("output", exist_ok=True)

with open("output/jobs_found.json", "w", encoding="utf-8") as file:
    json.dump(jobs, file, indent=4)

print(f"Found {len(jobs)} jobs.\n")

for i, job in enumerate(jobs, start=1):
    print(f"{i}. {job['title']}")
    print(f"   Company: {job['company']}")
    print(f"   Location: {job['location']}")
    print(f"   URL: {job['url']}\n")

print("Jobs saved successfully!")
print("Saved to: output/jobs_found.json")