import matplotlib.pyplot as plt

# Plot a scatter matrix to visualize the correlations between features
pd.plotting.scatter_matrix(movies_df[features], figsize=(12, 8))
plt.show()

# Plot a bar chart to visualize the distribution of revenue across genres
genres_df = movies_df.explode('genre')
genres_df.groupby('genre')['revenue'].mean().plot(kind='bar', figsize=(8, 6))
plt.show()
