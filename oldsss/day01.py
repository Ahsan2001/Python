# COMMENTS 

# This is a single line comment

'''
this is a multi
line comment
'''


# print("Hello world from python")

my_full_name = "Mr. Muhammad Ahsan"

# print(my_full_name)

my_age = 23

# print(my_age)


obtained_marks = 90
total_marks = 100
calculate_percentage = obtained_marks / total_marks * 100

# if calculate_percentage >= 80:
#     print("Grade A")
# elif calculate_percentage >= 60:
#     print("Grade B")
# elif calculate_percentage >= 50:
#     print("Grade C")
# elif calculate_percentage >= 40:
#     print("Grade D")
# else:
#     print("Grade F")


cities = ["Lahore", "Karachi", "Islamabad", "Quetta", "Peshawar"]

favourite_cities = cities[1:3]

# print(favourite_cities)

cities.append("Multan")

cities.insert(1, "Rawalpindi")

# print(cities)

favourite_cities = cities[:5]

# print(favourite_cities)



# print(cities)

del cities[0]

# print(cities)

cities.remove("Karachi")

# print(cities)




tasks = ["email Frank", "call Sarah", "meet with Zach"]
print(tasks)
a = tasks.pop(0)
tasks.append(a)


# newTask = tasks.pop(1)
# print (tasks, newTask)
print (tasks)
