import pandas as pd

# Load the repository data
repos_data = pd.read_csv('repositories.csv')

# Group by 'language' and calculate the average number of stars
average_stars = repos_data.groupby('language')['stargazers_count'].mean()

# Get the language with the highest average number of stars
highest_avg_stars_language = average_stars.idxmax()
highest_avg_stars_value = average_stars.max()

# Print the result
print(f"Language with the highest average number of stars per repository: {highest_avg_stars_language} (Average Stars: {highest_avg_stars_value:.2f})")
