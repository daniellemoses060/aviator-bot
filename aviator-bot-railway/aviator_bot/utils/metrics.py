# Placeholder for tracking accuracy, precision, recall, etc.
def track_performance(prediction, actual):
    accuracy = (prediction == actual)
    precision = (prediction == 1 and actual == 1)
    recall = (prediction == 1 and actual == 1)
    f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
    return accuracy, precision, recall, f1_score
