import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [gender, setGender] = useState('Male');
  const [nationality, setNationality] = useState('');
  const [age, setAge] = useState('');
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);
    setResult(null);

    try {
      const response = await axios.post('http://127.0.0.1:8000/predict', {
        Gender: gender,
        Nationality: nationality,
        Age: parseInt(age)
      });
      setResult(response.data);
    } catch (err) {
      setError('Failed to fetch prediction. Please try again.');
    }
  };

  return (
    <div className="app">
      <div className="form-wrapper">
        <h1>Food Preference Prediction</h1>
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label>Gender:</label>
            <select value={gender} onChange={(e) => setGender(e.target.value)}>
              <option value="Male">Male</option>
              <option value="Female">Female</option>
            </select>
          </div>

          <div className="form-group">
            <label>Nationality:</label>
            <select
              value={nationality}
              onChange={(e) => setNationality(e.target.value)}
              required
            >
              <option value="" disabled>
                Select Nationality
              </option>
              <option value="Indian">Indian</option>
              <option value="Pakistani">Pakistani</option>
              <option value="Tanzanian">Tanzanian</option>
              <option value="Indonesia">Indonesia</option>
              <option value="Muslim">Muslim</option>
              <option value="Pakistan">Pakistan</option>
              <option value="Maldivian">Maldivian</option>
              <option value="MY">MY</option>
              <option value="Malaysian">Malaysian</option>
              <option value="Indonesian">Indonesian</option>
              <option value="Malaysia">Malaysia</option>
              <option value="Canadian">Canadian</option>
              <option value="Nigerian">Nigerian</option>
              <option value="Algerian">Algerian</option>
              <option value="Korean">Korean</option>
              <option value="Seychellois">Seychellois</option>
              <option value="Indonesain">Indonesain</option>
              <option value="Japan">Japan</option>
              <option value="China">China</option>
              <option value="Mauritian">Mauritian</option>
              <option value="Yemen">Yemen</option>
            </select>
          </div>

          <div className="form-group">
            <label>Age:</label>
            <input
              type="number"
              value={age}
              onChange={(e) => setAge(e.target.value)}
              min="0"
              max="120"
              required
            />
          </div>

          <button type="submit" className="submit-btn">Predict</button>
        </form>

        {result && (
          <div className="result">
            <h2>Prediction Result</h2>
            <p>
              <strong>Type of food Preference: </strong>
              {result.Food}
            </p>
            <p>
              <strong>Juice Preference: </strong>
              {result.Juice}
            </p>
            <p>
              <strong>Preference for Dessert: </strong>
              {result.Dessert}
            </p>
          </div>
        )}

        {error && <p className="error">{error}</p>}
      </div>
    </div>
  );
}

export default App;
