"""Module for calculate mean of list with sphinx documentation"""

import statistics


def calculate_mean(data: list[float | int]) -> dict[str, float]:
    """Function to calculate the mean of a list of numbers.

    Args:
        data (list[float  |  int]): List of numbers to calculate the mean.

    Raises:
        FileNotFoundError: If the data list is empty.

    Returns:
        float: The mean of the list of numbers.
    """

    if not data:
        raise FileNotFoundError("The data doesn't exist")
    return {"mean of data": round(statistics.mean(data), 2)}
