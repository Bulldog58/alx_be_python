import sys
# Import the BankAccount class from the bank_account.py file
try:
    from bank_account import BankAccount
except ImportError:
    print("Error: Could not find bank_account.py. Make sure it is in the same directory.")
    sys.exit(1)

def main():
    # Instantiate the BankAccount with an initial balance of $100
    account = BankAccount(100.00) 
    
    # Check for minimum arguments
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Parse the argument (e.g., "deposit:50" or "display")
    try:
        # Split the argument by ':'
        command_parts = sys.argv[1].split(':')
        command = command_parts[0].lower()
        
        # Check if an amount was provided, otherwise default to None
        amount = float(command_parts[1]) if len(command_parts) > 1 else None

    except ValueError:
        print("Invalid amount format. Amount must be a number.")
        sys.exit(1)
    except IndexError:
        # This handles cases like 'deposit:' with no amount
        command = sys.argv[1].lower()
        amount = None
        
    # Process the command
    if command == "deposit" and amount is not None:
        account.deposit(amount)
        # Display balance after deposit for confirmation
        account.display_balance() 
        
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}")
            # Display balance after successful withdrawal
            account.display_balance() 
        else:
            print("Insufficient funds.")
            account.display_balance() 

    elif command == "display" and amount is None:
        account.display_balance()
        
    else:
        # Handles cases like invalid command or missing amount for deposit/withdraw
        print("Invalid command or missing amount for transaction.")

if __name__ == "__main__":
    main()