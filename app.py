from flask import Flask, request, jsonify
import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('iris_model.pkl')

# Define a route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Get the JSON data from the request
    data = request.get_json()

    # Convert JSON data to DataFrame
    df = pd.DataFrame(data, index=[0])

    # Perform prediction
    prediction = model.predict(df)

    # Map numerical labels back to categorical species names
    species_map = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
    predicted_species = species_map[prediction[0]]

    # Return the predicted species
    return jsonify({'predicted_species': predicted_species})

if __name__ == '__main__':
    app.run(debug=True)
