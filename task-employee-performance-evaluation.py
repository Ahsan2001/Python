# Scenario 01: Employee Performance Evaluation


# In a large corporation, the HR department needs
# to evaluate the performance of employees based on
# their sales records and customer satisfaction ratings.
# They want to identify the top-performing employees
# based on a weighted score that combined 
# sales performance and customer satisfaction.


# Hint: Use List comprehension & Lambda Functions


# Sample data: List of tuples containing 

# employee names, sales figures, and customer  satisfaction ratings

employeesData =  [
  ("John", 50000, 4.5),
  ("Alice", 60000, 4.7),
  ("Bob", 45000, 4.2),
  ("Emma", 55000, 4.6),
  ("James", 48000, 4.4)
]



# Define weights for sales performance 
# and customer satisfaction ratings
sales_weight = 0.6
satisfaction_weight = 0.4





employees = [
    ("John", 50000, 4.5),
    ("Alice", 60000, 4.7),
    ("Bob", 45000, 4.2),
    ("Emma", 55000, 4.6),
    ("James", 48000, 4.4)
]

def evaluate_performance(data):
    performance_list = []
    
    for x in data:  
        calculating = (x[1] * 0.6 + x[2] * 0.4)
        performance_list.append((x[0], calculating))
    
  
    performance_list.sort(key=lambda y: y[1], reverse=True)
    
    for name, performance in performance_list:
        print(f"Performance of {name} is {performance}")

evaluate_performance(employees)

