import numpy as np
from sklearn.linear_model import LinearRegression

def predict_bet(data):
    # Example of a regression model to predict the bet time (dummy example)
    
    # Gather historical multipliers for prediction (adjust as needed)
    multipliers = [data["multiplier"]]  # In a real case, this should be a history
    times = [1, 2, 3, 4, 5]  # Time series example

    model = LinearRegression()
    model.fit(np.array(times).reshape(-1, 1), np.array(multipliers))

    prediction = model.predict([[6]])  # Predict the next multiplier at time 6
    predicted_cashout = prediction[0]

    # Return the prediction as a Telegram message
    return f"Prediction: Bet now at time 6 with cashout {predicted_cashout:.2f}"
