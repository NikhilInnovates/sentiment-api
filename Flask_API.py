from flask import Flask, request, jsonify
from flask_cors import CORS  # Add this import
import joblib

# Initialize the Flask application
app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# Load the saved model and vectorizer
model = joblib.load('sentiment_model.joblib')
vectorizer = joblib.load('tfidf_vectorizer.joblib')

@app.route('/')
def home():
    return "Sentiment Analysis API is Running"

# Prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
    # Get the review from the request
    data = request.get_json()

    # Check if 'review' key is in the data
    if 'review' not in data:
        return jsonify({"error": "No review provided"}), 400

    review = data['review']

    # Transform the review using the vectorizer
    review_tfidf = vectorizer.transform([review])

    # Predict sentiment using the model
    prediction = model.predict(review_tfidf)

    # Convert prediction to sentiment (optional, if labels were 0=negative, 1=positive)
    sentiment = 'positive' if prediction[0] == 1 else 'negative'

    return jsonify({'review': review, 'sentiment': sentiment})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)  # Change port to 8080
