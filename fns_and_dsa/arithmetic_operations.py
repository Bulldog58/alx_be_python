def perform_operation(num1, num2, operation):
    """
    Performs a basic arithmetic operation between two numbers.

    Parameters:
    - num1 (float): The first number.
    - num2 (float): The second number.
    - operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide').

    Returns:
    - float: The result of the operation.
    - str: A specific message if division by zero is attempted.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            # Handle division by zero
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        # Handle unrecognized operation
        return "Error: Invalid operation specified."

# The provided main.py will import and use this function.