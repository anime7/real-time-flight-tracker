"""Test script to verify logging functionality."""
from utils.logger_setup import setup_logger

# Get a logger for this module
logger = setup_logger(__name__)


def main():
    """Test logging at different levels."""
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")


if __name__ == "__main__":
    main()
