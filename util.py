import sqlite3

def convert_f_to_c(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius with error handling."""
    try:
        return (fahrenheit - 32) * 5.0 / 9.0
    except TypeError as e:
        print(f"Error: Invalid input type. {e}")
        return None


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

def safe_convert_temperature(temp: float, scale: str) -> tuple[float, str]:
    """
    Safely convert temperature between Celsius and Fahrenheit.

    Returns a tuple of (converted_value, new_scale) or raises an error.
    """
    try:
        return convert_temperature(temp, scale)
    except ValueError as e:
        print(f"Error: {e}")
        return None, None
       

if __name__ == "__main__":
    print(f"100 F -> {convert_f_to_c(100):.2f} C")
    v, sc = convert_temperature(0, "C")
    print(f"0 C -> {v:.2f} {sc}")
