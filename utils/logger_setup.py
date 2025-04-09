import logging
import os
import sys
from datetime import datetime

from pythonjsonlogger import jsonlogger

from config.config import LOG_FORMAT, LOG_LEVEL


def setup_logger(name):
    logger = logging.getLogger(name)

    level = getattr(logging, LOG_LEVEL.upper(), logging.INFO)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    console_handler = logging.StreamHandler(sys.stdout)

    if LOG_FORMAT == "json":
        formatter = jsonlogger.JsonFormatter(
            "%(asctime)s-%(name)s-%(levelname)s-%(message)s",
            timestamp=True,
        )
    else:
        formatter = logging.Formatter(
            "%(asctime)s-%(name)s-%(levelname)s-%(message)s",
        )

    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    # creating a file handler to log to a file
    log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
    os.makedirs(log_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    # Example fix for line 41 being too long
    log_filename = f"{timestamp}_{name.replace('.', '_')}.log"
    log_file = os.path.join(log_dir, log_filename)

    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger
