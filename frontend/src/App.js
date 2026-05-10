# frontend/src/App.js
import React, { useEffect, useState } from 'react';
import './App.css';

function App() {
  const [contractors, setContractors] = useState([]);
  const [quoteRequest, setQuoteRequest] = useState({
    user_id: 1,
    items: [],
    budget: 0,
    request_datetime: new Date().toISOString(),
  });
  const [quotes, setQuotes] = useState([]);

  useEffect(() => {
    fetch(`${process.env.REACT_APP_API_URL}/contractors`)
      .then((res) => res.json())
      .then((data) => setContractors(data));
  }, []);

  const handleAddItem = () => {
    const item = prompt('Enter item (e.g., kitchen, bathroom)');
    if (item) {
      setQuoteRequest((prev) => ({
        ...prev,
        items: [...prev.items, item],
      }));
    }
  };

  const handleSubmit = () => {
    fetch(`${process.env.REACT_APP_API_URL}/quote-requests/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(quoteRequest),
    })
      .then((res) => res.json())
      .then((data) => setQuotes(data));
  };

  return (
    <div className="App">
      <h1>Home Improvement Service</h1>
      <div>
        <h2>Contractors</h2>
        <ul>
          {contractors.map((c) => (
            <li key={c.id}>
              {c.name} - {c.specialties.join(', ')} - Rating: {c.rating}
            </li>
          ))}
        </ul>
      </div>
      <div>
        <h2>Quote Request</h2>
        <button onClick={handleAddItem}>Add Item</button>
        <input
          type="number"
          placeholder="Budget"
          value={quoteRequest.budget}
          onChange={(e) =>
            setQuoteRequest((prev) => ({ ...prev, budget: parseFloat(e.target.value) }))
          }
        />
        <button onClick={handleSubmit}>Submit</button>
      </div>
      <div>
        <h2>Quotes</h2>
        <ul>
          {quotes.map((q) => (
            <li key={q.id}>
              Contractor ID: {q.contractor_id} - Amount: {q.amount}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default App;
