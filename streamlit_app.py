import streamlit as st
import joblib

# Load the trained model and vectorizer
model = joblib.load('sentiment_model.joblib')
vectorizer = joblib.load('tfidf_vectorizer.joblib')

# Streamlit App
st.title("Sentiment Analysis")

# User input
review = st.text_area("Enter your review", "")

# Analyze sentiment when the user clicks the button
if st.button("Analyze Sentiment"):
    if review:
        # Transform the review using the vectorizer
        review_tfidf = vectorizer.transform([review])

        # Predict sentiment
        prediction = model.predict(review_tfidf)

        # Display the result
        sentiment = "positive" if prediction[0] == 1 else "negative"
        st.write(f"The sentiment is: {sentiment}")
    else:
        st.error("Please enter a review!")
