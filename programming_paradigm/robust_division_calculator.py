# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Performs division robustly, handling ZeroDivisionError and ValueError.

    Args:
        numerator (str): The numerator passed as a string argument.
        denominator (str): The denominator passed as a string argument.

    Returns:
        str: The result of the division or an appropriate error message.
    """
    try:
        # Attempt to convert both string inputs to float
        num = float(numerator)
        den = float(denominator)

        try:
            # Attempt to perform the division
            result = num / den
            return f"The result of the division is {result}"

        except ZeroDivisionError:
            # Handle the specific case of division by zero
            return "Error: Cannot divide by zero."

    except ValueError:
        # Handle the case where the string inputs cannot be converted to float
        return "Error: Please enter numeric values only."