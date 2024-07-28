# Enhanced Problem: User Access Logs with Detailed Analysis
# You have been given a nested dictionary where the keys are user IDs and the values are dictionaries containing login information for each user. Each inner dictionary contains the IP addresses and the number of login attempts from those IP addresses. Write a Python program to identify users who have suspicious login activities based on the following criteria:

# Any IP address that has attempted to log in more than a specified number of times (e.g., 5 times) for a given user.
# IP addresses from a known list of suspicious IPs.
# Any user who has login attempts from more than a specified number of different IP addresses (e.g., 3 different IP addresses).
# The program should use functions to modularize the code and tuples to store and print the results.

# Example Input

user_logs = {
    "user1": {
        "192.168.1.10": 6,
        "203.0.113.8": 1,
        "10.0.0.5": 2
    },
    "user2": {
        "198.51.100.2": 1,
        "192.0.2.1": 4,
        "203.0.113.8": 5
    },
    "user3": {
        "192.168.1.15": 2,
        "192.168.1.20": 3,
        "192.168.1.25": 1,
        "203.0.113.8": 2
    }
}
known_suspicious_ips = ["203.0.113.8", "198.51.100.2"]
max_attempts = 5
max_unique_ips = 3

# Expected Output

# Suspicious user activities:
('user1', '192.168.1.10', 6)
('user2', '203.0.113.8', 5)
('user2', '198.51.100.2', 'suspicious IP')
('user3', 'more than 3 unique IPs')
