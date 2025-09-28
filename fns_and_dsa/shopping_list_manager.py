def display_menu():
    """Displays the main menu options to the user."""
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """Main function to run the shopping list manager loop."""
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Add an item
            item = input("Enter the item to add: ").strip()
            if item: # Ensure the item name is not empty
                shopping_list.append(item)
                print(f"'{item}' added to the list.")
            else:
                print("Item name cannot be empty.")
        elif choice == '2':
            # Remove an item
            if not shopping_list:
                print("The list is empty. Nothing to remove.")
                continue

            item_to_remove = input("Enter the item to remove: ").strip()
            try:
                shopping_list.remove(item_to_remove)
                print(f"'{item_to_remove}' removed from the list.")
            except ValueError:
                print(f"Error: '{item_to_remove}' not found in the list.")
        elif choice == '3':
            # Display the shopping list
            print("\n--- Shopping List ---")
            if not shopping_list:
                print("The list is empty.")
            else:
                for index, item in enumerate(shopping_list, 1):
                    print(f"{index}. {item}")
            print("---------------------")
        elif choice == '4':
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()