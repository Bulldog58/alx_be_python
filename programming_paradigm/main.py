# main.py

import sys
# Import the safe_divide function from the calculator script
try:
    from robust_division_calculator import safe_divide
except ImportError:
    print("Error: Could not find robust_division_calculator.py. Make sure it is in the same directory.")
    sys.exit(1)

def main():
    """
    Interfaces with the user through command line arguments to perform safe division.
    """
    
    # Check for correct number of arguments (script name + numerator + denominator)
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    # Arguments are passed as strings via sys.argv
    numerator = sys.argv[1]
    denominator = sys.argv[2]

    # Call the robust function and print the returned result or error message
    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()