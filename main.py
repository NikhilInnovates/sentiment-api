import pandas as pd
import nltk
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from nltk.corpus import stopwords
import string
from sklearn.metrics import classification_report
import joblib


# Read dataset
df = pd.read_csv("IMDB Dataset.csv")
print(df.head())

#prepocess
print(df.isnull().sum())
data = df.dropna()  # Remove rows with missing values



# Download necessary nltk resources
nltk.download('stopwords')


# Function to preprocess text
def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()

    # Remove punctuation
    text = ''.join([char for char in text if char not in string.punctuation])

    # Tokenize and remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = text.split()
    tokens = [word for word in tokens if word not in stop_words]

    return ' '.join(tokens)


# Apply the preprocessing function
data['review'] = data['review'].apply(preprocess_text)

# Split dataset into training and testing data
X = data['review']
y = data['sentiment']

# Convert sentiments to numeric if necessary (for binary classification: 0 = negative, 1 = positive)
y = y.map({'negative': 0, 'positive': 1})  # Adjust based on your sentiment column labels

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# TF-IDF Vectorization
vectorizer = TfidfVectorizer(max_features=5000)
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Initialize and train the Logistic Regression model
model = LogisticRegression()
model.fit(X_train_tfidf, y_train)

# Predict on the test data
y_pred = model.predict(X_test_tfidf)

# Evaluate the model's performance
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')
print(classification_report(y_test, y_pred))

# Save the trained model to a file
joblib.dump(model, 'sentiment_model.joblib')

# Save the vectorizer to a file (we'll need this to transform new text inputs)
joblib.dump(vectorizer, 'tfidf_vectorizer.joblib')

print("Model and vectorizer saved successfully!")