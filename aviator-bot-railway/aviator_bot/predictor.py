def predict_entry(latest_multiplier):
    # Simple baseline strategy for safe testing
    threshold = 1.85
    confidence = "Medium"

    if latest_multiplier > threshold:
        signal = True
        cashout = round(latest_multiplier + 0.4, 2)
        confidence = "High" if latest_multiplier > 2.1 else "Medium"
    else:
        signal = False
        cashout = None

    return {
        "signal": signal,
        "cashout": cashout,
        "confidence": confidence
    }
