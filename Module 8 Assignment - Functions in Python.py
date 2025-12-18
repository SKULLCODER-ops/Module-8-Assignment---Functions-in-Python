Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> # Module 6 Assignment - Fundamental Concepts of Python - IDLE
... # Author: Aiden
... # Purpose: Demonstrate user-defined functions in Python
... 
... # Define the function greater_than
... def greater_than(x, y):
...     # Check if x is greater than y
...     if x > y:
...         return True
...     else:
...         return False
... 
... # --- First Scenario ---
... a = 2
... b = 3
... result = greater_than(a, b)
... 
... # Print the formatted output
... print("The statement " + str(a) + " is greater than " + str(b) + " is " + str(result))
... 
... # --- Second Scenario ---
... a = 10
... b = 6
... result = greater_than(a, b)
... 
... # Print the formatted output
