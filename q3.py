import pandas as pd

# Load the repository data
repos_data = pd.read_csv('repositories.csv')

# Filter out missing licenses and count the occurrences
license_counts = repos_data[repos_data['license_name'].notna()]['license_name'].value_counts()

# Get the top 3 most popular licenses
top_licenses = license_counts.head(3).index.tolist()

# Print the result as a comma-separated string
print("Most popular licenses:", ",".join(top_licenses))
