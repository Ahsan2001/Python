# Scenario: Student Grade Management System
# You are tasked with creating a basic Student Grade Management System for a small class. The system should allow you to:

# Add new students to the system.
# Record grades for each student in different subjects.
# Calculate the average grade for each student.
# Display the list of all students with their grades and averages.
# Find and display the student with the highest average grade.

# Sample Data Set:
sample_students = {
    "Alice": {
        "Math": 88,
        "Science": 92,
        "English": 85
    },
    "Bob": {
        "Math": 75,
        "Science": 80,
        "History": 78
    },
    "Charlie": {
        "Math": 90,
        "Science": 85,
        "English": 87,
        "History": 80
    },
    "David": {
        "Math": 70,
        "Science": 72,
        "English": 75
    },
    "Eve": {
        "Math": 95,
        "Science": 90,
        "History": 85
    }
}





def add_new_student(student, name):
     student[name] = {}
     print(f"New student edit successfully")

add_new_student(sample_students, "Ahsan")


def record_grade(students, name, subject, grade):
    students[name][subject] = grade
    print(f"Recorded grade {grade} for {name} in {subject}.")

record_grade(sample_students, "Ahsan", "Python", 85)

print(sample_students)
