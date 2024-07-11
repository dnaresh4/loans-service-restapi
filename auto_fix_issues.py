import json
import re

def fix_code(file_path, issue):
    with open(file_path, 'r') as file:
        content = file.read()

    # Example fix: Replace 'System.out.println' with a logger
    if 'System.out.println' in content:
        content = content.replace('System.out.println', 'logger.info')

    with open(file_path, 'w') as file:
        file.write(content)

def apply_fixes(issues):
    for issue in issues:
        file_path = issue['component'].replace('.', '/') + '.java'  # Adjust for your project structure
        fix_code(file_path, issue)

with open('sonar_issues.json', 'r') as f:
    issues = json.load(f)

apply_fixes(issues)
