import sqlite3

# Initialize the database with the necessary table
def init_db():
    conn = sqlite3.connect('financial_analysis.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS analysis_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            total_revenue REAL,
            total_expenses REAL,
            profit REAL,
            predictions TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Save the analysis results to the database
def save_analysis_results(results):
    conn = sqlite3.connect('financial_analysis.db')
    c = conn.cursor()

    # Insert the analysis results into the table
    c.execute('''
        INSERT INTO analysis_results (total_revenue, total_expenses, profit, predictions)
        VALUES (?, ?, ?, ?)
    ''', (results['Total Revenue'], results['Total Expenses'], results['Profit'], str(results['Predictions'])))
    conn.commit()
    conn.close()
