import pandas as pd

# Load repository data from CSV
repos_data = pd.read_csv('repositories.csv')

# Check if 'has_projects' and 'has_wiki' columns exist
if 'has_projects' in repos_data.columns and 'has_wiki' in repos_data.columns:
    # Calculate the correlation
    correlation = repos_data['has_projects'].corr(repos_data['has_wiki'])

    # Print the correlation rounded to three decimal places
    print("Correlation between projects and wiki enabled:", round(correlation, 3))
else:
    print("Columns 'has_projects' or 'has_wiki' not found in the repository data.")
