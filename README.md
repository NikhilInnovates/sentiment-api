

---

# Sentiment Analysis API and Frontend

This project is a **Sentiment Analysis Application** where users can input reviews and get the sentiment prediction (Positive/Negative). The application consists of the following components:

- **Flask API**: A RESTful API for running the sentiment analysis model.
- **Sentiment Analysis Model**: A trained machine learning model for sentiment classification.
- **Frontend**: A React-based web application to interact with the API and display sentiment predictions.
- **Deployment**: The API is deployed using Docker and the frontend is served via React.

- Here you can access the deployed project :

https://sentiment-api-ch2dwq7kgu3dopuxwndzyx.streamlit.app/

## Project Structure

```
sentiment-api/
├── Flask_API.py            # Flask API backend
├── sentiment_model.joblib  # Trained sentiment analysis model
├── tfidf_vectorizer.joblib # TF-IDF Vectorizer
├── Dockerfile              # Dockerfile for API deployment
├── requirements.txt        # Python dependencies
├── sentiment-analysis-ui/  # Frontend React app
│   ├── public/
│   ├── src/
│   └── package.json
├── .gitignore              # Git ignore file
└── README.md               # Project README (this file)
```

## Features

- **Sentiment Analysis API**:
  - The backend API is built with Flask.
  - The model uses a **TF-IDF vectorizer** to transform text input and a **Machine Learning classifier** to predict sentiment (positive or negative).
  - The API exposes a `POST` endpoint `/predict` that accepts JSON data with a review and returns the sentiment prediction.

- **Frontend Web Application**:
  - A simple React application where users can type reviews and click a button to analyze sentiment.
  - The React app interacts with the API, sending the review to the backend and displaying the sentiment response.

## Requirements

- Python 3.x
- Node.js (for React)
- Docker (for containerization)

### Backend (Flask API)

1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the Flask API locally:
   ```bash
   python Flask_API.py
   ```
   The API will run on `http://localhost:5000` by default (or port 8080 if configured).

### Frontend (React)

1. Navigate to the frontend directory:
   ```bash
   cd sentiment-analysis-ui
   ```

2. Install the required Node.js packages:
   ```bash
   npm install
   ```

3. Start the React development server:
   ```bash
   npm start
   ```
   The frontend will be available at `http://localhost:3000` by default.

### Docker (for both Backend and Frontend)

#### Docker for Backend (Flask API)

1. Build the Docker image for the API:
   ```bash
   docker build -t sentiment-api .
   ```

2. Run the Docker container:
   ```bash
   docker run -p 8080:8080 sentiment-api
   ```

#### Docker for Frontend (React)

1. Navigate to the `sentiment-analysis-ui` folder:
   ```bash
   cd sentiment-analysis-ui
   ```

2. Build the Docker image for the React app:
   ```bash
   docker build -t sentiment-ui .
   ```

3. Run the Docker container:
   ```bash
   docker run -p 3000:3000 sentiment-ui
   ```

### Deployment (Serverless/API)

1. Upload the model and vectorizer files to **AWS S3**.
2. Use **AWS Lambda** and **API Gateway** to deploy the Flask API serverless, ensuring it can handle incoming POST requests.

## CI/CD Pipeline with GitHub Actions

This project is integrated with **GitHub Actions** to automate continuous integration and deployment.

### Steps:
- On every push or pull request to the `main` branch, GitHub Actions will:
  1. Run tests on the backend and frontend.
  2. Deploy the backend and frontend applications automatically.

### Setup CI/CD:
1. Create a `.github` folder in the root of the repository.
2. Inside `.github`, create a `workflows` folder.
3. Create a workflow YAML file (e.g., `deploy.yml`) for automating deployment.

Example of a simple CI/CD workflow for deploying:

```yaml
name: Deploy Sentiment API

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v2

      - name: Set up Python environment
        uses: actions/setup-python@v2
        with:
          python-version: '3.8'

      - name: Install dependencies
        run: |
          pip install -r requirements.txt

      - name: Run Flask API tests
        run: |
          pytest

      - name: Build and push Docker images
        run: |
          docker build -t sentiment-api .
          docker push sentiment-api
```

## Troubleshooting

- **Error fetching sentiment**: Make sure the API is running correctly and accessible.
- **CORS issues**: Ensure CORS is enabled in the Flask API if you are calling it from a different domain (use `flask_cors`).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

