import sqlite3


def convert_f_to_c(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5.0 / 9.0


def open_database_connection(db_path: str):
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
    """
    s = scale.upper()
    if s == "C":
        return convert_c_to_f(temp), "F"
    elif s == "F":
        return convert_f_to_c(temp), "C"
    else:
        raise ValueError("scale must be 'C' or 'F'")


def convert_c_to_f(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32


if __name__ == "__main__":
    print(f"100 F -> {convert_f_to_c(100):.2f} C")
    v, sc = convert_temperature(0, "C")
    print(f"0 C -> {v:.2f} {sc}")
# filepath: g:\VSCode\Hello\util.py
import sqlite3


def convert_f_to_c(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5.0 / 9.0


def open_database_connection(db_path: str):
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
    """
    s = scale.upper()
    if s == "C":
        return convert_c_to_f(temp), "F"
    elif s == "F":
        return convert_f_to_c(temp), "C"
    else:
        raise ValueError("scale must be 'C' or 'F'")


def convert_c_to_f(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32


if __name__ == "__main__":
    print(f"100 F -> {convert_f_to_c(100):.2f} C")
    v, sc = convert_temperature(0, "C")
    print(f"0 C -> {v:.2f} {sc}")