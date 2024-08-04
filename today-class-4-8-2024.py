# def display_nums(first_num, second_num,*opt_nums):
        
#     print(first_num)
#     print(second_num)
#     print(opt_nums)

# display_nums(100, 200, 300, 400, 500)

# y = 1

# def whatever():
# #  y = 2
#  print(y)
#  y = 1
#  print(y)


# whatever()

# global course
# course = "Python"

# def display_name(full_name):
#     print(f"Student name is {full_name} stuyding in {course}")
# display_name("Mr. Muhammad Ahsan Shaikh" )



# global tax
# tax = 0.18

# def totalTaxes(amount):
#     return amount * tax


# def today_sales(carsales = 10 , bikesales = 50, crusesales = 2):

#     total = carsales + bikesales + crusesales

#     taxes = totalTaxes(total)

#     return total,taxes

# todayRecords = today_sales()

# print(f"total sales is {todayRecords[0]} and taxes is {todayRecords[1]}")















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