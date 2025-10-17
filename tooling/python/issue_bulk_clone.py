import os
import requests
import json
import argparse

##
# How to run the script:
#
# > export GITHUB_TOKEN="<your github secret token>"
# > python issue_bulk_clone.py <source repo> <destination repo>
#
# Example:
# > python issue_bulk_clone.py CodeYourFuture/Module-Data-Flows Migracode-Barcelona/Module-Data-Flows
#
# Note: your token must have read access to issues and labels in the source repo, and *write access* for the same in the destination one.
# At the time of writing, a personal fine-grained access token with r/w access on the destination repo over issues, pull requests and discussions sufficed.
#
# Note: if cloning issues to recently created repo, remember to enable the "Issues" feature in the UI (Settings > Features > [] Issues).
# Otherwise the script will get a 410 error when attempting to list issues within the destination repo.

# Modules
# https://github.com/CodeYourFuture/The-Piscine
# https://github.com/CodeYourFuture/Module-Onboarding
# https://github.com/CodeYourFuture/Module-Structuring-and-Testing-Data
# https://github.com/CodeYourFuture/Module-Data-Groups
# https://github.com/CodeYourFuture/Module-Data-Flows
# https://github.com/CodeYourFuture/Project-TV-Show



# Read GitHub token from environment variable
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
if not GITHUB_TOKEN:
    raise ValueError("GitHub token not found in environment variables")

# Helper functions
def get_all_issues(repo):
    """Fetch all issues from the given repository, handling pagination."""
    issues = []
    page = 1
    while True:
        url = f'https://api.github.com/repos/{repo}/issues?page={page}&per_page=100'
        headers = {'Authorization': f'token {GITHUB_TOKEN}'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        if not data:
            break
        issues.extend(data)
        page += 1
    return issues

def get_labels(repo):
    """Fetch all labels from the given repository."""
    labels = {}
    page = 1
    while True:
        url = f'https://api.github.com/repos/{repo}/labels?page={page}&per_page=100'
        headers = {'Authorization': f'token {GITHUB_TOKEN}'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        if not data:
            break
        for label in data:
            labels[label['name']] = label['color']
        page += 1
    return labels

def create_label(repo, label_name, color):
    """Create a label in the target repository."""
    url = f'https://api.github.com/repos/{repo}/labels'
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Content-Type': 'application/json'
    }
    label_data = {'name': label_name, 'color': color}
    response = requests.post(url, headers=headers, data=json.dumps(label_data))
    if response.status_code == 422:  # Label already exists
        print(f"Label '{label_name}' already exists in target repo.")
    else:
        response.raise_for_status()
        print(f"Created label: {label_name}")

def create_issue(repo, title, body, labels):
    """Create an issue in the target repository."""
    url = f'https://api.github.com/repos/{repo}/issues'
    headers = {'Authorization': f'token {GITHUB_TOKEN}'}
    issue_data = {'title': title, 'body': body, 'labels': labels}
    response = requests.post(url, headers=headers, data=json.dumps(issue_data))
    response.raise_for_status()
    return response.json()

def clone_issues(source_repo, target_repo):
    """Clone issues from source_repo to target_repo, copying all labels along with colors."""
    source_labels = get_labels(source_repo)
    target_labels = get_labels(target_repo)

    # Create labels in the target repo if they don't exist
    for label_name, color in source_labels.items():
        if label_name not in target_labels:
            create_label(target_repo, label_name, color)

    issues = get_all_issues(source_repo)
    for issue in issues:
        if "pull_request" not in issue:  # Skip pull requests, only clone issues
            title = issue['title']
            body = issue['body'] or ''
            labels = [label['name'] for label in issue.get('labels', [])]
            print(f'Cloning issue: {title} with labels {labels}')
            created_issue = create_issue(target_repo, title, body, labels)
            print(f'Created: {created_issue["html_url"]}')

def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Script to copy issues from one github repository to another. Repos must be expressed as <owner>/<repo name>.'
    )
    parser.add_argument(
        'source_repo',
        type=str,
        help='The source github repository.'
    )
    parser.add_argument(
        'destination_repo',
        type=str,
        help='The destination github repository.'
    )

    args = parser.parse_args()

    return args.source_repo, args.destination_repo

def main():
    source_repo, destination_repo = parse_arguments()

    print(f"Copying issues from {source_repo} to {destination_repo}...")

    # Run the cloning process
    clone_issues(source_repo, destination_repo)

if __name__ == "__main__":
    main()
