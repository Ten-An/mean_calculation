"""Module for saving data analysis results to a JSON file."""

import json


def save_results_to_json(results: dict, filename: str) -> None:
    """Function to save results to a JSON file.

    Args:
        results (dict): The results to save.
        filename (str): The name of the file to save the results to.

    Raises:
        IOError: If there is an error writing to the file.
    """
    try:
        with open(filename, "w", encoding="utf-8") as json_file:
            json.dump(results, json_file, indent=4)
    except IOError as e:
        raise IOError(f"Error writing to file {filename}: {e}")
