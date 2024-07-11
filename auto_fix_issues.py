import os
import openai
import json

# Set up the OpenAI API key from the environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

def load_issues(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def get_openai_suggestion(issue_description, code_snippet):
    prompt = f"Here is a code snippet:\n{code_snippet}\n\nIssue: {issue_description}\n\nPlease provide a fixed version of the code."
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def apply_fix(file_path, issue):
    print(f"Applying fix for issue: {issue['message']} in file: {file_path}")
    with open(file_path, 'r') as file:
        content = file.read()

    # Get a code snippet to fix
    code_snippet = content  # This could be refined to only take relevant parts
    fix_suggestion = get_openai_suggestion(issue['message'], code_snippet)

    # Apply the fix
    fixed_content = content.replace(code_snippet, fix_suggestion)
    with open(file_path, 'w') as file:
        file.write(fixed_content)

def apply_fixes(issues):
    for issue in issues:
        component = issue.get('component')
        if not component:
            continue

        file_path = component.replace('.', os.sep) + '.java'
        file_path = os.path.join('src', 'main', 'java', file_path)

        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            continue

        apply_fix(file_path, issue)

if __name__ == "__main__":
    issues = load_issues('sonar_issues.json')
    apply_fixes(issues