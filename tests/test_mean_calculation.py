"""Module for testing the mean calculation functionality."""

from .conftest import sample_data
from src.mean_calculation import calculate_mean


def test_calculate_mean_with_valid_data(sample_data):
    """Test calculate_mean with valid data."""
    result = calculate_mean(sample_data)
    assert result == {"mean of data": 30.0}


def test_calculate_mean_with_empty_data():
    """Test calculate_mean with empty data."""
    try:
        calculate_mean([])
    except FileNotFoundError as e:
        assert str(e) == "The data doesn't exist"
