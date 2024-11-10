import React, { useState } from 'react';
import './FileUpload.css';

const FileUpload = ({ onFileUpload }) => {
  const [file, setFile] = useState(null);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    if (file) {
      onFileUpload(file);
    }
  };

  return (
    <div className="file-upload">
      <form onSubmit={handleSubmit}>
        <input type="file" accept=".csv" onChange={handleFileChange} />
        <button type="submit">Upload and Analyze</button>
      </form>
    </div>
  );
};

export default FileUpload;
