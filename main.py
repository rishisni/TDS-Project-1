import requests
import pandas as pd
import time
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the GitHub token from the environment variable
TOKEN = os.getenv('GITHUB_TOKEN')
HEADERS = {'Authorization': f'token {TOKEN}'}
rate_limit_url = "https://api.github.com/rate_limit"

response = requests.get(rate_limit_url, headers=HEADERS)
print(response.json())
USER_PARAMS = {'q': 'location:Boston followers:>100'}

# Filenames
USER_FILE = 'users.csv'
REPO_FILE = 'repositories.csv'
README_FILE = 'README.md'

# Helper functions
def clean_company_name(company):
    if not isinstance(company, str):
        return ""
    cleaned = company.lstrip('@').strip().upper()
    return cleaned

# Fetch user data
def fetch_users_in_boston():
    print("Fetching user data...")
    users_url = 'https://api.github.com/search/users'
    users_data = []
    response = requests.get(users_url, headers=HEADERS, params=USER_PARAMS).json()

    if 'items' not in response:
        print("No user data found. Check your API rate limit or query.")
        return users_data
    
    for item in response['items']:
        user_detail = requests.get(item['url'], headers=HEADERS).json()
        users_data.append({
            'login': user_detail.get('login', ''),
            'name': user_detail.get('name', ''),
            'company': clean_company_name(user_detail.get('company', '')),
            'location': user_detail.get('location', ''),
            'email': user_detail.get('email', ''),
            'hireable': user_detail.get('hireable', ''),
            'bio': user_detail.get('bio', ''),
            'public_repos': user_detail.get('public_repos', 0),
            'followers': user_detail.get('followers', 0),
            'following': user_detail.get('following', 0),
            'created_at': user_detail.get('created_at', '')
        })
        time.sleep(1)  # To avoid rate limits
    print(f"Fetched {len(users_data)} users.")
    return users_data

# Fetch repositories for each user
def fetch_repositories_for_users(users):
    print("Fetching repository data...")
    repos_data = []
    for user in users:
        repos_url = f"https://api.github.com/users/{user['login']}/repos"
        response = requests.get(repos_url, headers=HEADERS, params={'per_page': 500}).json()
        
        for repo in response:
            repos_data.append({
                'login': user['login'],
                'full_name': repo.get('full_name', ''),
                'created_at': repo.get('created_at', ''),
                'stargazers_count': repo.get('stargazers_count', 0),
                'watchers_count': repo.get('watchers_count', 0),
                'language': repo.get('language', ''),
                'has_projects': repo.get('has_projects', False),
                'has_wiki': repo.get('has_wiki', False),
                'license_name': repo.get('license', {}).get('key', '') if repo.get('license') else ''
            })
        time.sleep(1)  # To avoid rate limits
    print(f"Fetched {len(repos_data)} repositories.")
    return repos_data


# Save data to CSV
def save_to_csv(data, filename):
    if data:
        pd.DataFrame(data).to_csv(filename, index=False)
        print(f"Saved data to {filename}")
    else:
        print(f"No data to save for {filename}")

# Create README.md
def create_readme():
    content = """\
* The data was scraped using the GitHub API and includes users from Boston with over 100 followers and their public repositories.
* An interesting insight was the range of programming languages popular among Boston-based developers.
* Developers should consider including licenses in repositories, as we found many repos lacked clear licensing information.

# Project Overview
This project uses the GitHub API to fetch data on GitHub users located in Boston with over 100 followers and details about their repositories.

## Files
- `users.csv`: Contains information about users, including their username, company, bio, and follower count.
- `repositories.csv`: Lists the most recent repositories for each user, including stars, watchers, and primary language.

## Running the Script
- To use this script, ensure you have a valid GitHub API token and replace `'YOUR_GITHUB_TOKEN'` in the script.
- Run the script to fetch data and generate `users.csv` and `repositories.csv`.
"""
    with open(README_FILE, 'w') as file:
        file.write(content)
    print(f"README.md created at {README_FILE}")

# Main script
if __name__ == '__main__':
    # Fetch and save user data
    users_data = fetch_users_in_boston()
    save_to_csv(users_data, USER_FILE)

    # Fetch and save repository data
    if users_data:
        repos_data = fetch_repositories_for_users(users_data)
        save_to_csv(repos_data, REPO_FILE)

    # Create README
    create_readme()
