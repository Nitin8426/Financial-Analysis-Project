import React, { useState } from 'react';
import axios from 'axios';
import FileUpload from './components/FileUpload';
import AnalysisResults from './components/AnalysisResults';
import './App.css';

function App() {
  const [results, setResults] = useState(null);
  const [error, setError] = useState(null);

  const handleFileUpload = (file) => {
    const formData = new FormData();
    formData.append('file', file);

    axios.post('http://127.0.0.1:5000/upload', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    })
      .then(response => {
        setResults(response.data);
        setError(null);
      })
      .catch(err => {
        setError('Failed to upload file. Please try again.');
        setResults(null);
      });
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>MSME Financial Analysis</h1>
      </header>
      <FileUpload onFileUpload={handleFileUpload} />
      {error && <p className="error">{error}</p>}
      {results && <AnalysisResults data={results} />}
    </div>
  );
}

export default App;
