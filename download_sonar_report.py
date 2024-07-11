import requests

def get_sonar_issues(sonar_host, project_key, sonar_token):
    url = f"{sonar_host}/api/issues/search?projectKeys={project_key}"
    headers = {
        'Authorization': f'Bearer {sonar_token}'
    }
    response = requests.get(url, headers=headers)

    # Debugging statements
    print(f"Status Code: {response.status_code}")
    print(f"Response Content: {response.text}")

    response.raise_for_status()  # Raise an HTTPError if the HTTP request returned an unsuccessful status code

    issues = response.json().get('issues', [])
    return issues

# Usage
sonar_host = 'https://sonarcloud.io'
project_key = 'dnaresh4_loans-service-restapi'
sonar_token = '273b52a0e0986e3d298f64e0768d31d01a0de09c'

issues = get_sonar_issues(sonar_host, project_key, sonar_token)
print(issues)