"""Module for main orchestrating the mean calculation and saving results to a JSON file."""

from src.mean_calculation import calculate_mean
from src.saver import save_results_to_json
from src.data_creator import create_data
from utils.logger import setup_logging


def main():
    """Main function to calculate mean and save results."""
    logger = setup_logging()

    logger.info("Starting the mean calculation process.")

    data = create_data()
    logger.info("Data created: %s", data)

    try:
        results = calculate_mean(data)
        save_results_to_json(results, "results.json")
        logger.info("Results saved to results.json")
    except Exception as e:
        logger.error("An error occurred: %s", {e})


if __name__ == "__main__":
    main()
