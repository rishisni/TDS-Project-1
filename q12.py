import pandas as pd

# Load user data from CSV
users_data = pd.read_csv('users.csv')

# Display the first few rows and info about the DataFrame
print("First few rows of the data:")
print(users_data.head())
print("\nDataFrame info:")
print(users_data.info())

# Check for NaN values in 'following' column
nan_count = users_data['following'].isna().sum()
print(f"\nNumber of NaN values in 'following' column: {nan_count}")

# Handle missing values in 'following' by filling NaN with 0
users_data['following'].fillna(0, inplace=True)

# Calculate the average following for hireable users
average_following_hireable = users_data[users_data['hireable'] == True]['following'].mean()

# Calculate the average following for non-hireable users
average_following_non_hireable = users_data[users_data['hireable'] == False]['following'].mean()

# Calculate the difference
difference = average_following_hireable - average_following_non_hireable

# Print the difference rounded to three decimal places
print("Average following per user for hireable minus non-hireable:", round(difference, 3))

# Count users in each category for debugging
hireable_count = users_data[users_data['hireable'] == True].shape[0]
non_hireable_count = users_data[users_data['hireable'] == False].shape[0]

print(f"\nNumber of hireable users: {hireable_count}")
print(f"Number of non-hireable users: {non_hireable_count}")
