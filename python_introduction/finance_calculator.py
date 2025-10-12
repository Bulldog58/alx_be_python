# finance_calculator.py

# --- Variables for constants ---
ANNUAL_INTEREST_RATE = 0.05
MONTHS_IN_YEAR = 12

# --- User Input for Financial Details ---
# Prompt the user for their monthly income.
# The input() function returns a string, so we convert it to a float for arithmetic.
monthly_income_str = input("Enter your monthly income: ")
monthly_income = float(monthly_income_str)

# Ask for their total monthly expenses.
monthly_expenses_str = input("Enter your total monthly expenses: ")
monthly_expenses = float(monthly_expenses_str)

# --- Calculate Monthly Savings ---
# Calculate the monthly savings by subtracting monthly expenses from the monthly income.
monthly_savings = monthly_income - monthly_expenses

# --- Project Annual Savings ---
# 1. Calculate the total savings without interest over one year.
annual_savings_without_interest = monthly_savings * MONTHS_IN_YEAR

# 2. Calculate the interest earned on the total annual savings.
# Simple interest = Principal * Rate
annual_interest_earned = annual_savings_without_interest * ANNUAL_INTEREST_RATE

# 3. Calculate the projected savings after one year, including the interest.
# Projected Savings = Annual Savings without Interest + Annual Interest Earned
projected_annual_savings = annual_savings_without_interest + annual_interest_earned

# The specified simplified formula for projected annual savings is:
# Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05)
# This is equivalent to the steps above.

# --- Output Results ---
# Display the user's monthly savings.
# We use f-strings and format the output to two decimal places for currency.
print(f"Your monthly savings are ${monthly_savings:.2f}.")

# Display the projected annual savings after including interest.
print(f"Projected savings after one year, with interest, is: ${projected_annual_savings:.2f}.")
  
