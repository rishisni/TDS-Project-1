import pandas as pd

# Load the user data from CSV
users_data = pd.read_csv('users.csv')

# Convert the 'created_at' column to datetime
users_data['created_at'] = pd.to_datetime(users_data['created_at'])

# Filter users who joined after 2020
users_after_2020 = users_data[users_data['created_at'] > '2020-01-01']

# Load the repository data
repos_data = pd.read_csv('repositories.csv')

# Filter repositories for the users who joined after 2020
repos_after_2020 = repos_data[repos_data['login'].isin(users_after_2020['login'])]

# Count occurrences of each programming language, ignoring missing values
language_counts = repos_after_2020['language'].value_counts()

# Get the second most popular programming language
if len(language_counts) > 1:
    second_most_popular_language = language_counts.index[1]
else:
    second_most_popular_language = "Not enough data"

# Print the result
print("Second most popular programming language among users who joined after 2020:", second_most_popular_language)
