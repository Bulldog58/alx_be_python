# Prompt the user for their current age and convert the input to an integer
# The input() function returns a string, so we use int() to cast it to an integer
current_age = int(input("How old are you? "))

# Calculate the age in 2050, assuming the current year is 2023
# The difference in years is 2050 - 2023 = 27
future_age = current_age + 27

# Print the calculated age in the specified format
print(f"In 2050, you will be {future_age} years old.")
