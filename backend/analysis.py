import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Function to analyze financial data and generate insights
def analyze_financial_data(df):
    """
    Perform financial calculations and generate insights based on the provided financial data.
    :param df: pandas DataFrame containing financial data (e.g., Revenue, Expenses, etc.)
    :return: analysis_results (dict) and insights (list)
    """

    # Ensure the necessary columns exist in the DataFrame
    if 'Revenue' not in df.columns or 'Expenses' not in df.columns:
        raise ValueError("Missing necessary columns: 'Revenue' and 'Expenses'")

    # Perform financial calculations
    total_revenue = df['Revenue'].sum()
    total_expenses = df['Expenses'].sum()
    net_profit = total_revenue - total_expenses
    profit_margin = (net_profit / total_revenue) * 100 if total_revenue > 0 else 0

    # Generate basic insights based on the financial data
    insights = []
    if profit_margin < 10:
        insights.append("Profit margin is low. Consider reducing operational expenses or increasing revenue.")
    else:
        insights.append("Profit margin is healthy. Keep maintaining the current strategies.")

    if total_expenses > total_revenue:
        insights.append("Warning: Expenses are higher than revenue. Consider cost-cutting measures.")
    else:
        insights.append("Revenue exceeds expenses. Keep optimizing your financials for growth.")

    # Optionally, machine learning-based prediction (e.g., predict future revenue)
    # Let's assume the DataFrame has a 'Month' column that acts as a time series for ML prediction
    if 'Month' in df.columns:
        future_revenue_prediction, ml_insights = predict_future_revenue(df)
        insights.extend(ml_insights)
        insights.append(f"Projected revenue for next month: ${future_revenue_prediction:,.2f}")

    # Prepare the final analysis results to be returned
    analysis_results = {
        'Total Revenue': total_revenue,
        'Total Expenses': total_expenses,
        'Net Profit': net_profit,
        'Profit Margin (%)': profit_margin
    }

    return analysis_results, insights


# Machine Learning Model for predicting future revenue based on historical data
def predict_future_revenue(df):
    """
    Use a machine learning model to predict future revenue based on historical data.
    :param df: pandas DataFrame containing 'Month' and 'Revenue' columns
    :return: future_revenue_prediction (float) and additional insights (list)
    """

    # Ensure the necessary columns exist in the DataFrame
    if 'Month' not in df.columns or 'Revenue' not in df.columns:
        raise ValueError("Missing necessary columns: 'Month' and 'Revenue'")

    # Split the data into training and testing sets
    X = df[['Month']]  # Feature: Month (or any other time-related feature)
    y = df['Revenue']  # Target: Revenue
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a simple Linear Regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions on the test set and calculate accuracy
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    rmse = mse ** 0.5

    # Predict future revenue for the next month (let's assume next month is Month 13)
    future_revenue_prediction = model.predict([[13]])[0]

    # Insights based on the model's performance and predictions
    ml_insights = [
        f"Machine learning model RMSE: {rmse:.2f} (lower is better).",
        "The model uses historical revenue data to predict future revenue."
    ]

    return future_revenue_prediction, ml_insights

