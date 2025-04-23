def predict_entry(multiplier):
    # Basic rule: if last multiplier is above 1.85x, consider it a signal
    signal = multiplier >= 1.85
    cashout = round(multiplier + 0.4, 2)
    confidence = "High" if multiplier >= 2.1 else "Medium"

    return {
        "signal": signal,
        "cashout": cashout if signal else None,
        "confidence": confidence if signal else "Low"
    }
