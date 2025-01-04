import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [gender, setGender] = useState('male');
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
    <div className="App">
      <h1>Food Preference Prediction</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Gender:</label>
          <select value={gender} onChange={(e) => setGender(e.target.value)}>
            <option value="male">Male</option>
            <option value="female">Female</option>
          </select>
        </div>

        <div>
          <label>Nationality:</label>
          <select value={nationality} onChange={(e) => setNationality(e.target.value)} required>
            <option value="" disabled> Select Nationality</option>
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


        <div>
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

        <button type="submit">Predict</button>
      </form>

      {result && (
        <div>
          <h2>Prediction Result</h2>
          <p><strong>Type of food Preference:</strong> {result.Food}</p>
          <p><strong>Juice Preference:</strong> {result.Juice}</p>
          <p><strong>Preference for Dessert:</strong> {result.Dessert}</p>
        </div>
      )}

      {error && <p style={{ color: 'red' }}>{error}</p>}
    </div>
  );
}

export default App;
