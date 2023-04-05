# Drop duplicates and irrelevant columns
movies_df.drop_duplicates(subset=['title'], keep='first', inplace=True)
movies_df.drop(['imdb_id', 'homepage', 'tagline', 'overview', 'runtime'], axis=1, inplace=True)

# Convert release_date column to datetime format
movies_df['release_date'] = pd.to_datetime(movies_df['release_date'], errors='coerce')

# Handle missing data
movies_df['budget'] = movies_df['budget'].replace(0, pd.NA)
movies_df['revenue'] = movies_df['revenue'].replace(0, pd.NA)

# Add new features
movies_df['release_year'] = movies_df['release_date'].dt.year
movies_df['release_month'] = movies_df['release_date'].dt.month
movies_df['profit'] = movies_df['revenue'] - movies_df['budget']



import matplotlib.pyplot as plt

# Plot a scatter matrix to visualize the correlations between features
pd.plotting.scatter_matrix(movies_df[features], figsize=(12, 8))
plt.show()

# Plot a bar chart to visualize the distribution of revenue across genres
genres_df = movies_df.explode('genre')
genres_df.groupby('genre')['revenue'].mean().plot(kind='bar', figsize=(8, 6))
plt.show()
