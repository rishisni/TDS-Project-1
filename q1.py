import pandas as pd

# Load users data from CSV
users_df = pd.read_csv('users.csv')

# Sort users by followers in descending order and select top 5
top_users = users_df.sort_values(by='followers', ascending=False).head(5)

# Get logins of top users as a comma-separated string
top_user_logins = ', '.join(top_users['login'].tolist())

print(top_user_logins)

