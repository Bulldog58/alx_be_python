# Get user input for the size of the pattern
try:
    size = int(input("Enter the size of the pattern: "))
    
    # Use a while loop for the rows
    row = 0
    while row < size:
        # Use a for loop for the columns (to print the asterisks)
        for _ in range(size):
            print("*", end="")
        
        # Print a newline character to move to the next row
        print()
        
        # Increment the row counter
        row += 1
        
except ValueError:
    print("Invalid input. Please enter a positive integer.")
