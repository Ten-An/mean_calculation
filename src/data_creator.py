"""Module for create data according to manually or imported from file."""


def create_data() -> list[float | int]:
    """Function to create data.

    Returns:
        list[float | int]: List of numbers.
    """
    choice_ = (
        input(
            """
Do you want to create data (manually) or to import data from (file)? : """,
        )
        .lower()
        .strip()
    )
    if choice_ == "manually":
        data_insert = input("Enter numbers separated by space: ")
        data = [float(num) if "." in num else int(num) for num in data_insert.split()]
    elif choice_ == "file":
        filename = input("Enter the filename: ").lower().strip()
        try:
            with open(filename, "r", encoding="utf-8") as file:
                data_imported = file.read().strip().split()
                data = [float(num) if "." in num else int(num) for num in data_imported]
        except FileNotFoundError:
            raise FileNotFoundError(f"File {filename} not found.")
    else:
        print("Invalid choice.")
    return data
