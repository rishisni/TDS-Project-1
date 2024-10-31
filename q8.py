import pandas as pd

# Load user data from CSV
users_data = pd.read_csv('users.csv')

# Calculate leader_strength
users_data['leader_strength'] = users_data['followers'] / (1 + users_data['following'])

# Get the top 5 users based on leader_strength
top_leaders = users_data.nlargest(5, 'leader_strength')

# Get their logins in order
top_logins = top_leaders['login'].tolist()

# Print the result as a comma-separated string
print("Top 5 users by leader_strength:", ",".join(top_logins))
