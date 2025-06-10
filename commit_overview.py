import argparse
import requests
from datetime import datetime


def get_github_commits(token, owner, repo, per_page=5):
    """Return a list of recent commits from a GitHub repository."""
    headers = {"Authorization": f"token {token}"}
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    response = requests.get(url, headers=headers, params={"per_page": per_page})
    response.raise_for_status()
    data = response.json()
    return [
        {
            "sha": item["sha"],
            "date": item["commit"]["author"]["date"],
            "message": item["commit"]["message"],
        }
        for item in data
    ]


def get_gitlab_commits(token, project_id, per_page=5):
    """Return a list of recent commits from a GitLab project."""
    headers = {"PRIVATE-TOKEN": token}
    url = f"https://gitlab.com/api/v4/projects/{project_id}/repository/commits"
    response = requests.get(url, headers=headers, params={"per_page": per_page})
    response.raise_for_status()
    data = response.json()
    return [
        {
            "id": item["id"],
            "date": item["committed_date"],
            "message": item["title"],
        }
        for item in data
    ]


def print_overview(label, commits):
    if not commits:
        print(f"No commits found for {label}.")
        return
    last_commit = commits[0]
    total = len(commits)
    date = datetime.fromisoformat(last_commit["date"].replace("Z", "+00:00"))
    print(f"{label}: {total} commits. Last commit on {date:%Y-%m-%d} - {last_commit['message']}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Summarize recent GitHub and GitLab commits.")
    parser.add_argument("--github-token", help="GitHub personal access token")
    parser.add_argument("--github-owner", help="GitHub repository owner")
    parser.add_argument("--github-repo", help="GitHub repository name")
    parser.add_argument("--gitlab-token", help="GitLab private token")
    parser.add_argument("--gitlab-project", help="GitLab project ID")
    parser.add_argument("--per-page", type=int, default=5, help="Number of commits to retrieve from each repo")
    args = parser.parse_args()

    if args.github_token and args.github_owner and args.github_repo:
        gh_commits = get_github_commits(
            args.github_token, args.github_owner, args.github_repo, args.per_page
        )
        print_overview("GitHub", gh_commits)

    if args.gitlab_token and args.gitlab_project:
        gl_commits = get_gitlab_commits(
            args.gitlab_token, args.gitlab_project, args.per_page
        )
        print_overview("GitLab", gl_commits)
