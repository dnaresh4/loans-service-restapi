import subprocess
import requests
import sys

def run_command(command):
    result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
    return result.stdout.strip()

def check_for_changes():
    result = run_command("git status --porcelain")
    return bool(result.strip())

def commit_changes(branch_name):
    if not check_for_changes():
        print("No changes to commit.")
        return False

    run_command("git config --global user.email 'dnaresh4@gmail.com'")
    run_command("git config --global user.name 'Naresh Darapaneni'")

    run_command(f"git checkout -b {branch_name}")
    run_command("git add .")
    
    try:
        run_command("git commit -m 'Fix SonarQube issues'")
    except subprocess.CalledProcessError as e:
        print(f"Error during commit: {e}")
        print(f"Command output: {e.output}")
        return False

    run_command(f"git push origin {branch_name}")
    return True

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

    if commit_changes(head):
        create_pull_request(repo, title, body, head, base, token)
