# Get user input for the number to generate the table for
try:
    number = int(input("Enter a number to see its multiplication table: "))

    # Use a for loop to iterate from 1 to 10 and print the multiplication table
    for i in range(1, 11):
        product = number * i
        print(f"{number} * {i} = {product}")
        
except ValueError:
    print("Invalid input. Please enter a valid integer.")
