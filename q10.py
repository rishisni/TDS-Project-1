import pandas as pd
import statsmodels.api as sm

# Load user data from CSV
users_data = pd.read_csv('users.csv')

# Define the independent variable (public repositories) and the dependent variable (followers)
X = users_data['public_repos']
y = users_data['followers']

# Add a constant to the independent variable
X = sm.add_constant(X)

# Perform linear regression
model = sm.OLS(y, X).fit()

# Get the slope (coefficient) of public_repos
slope = model.params['public_repos']

# Print the slope rounded to three decimal places
print("Regression slope of followers on public repositories:", round(slope, 3))
