# Scenario 1: Grocery Shopping List
# You are creating a program to manage a grocery shopping list. Users should be able to add items,
# remove items, and display the current list.



shopping_list = ["shoes", "tie", "coat"]

def add_item(item):
    shopping_list.append(item)
    print(f"{item} has been added to the list.")

def remove_item(item):
    shopping_list.remove(item)
    print(f"{item} has been removed from the list.")

def display_list():
    print("Your shopping list:")
    for item in shopping_list:
        print(item)


def run_program():
    print(f"What would you like to do ? \n 1. Add item \n 2. Remove item \n 3. Display list")
    choice = input("Enter your choice (1-3): ")
    if choice == "1":
        item = input("Enter the item you want to add: ")
        add_item(item)
    elif choice == "2":
        item = input("Enter the item you want to remove: ")
        remove_item(item)
    elif choice == "3":
        display_list()
    else:
        print("Invalid choice. Please try again.")


run_program()