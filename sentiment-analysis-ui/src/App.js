import React, { useState } from "react";
import axios from "axios";

function App() {
  const [review, setReview] = useState("");
  const [sentiment, setSentiment] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = async () => {
    setLoading(true);
    setError(null);
    try {
      const response = await axios.post("http://localhost:5001/predict", {
        review: review,
      });
      setSentiment(response.data.sentiment);
    } catch (err) {
      setError("Error fetching sentiment. Make sure API is running.");
    }
    setLoading(false);
  };

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h1>Sentiment Analysis</h1>
      <textarea
        rows="4"
        cols="50"
        placeholder="Enter your review here..."
        value={review}
        onChange={(e) => setReview(e.target.value)}
      />
      <br />
      <button onClick={handleSubmit} disabled={loading}>
        {loading ? "Analyzing..." : "Analyze Sentiment"}
      </button>
      <br />
      {sentiment && <h2>Sentiment: {sentiment}</h2>}
      {error && <p style={{ color: "red" }}>{error}</p>}
    </div>
  );
}

export default App;
