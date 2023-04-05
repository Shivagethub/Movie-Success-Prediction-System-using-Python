# Use correlation analysis to identify important features
corr_matrix = movies_df.corr()
corr_matrix['revenue'].sort_values(ascending=False)

# Select relevant features
features = ['budget', 'popularity', 'release_year', 'release_month', 'profit', 'genre']
target = 'revenue'
