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
