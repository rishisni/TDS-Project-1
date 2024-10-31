import pandas as pd

# Load the repository data
repos_data = pd.read_csv('repositories.csv')

# Count occurrences of each programming language, ignoring missing values
language_counts = repos_data['language'].value_counts()

# Get the most popular programming language
most_popular_language = language_counts.idxmax()

# Print the result
print("Most popular programming language among developers:", most_popular_language)
