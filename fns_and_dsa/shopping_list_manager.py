def display_menu():
    """Prints the main menu options for the Shopping List Manager."""
    print("\n--- Shopping List Manager ---")
    print("1. Add Item ➕")
    print("2. Remove Item ➖")
    print("3. View List 👀")
    print("4. Exit 👋")
    print("-----------------------------")

def main():
    """
    The main function that runs the interactive shopping list management loop.
    It uses a Python list to store all shopping items.
    """
    # Core functionality: Initialize the shopping list as an empty list
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # 1. Add Item
            item_name = input("Enter the item to add: ").strip().capitalize()
            if item_name:
                # Use the list's append method to add an item
                shopping_list.append(item_name)
                print(f"'{item_name}' added to the list. ✅")
            else:
                print("Item name cannot be empty.")
                
        elif choice == '2':
            # 2. Remove Item
            if not shopping_list:
                print("The shopping list is empty. Nothing to remove.")
                continue

            item_to_remove = input("Enter the item to remove: ").strip().capitalize()
            
            try:
                # Use the list's remove method to delete the item by value
                shopping_list.remove(item_to_remove)
                print(f"'{item_to_remove}' removed from the list. 🗑️")
            except ValueError:
                # Handle case where the item is not found
                print(f"Error: '{item_to_remove}' was not found in the list. 🧐")
                
        elif choice == '3':
            # 3. View List
            if shopping_list:
                print("\n🛒 Your Current Shopping List:")
                # Use enumerate to display items with a numbered index
                for index, item in enumerate(shopping_list, 1):
                    print(f"{index}. {item}")
            else:
                print("\nYour shopping list is empty! Add some essentials. 😊")

        elif choice == '4':
            # 4. Exit
            print("\nThank you for using the Shopping List Manager. Goodbye! 👋")
            break
            
        else:
            # Handle invalid menu choices gracefully
            print("\n❌ Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()