# match_case_calculator.py

# Prompt for user input
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose the operation (+, -, *, /): ")

    result = None
    match operation:
        case '+':
            result = num1 + num2
        case '-':
            result = num1 - num2
        case '*':
            result = num1 * num2
        case '/':
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                result = num1 / num2
        case _:
            print("Invalid operation chosen.")


    if result is not None:
        print(f"The result is {result}.")

except ValueError:
    print("Invalid input. Please enter numbers.")