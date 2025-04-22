import time
from threading import Timer

def schedule_predictions(interval, callback):
    Timer(interval, callback).start()
