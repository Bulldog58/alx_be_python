from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in 'YYYY-MM-DD HH:MM:SS' format.
    """
    # Part 1: Display the Current Date and Time
    current_date = datetime.now()
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")
    return current_date

def calculate_future_date(current_date):
    """
    Calculates and displays a future date based on user input.

    Parameters:
    - current_date (datetime): The starting datetime object.
    """
    # Part 2: Calculate a Future Date
    while True:
        try:
            days_to_add = int(input("Enter the number of days to add to the current date: "))
            if days_to_add < 0:
                 print("Please enter a non-negative number of days.")
                 continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    future_date = current_date + timedelta(days=days_to_add)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    return future_date

if __name__ == "__main__":
    # The main execution flow
    current_dt = display_current_datetime()
    calculate_future_date(current_dt)