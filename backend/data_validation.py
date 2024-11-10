import pandas as pd

# Validate the CSV file data
def validate_data(filepath):
    required_columns = ['Revenue', 'Expenses', 'Profit']
    df = pd.read_csv(filepath)

    # Ensure all required columns are present
    return all(col in df.columns for col in required_columns)
