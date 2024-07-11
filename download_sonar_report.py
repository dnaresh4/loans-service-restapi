import requests
import json

def get_sonar_issues(sonar_host, project_key, sonar_token):
    url = f"{sonar_host}/api/issues/search?projectKeys={project_key}"
    headers = {
        'Authorization': f'Bearer {sonar_token}'
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        raise Exception(f"Failed to fetch issues: {response.status_code} - {response.text}")
    
    return response.json().get('issues', [])

def save_issues_to_file(issues, file_path):
    with open(file_path, 'w') as file:
        json.dump(issues, file, indent=2)

# Usage
sonar_host = 'https://sonarcloud.io'
project_key = 'loans-service-restapi'
sonar_token = '273b52a0e0986e3d298f64e0768d31d01a0de09c'
issues = get_sonar_issues(sonar_host, project_key, sonar_token)
save_issues_to_file(issues, 'sonar_issues.json')
