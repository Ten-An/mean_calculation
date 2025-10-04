"""_Module for initializing the tests package."""

from .conftest import sample_data
from .test_mean_calculation import (
    test_calculate_mean_with_valid_data,
    test_calculate_mean_with_empty_data,
)

__all__ = [
    "sample_data",
    "test_calculate_mean_with_valid_data",
    "test_calculate_mean_with_empty_data",
]
__version__ = "1.0.0"
__author__ = "Admin"
