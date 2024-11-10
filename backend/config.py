import os

# Configuration settings for the app
class Config:
    # Directory for uploaded files
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')

    # Allow only CSV files
    ALLOWED_EXTENSIONS = {'csv'}
    
    # SQLite database path
    SQLALCHEMY_DATABASE_URI = 'sqlite:///financial_analysis.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
