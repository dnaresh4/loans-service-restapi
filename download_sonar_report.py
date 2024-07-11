import requests
import json

def get_sonar_issues(sonar_host, project_key, sonar_token):
    url = f"{sonar_host}/api/issues/search?componentKeys={project_key}"
    headers = {
        'Authorization': f'Basic {sonar_token}',
    }
    response = requests.get(url, headers=headers)
    issues = response.json().get('issues', [])
    return issues

sonar_host = 'https://sonarcloud.io'
project_key = 'dnaresh4_loans-service-restapi'
sonar_token = 'YOUR_SONAR_TOKEN'

issues = get_sonar_issues(sonar_host, project_key, sonar_token)
with open('sonar_issues.json', 'w') as f:
    json.dump(issues, f, indent=4)
