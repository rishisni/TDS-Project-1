import pandas as pd

# Load user data from CSV
users_data = pd.read_csv('users.csv')

# Calculate the correlation between followers and public repositories
correlation = users_data['followers'].corr(users_data['public_repos'])

# Print the correlation rounded to three decimal places
print("Correlation between followers and public repositories:", round(correlation, 3))
