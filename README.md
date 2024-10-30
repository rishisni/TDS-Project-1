* The data was scraped using the GitHub API and includes users from Boston with over 100 followers and their public repositories.
* An interesting insight was the range of programming languages popular among Boston-based developers.
* Developers should consider including licenses in repositories, as we found many repos lacked clear licensing information.

# Project Overview
This project uses the GitHub API to fetch data on GitHub users located in Boston with over 100 followers and details about their repositories.

## Files
- `users.csv`: Contains information about users, including their username, company, bio, and follower count.
- `repositories.csv`: Lists the most recent repositories for each user, including stars, watchers, and primary language.

## Running the Script
- To use this script, ensure you have a valid GitHub API token and replace `'YOUR_GITHUB_TOKEN'` in the script.
- Run the script to fetch data and generate `users.csv` and `repositories.csv`.
