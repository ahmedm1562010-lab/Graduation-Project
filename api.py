import pandas as pd
import requests

GITHUB_TOKEN = "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" 
headers = {"Authorization": f"token {GITHUB_TOKEN}"}

TARGET_YEAR = "2026"

url = "https://api.github.com/search/repositories"
params = {
    "q": f"topic:machine-learning created:{TARGET_YEAR}-01-01..{TARGET_YEAR}-12-31",
    "sort": "stars",
    "order": "desc",
    "per_page": 100,
}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    data = response.json()["items"]

    repo_list = []
    for repo in data:
        repo_list.append(
            {
                "id": repo["id"],
                "name": repo["name"],
                "full_name": repo["full_name"],
                "owner": repo["owner"]["login"],
                "stars": repo["stargazers_count"],
                "forks": repo["forks_count"],
                "open_issues": repo["open_issues_count"],
                "language": (
                    repo["language"] if repo["language"] else "Unknown"
                ),
                "created_at": repo["created_at"],
                "updated_at": repo["updated_at"],
            }
        )

    df = pd.DataFrame(repo_list)
    df["created_at"] = pd.to_datetime(df["created_at"])
    df["updated_at"] = pd.to_datetime(df["updated_at"])

    df.to_csv("ml_repositories_cleaned.csv", index=False)
    print("Data fetched and saved successfully! Count:", len(df))

else:
    print(f"Failed to fetch data. Status code: {response.status_code}")