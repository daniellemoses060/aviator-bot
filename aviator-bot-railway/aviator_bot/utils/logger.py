import logging

def log_info(message):
    logging.basicConfig(level=logging.INFO)
    logging.info(message)

def log_error(message):
    logging.basicConfig(level=logging.ERROR)
    logging.error(message)
