import numpy as np
import datetime
import logging

history = []

def update_history(new_multiplier):
    timestamp = datetime.datetime.now().isoformat()
    history.append((timestamp, new_multiplier))
    if len(history) > 100:
        history.pop(0)

def predict_next_multiplier():
    if len(history) < 5:
        return 2.0  # default fallback
    values = [m for _, m in history[-20:]]
    trend = np.polyfit(range(len(values)), values, 1)
    prediction = trend[0] * len(values) + trend[1]
    return round(max(prediction, 1.5), 2)  # never predict below 1.5
