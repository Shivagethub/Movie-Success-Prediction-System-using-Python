import pandas as pd

# Load data from a CSV file
movies_df = pd.read_csv('movies.csv')


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


# Use correlation analysis to identify important features
corr_matrix = movies_df.corr()
corr_matrix['revenue'].sort_values(ascending=False)

# Select relevant features
features = ['budget', 'popularity', 'release_year', 'release_month', 'profit', 'genre']
target = 'revenue'



import matplotlib.pyplot as plt

# Plot a scatter matrix to visualize the correlations between features
pd.plotting.scatter_matrix(movies_df[features], figsize=(12, 8))
plt.show()

# Plot a bar chart to visualize the distribution of revenue across genres
genres_df = movies_df.explode('genre')
genres_df.groupby('genre')['revenue'].mean().plot(kind='bar', figsize=(8, 6))
plt.show()


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(movies_df[features], movies_df[target], test_size=0.2, random_state=42)

# Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the testing set and calculate the R2 score
y_pred = model.predict(X_test)
score = r2_score(y_test, y_pred)
print(f'R2 score: {score}')


from sklearn.metrics import mean_squared_error

# Calculate the mean squared error of the predictions
mse = mean_squared_error(y_test, y_pred)
print(f'Mean squared error: {mse}')


from flask import Flask, request, jsonify

# Create a Flask app and define an API endpoint for making predictions
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    budget = data['budget']
    popularity = data['popularity']
    release_year = data['release_year']
    release_month = data['release_month']
    profit = data['profit']
    genre = data['genre']
    
    # Preprocess input data and make a prediction
    input_data = [[budget, popularity, release_year, release_month, profit, genre]]
    prediction = model.predict(input_data)[0]
    
    # Return the prediction as a JSON response
    return jsonify({'re
