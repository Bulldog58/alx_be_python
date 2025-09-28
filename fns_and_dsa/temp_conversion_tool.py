# Define Global Conversion Factors
# These variables are in the global scope. Functions can read them 
# without the 'global' keyword.
FAHRENHEIT_TO_CELSIUS_FACTOR = 5.0 / 9.0  # Used in formula: (Tf - 32) * (5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR = 9.0 / 5.0  # Used in formula: (Tc * 9/5) + 32

def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius.
    It accesses the global FAHRENHEIT_TO_CELSIUS_FACTOR.
    """
    # Tc = (Tf - 32) * (5/9)
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit.
    It accesses the global CELSIUS_TO_FAHRENHEIT_FACTOR.
    """
    # Tf = (Tc * 9/5) + 32
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    """
    Handles user interaction, input validation, and temperature conversion.
    """
    while True:
        try:
            # 1. Prompt for temperature and validate
            temp_input = input("Enter the temperature to convert: ")
            
            try:
                # Attempt to convert input to a floating-point number
                temperature = float(temp_input)
            except ValueError:
                # If conversion fails, raise a custom error as required
                raise ValueError("Invalid temperature. Please enter a numeric value.")
            
            # 2. Prompt for unit and normalize input
            unit_input = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
            
            if unit_input == 'F':
                # Convert F to C
                converted_temp = convert_to_celsius(temperature)
                print(f"{temperature}°F is {converted_temp}°C")
                
            elif unit_input == 'C':
                # Convert C to F
                converted_temp = convert_to_fahrenheit(temperature)
                print(f"{temperature}°C is {converted_temp}°F")
            
            else:
                # Handle invalid unit input
                print("Invalid unit. Please enter 'C' or 'F'.")
                continue # Restart the loop for unit error

            # Exit the loop after a successful conversion
            break
            
        except ValueError as e:
            # Catch the specific error raised for invalid temperature
            print(f"Error: {e}")
        except Exception as e:
            # Catch any other unexpected error
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()