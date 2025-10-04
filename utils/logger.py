"""Module for setup logging configuration."""

import logging
from logging import Logger


def setup_logging(log_file: str = "mean_calculation.log") -> logging.Logger:
    """Set up logging configuration.

    Args:
        log_file (str): The name of the log file. Defaults
        to 'mean_calculation.log'
    Returns:
        logging.Logger: Configured logger instance.
    """
    # File handler configuration
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    file_handler.setFormatter(file_formatter)

    # Console handler configuration
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)
    console_formatter = logging.Formatter("%(levelname)s - %(message)s")
    console_handler.setFormatter(console_formatter)

    # Logger configuration
    logger: Logger = logging.getLogger("mean_calculation_logger")
    logger.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
