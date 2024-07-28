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

employees =  [
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
