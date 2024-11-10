import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Perform financial analysis and machine learning predictions
def analyze_financial_data(df):
    # Calculate total financial metrics
    total_revenue = df['Revenue'].sum()
    total_expenses = df['Expenses'].sum()
    profit = total_revenue - total_expenses

    # ML Model: Predict future profits
    X = df[['Revenue', 'Expenses']]  # Features: Revenue, Expenses
    y = df['Profit']  # Target: Profit

    # Split data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Use Random Forest for prediction
    model = RandomForestRegressor()
    model.fit(X_train, y_train)

    # Make predictions
    predictions = model.predict(X_test)

    return {
        'Total Revenue': total_revenue,
        'Total Expenses': total_expenses,
        'Profit': profit,
        'Predictions': predictions.tolist()
    }
