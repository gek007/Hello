import sqlite3

def convert_f_to_c(fahrenheit: float) -> float | None:
    """Convert Fahrenheit to Celsius with error handling. Returns None if input type is invalid."""
    try:
        return (fahrenheit - 32) * 5.0 / 9.0
    except TypeError as e:
        print(f"Error: Invalid input type. {e}")
        return None


def convert_c_to_f(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9.0 / 5.0) + 32.0


def open_database_connection(db_path: str) -> sqlite3.Connection | None:
    """Open a connection to the SQLite database."""
    try:
        connection = sqlite3.connect(db_path)
        print("Database connection opened successfully.")
        return connection
    except sqlite3.Error as e:
        print(f"An error occurred while connecting to the database: {e}")
        return None


def convert_temperature(temp: float, scale: str) -> tuple[float, str]:
    """
    Convert temperature between Celsius and Fahrenheit.

    Returns a tuple of (converted_value, new_scale).
    Raises ValueError for invalid scale and TypeError for invalid temperature.
    """
    s = scale.upper()
    if s == "C":
        return convert_c_to_f(temp), "F"
    elif s == "F":
        result = convert_f_to_c(temp)
        if result is None:
            raise TypeError("temperature must be a number")
        return result, "C"
    else:
        raise ValueError("scale must be 'C' or 'F'")


def safe_convert_temperature(temp: float, scale: str) -> tuple[float | None, str | None]:
    """
    Safely convert temperature between Celsius and Fahrenheit.

    Returns a tuple of (converted_value, new_scale) or (None, None) on error.
    """
    try:
        return convert_temperature(temp, scale)
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
        return None, None


if __name__ == "__main__":
    print(f"100 F -> {convert_f_to_c(100):.2f} C")
    v, sc = convert_temperature(0, "C")
    print(f"0 C -> {v:.2f} {sc}")

    