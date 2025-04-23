import numpy as np
import pandas as pd
from datetime import datetime
from sklearn.linear_model import LinearRegression
import logging

# Historical multipliers memory (can later be persisted to DB or JSON)
multiplier_history = []

def update_history(new_multiplier):
    if new_multiplier:
        multiplier_history.append({
            "time": datetime.now(),
            "multiplier": new_multiplier
        })

        # Keep last 100 multipliers
        if len(multiplier_history) > 100:
            multiplier_history.pop(0)

def get_features():
    df = pd.DataFrame(multiplier_history)
    if df.empty or len(df) < 10:
        return None

    df["timestamp"] = df["time"].astype("int64") // 10**9
    df["rolling_mean"] = df["multiplier"].rolling(window=10).mean()
    df["rolling_max"] = df["multiplier"].rolling(window=10).max()
    df["rolling_var"] = df["multiplier"].rolling(window=10).var()

    # Streak detection
    streaks = []
    streak = 1
    for i in range(1, len(df)):
        if df["multiplier"].iloc[i] > 2.0 and df["multiplier"].iloc[i-1] > 2.0:
            streak += 1
        else:
            streak = 1
        streaks.append(streak)
    streaks.insert(0, 1)
    df["streak"] = streaks

    return df

def predict_next_cashout():
    df = get_features()
    if df is None or len(df) < 10:
        return "1.80x – 2.20x", 50  # Default range with low confidence

    recent = df.tail(10)

    # Simple regression model
    try:
        X = recent["timestamp"].values.reshape(-1, 1)
        y = recent["multiplier"].values
        model = LinearRegression().fit(X, y)
        prediction = model.predict([[datetime.now().timestamp()]])[0]

        # Confidence score (normalized range)
        var = recent["rolling_var"].mean()
        confidence = max(30, min(100, 100 - var * 10))

        # Adjust range
        if prediction < 1.8:
            return "1.80x – 2.20x", confidence
        elif prediction < 3.0:
            return "2.00x – 3.00x", confidence
        else:
            return "3.00x – 5.00x", confidence
    except Exception as e:
        logging.error(f"Prediction error: {e}")
        return "1.80x – 2.20x", 40
