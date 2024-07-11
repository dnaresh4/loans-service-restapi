import requests
import json

def get_sonar_issues(sonar_host, project_key, sonar_token):
    url = f"https://sonarcloud.io/api/issues/search?componentKeys=dnaresh4_loans-service-restapi"
    headers = {
        'Authorization': f'Basic {sonar_token}',
    }
    response = requests.get(url, headers=headers)
    issues = response.json().get('issues', [])
    return issues

sonar_host = 'https://sonarcloud.io'
project_key = 'dnaresh4_loans-service-restapi'
sonar_token = '273b52a0e0986e3d298f64e0768d31d01a0de09c'

issues = get_sonar_issues(sonar_host, project_key, sonar_token)
with open('sonar_issues.json', 'w') as f:
    json.dump(issues, f, indent=4)
