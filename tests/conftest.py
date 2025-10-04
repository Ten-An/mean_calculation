"""Module for fixtures and configurations for tests."""

import pytest


@pytest.fixture
def sample_data():
    """Fixture to provide sample data for tests."""
    return [10, 20, 30, 40, 50]
