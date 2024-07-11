import subprocess
import requests
import sys


def run_command(command):
    result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
    return result.stdout.strip()


def commit_changes(branch_name):
    run_command(f"git checkout -b {branch_name}")
    run_command("git add .")
    run_command("git commit -m 'Fix SonarQube issues'")
    run_command(f"git push origin {branch_name}")


def create_pull_request(repo, title, body, head, base, token):
    url = f"https://api.github.com/repos/{repo}/pulls"
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    data = {
        'title': title,
        'body': body,
        'head': head,
        'base': base
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        print(f"Pull request created: {response.json().get('html_url')}")
    else:
        print(f"Failed to create pull request: {response.status_code} - {response.text}")


if __name__ == "__main__":
    repo = sys.argv[1]
    title = sys.argv[2]
    body = sys.argv[3]
    head = sys.argv[4]
    base = sys.argv[5]
    token = sys.argv[6]

    commit_changes(head)
    create_pull_request(repo, title, body, head, base, token)
