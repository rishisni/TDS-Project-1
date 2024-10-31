# import pandas as pd

# # Load users data from CSV
# users_df = pd.read_csv('users.csv')

# # Sort users by followers in descending order and select top 5
# top_users = users_df.sort_values(by='followers', ascending=False).head(5)

# # Get logins of top users as a comma-separated string
# top_user_logins = ', '.join(top_users['login'].tolist())

# print(top_user_logins)

import csv

# Define the list to store users from Delhi
users_in_delhi = []

# Read the CSV file with UTF-8 encoding
with open('users.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        location = row['location'].strip().lower()
        # Check if the user is from Delhi
        if 'boston' in location:
            users_in_delhi.append({
                'login': row['login'],
                'followers': int(row['followers'])
            })

# Sort users based on followers in descending order
top_users = sorted(users_in_delhi, key=lambda x: x['followers'], reverse=True)

# Extract the top 5 user logins
top_5_logins = [user['login'] for user in top_users[:5]]

# Print the result as a comma-separated list
print(','.join(top_5_logins))
