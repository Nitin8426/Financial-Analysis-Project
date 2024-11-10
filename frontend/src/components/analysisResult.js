import React from 'react';
import { Bar } from 'react-chartjs-2';
import './AnalysisResults.css';

const AnalysisResults = ({ data }) => {
  const { analysis, insights } = data;

  // Example chart data for visualizing Revenue, Expenses, Profit
  const chartData = {
    labels: ['Revenue', 'Expenses', 'Profit'],
    datasets: [{
      label: 'Financial Metrics',
      data: [analysis['Total Revenue'], analysis['Total Expenses'], analysis['Profit']],
      backgroundColor: ['rgba(75, 192, 192, 0.6)', 'rgba(255, 99, 132, 0.6)', 'rgba(54, 162, 235, 0.6)'],
    }]
  };

  return (
    <div className="analysis-results">
      <h2>Analysis Results</h2>
      <div className="chart-container">
        <Bar data={chartData} />
      </div>
      <h3>Insights</h3>
      <ul>
        {insights.map((insight, index) => (
          <li key={index}>{insight}</li>
        ))}
      </ul>
    </div>
  );
};

export default AnalysisResults;
