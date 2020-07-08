import requests
import json
import pandas as pd


repos = requests.get(
    "https://api.github.com/repos/awesome-jobs/vietnam/issues?per_page=200"
)
repos.json()
issues = json.loads(repos.content)
jobs = []
links = []
for issue in issues:
    jobs.append(issue["title"])
    links.append(issue["url"])
github_jobs = pd.DataFrame(zip(jobs, links), columns=["jobs on github", "links"])
github_jobs.to_csv("github_job.csv")
