# mean_calculation
This is a project to calculate mean value of list
<<<<<<< HEAD

# Calculation_Mean

This project allow to calculate mean of number list, save the result value in JSON file and generate a documentation

## Project structure

- `main.py` : Entry point of program, orchestrates the creation of data, averaging and saving result.
- `src/` : Contains the main modules:
  - [`src/mean_calculation.py`](src/mean_calculation.py) : Function [`calculate_mean`](src/mean_calculation.py) for calculate the mean.
  - [`src/data_creator.py`](src/data_creator.py) : Function [`create_data`](src/data_creator.py) for create or import data.
  - [`src/saver.py`](src/saver.py) : Function [`save_results_to_json`](src/saver.py) for save the result.
- `utils/logger.py` : Logging configuration.
- `tests/` : Unit tests with pytest.
- `docs/` : Sphinx documentation.

## Installation

```sh
pip install -r requirements.txt
```

## Utilisation

Launch the main program :

```sh
python3 main.py
```

You can choice input the data manually or import from file. The result will be saved in `results.json`.

## Tests

For executinf tests:

```sh
pytest
```

## Documentation

For generate the documentation HTML with Sphinx :
```sh
cd docs
make html
```
The generate documentation is in `docs/_build/html/`.

## Author

Admin

## Licence

MIT
=======
>>>>>>> 40c3eefe024505d6fbff968548e8d6c7b3b5da93
