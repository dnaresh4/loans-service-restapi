import os
import requests

def get_sonar_issues(sonar_host, project_key, sonar_token):
    url = f"{sonar_host}/api/issues/search?projectKeys={project_key}"
    headers = {
        'Authorization': f'Bearer {sonar_token}'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an HTTPError if the HTTP request returned an unsuccessful status code
    issues = response.json().get('issues', [])
    return issues

def fix_code(file_path, issue):
    # Debugging statement
    print(f"Attempting to open file: {file_path}")

    # Adjust the file path if necessary
    adjusted_file_path = os.path.join('src/main/java', file_path.replace(':', '/'))

    print(f"Adjusted file path: {adjusted_file_path}")

    if not os.path.exists(adjusted_file_path):
        print(f"File not found: {adjusted_file_path}")
        return

    with open(adjusted_file_path, 'r') as file:
        # Read and fix code here
        pass

def apply_fixes(issues):
    for issue in issues:
        component = issue.get('component')
        text_range = issue.get('textRange')
        file_path = component.replace('.', '/') + ".java"
        fix_code(file_path, issue)

# Usage
sonar_host = 'https://sonarcloud.io'
project_key = 'loans-service-restapi'
sonar_token = '273b52a0e0986e3d298f64e0768d31d01a0de09c'

try:
    issues = get_sonar_issues(sonar_host, project_key, sonar_token)
    apply_fixes(issues)
except Exception as e:
    print(f"Error: {e}")