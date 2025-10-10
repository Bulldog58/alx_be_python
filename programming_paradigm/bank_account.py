class BankAccount:
    """
    A class to represent a simple bank account with deposit, 
    withdraw, and balance display functionalities.
    """

    def __init__(self, initial_balance=0.0):
        """
        Initializes the BankAccount with a specified or default balance.
        """
        # Encapsulated attribute to store the balance
        self._account_balance = initial_balance

    def deposit(self, amount):
        """
        Adds the specified amount to the account balance.
        """
        if amount > 0:
            self._account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Deducts the amount from the balance if funds are sufficient.
        
        Returns:
            bool: True if withdrawal was successful, False otherwise.
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
            
        if self._account_balance >= amount:
            self._account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """
        Prints the current balance in a user-friendly format.
        """
        # Formatted output to two decimal places
        print(f"Current Balance: ${self._account_balance:.2f}")

# Note on Encapsulation: The use of a single leading underscore 
# in _account_balance is a Python convention indicating that 
# the attribute is intended for internal use and should not 
# be directly modified from outside the class.