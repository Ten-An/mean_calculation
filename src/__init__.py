"""Module for initializing the mean calculation package source."""

from .mean_calculation import calculate_mean
from .saver import save_results_to_json

__all__ = ["calculate_mean", "save_results_to_json"]
__version__ = "1.0.0"
__author__ = "Admin"
