import pandas as pd

# Load the CSV file
users_data = pd.read_csv('users.csv')

# Sort by 'created_at' and get the top 5 earliest registered users
earliest_users = users_data.sort_values(by='created_at').head(5)

# Extract the 'login' column and join the results in a comma-separated string
earliest_logins = ",".join(earliest_users['login'])

# Print the result
print("Earliest registered users in Boston:", earliest_logins)
