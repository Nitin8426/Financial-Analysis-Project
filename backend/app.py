from flask import Flask, render_template, request, jsonify
import os
import pandas as pd
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from analysis import analyze_financial_data
from utils import allowed_file, validate_data
from database import save_analysis_results

# Initialize the Flask app
app = Flask(__name__)

# Set the upload folder for CSV files
app.config['UPLOAD_FOLDER'] = 'uploads/'
ALLOWED_EXTENSIONS = {'csv'}

# Function to check if the file is allowed (CSV)
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route for the home page where users can upload CSV files
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

# Route for uploading and processing the CSV file
@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if the request contains a file
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']

    # Check if a file is selected
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Check if the file format is allowed (CSV)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Validate the CSV data format
        if not validate_data(filepath):
            return jsonify({'error': 'Invalid data format in CSV file'}), 400

        # Read the CSV file into a DataFrame
        df = pd.read_csv(filepath)

        # Perform financial analysis on the DataFrame
        analysis_results, insights = analyze_financial_data(df)

        # Save the results to the database
        save_analysis_results(analysis_results)

        # Render the results page with the analysis summary and insights
        return render_template("results.html", tables=df.to_html(), analysis=analysis_results, insights=insights)

    return jsonify({'error': 'Invalid file format. Only CSV is allowed'}), 400

# Start the Flask server
if __name__ == '__main__':
    # Ensure the uploads directory exists
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    
    # Run the app
    app.run(debug=True)
