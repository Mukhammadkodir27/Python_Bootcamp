# --------------- Conditional Statements -----------------

"""
if (boolean expression): 
  execute the statements
     
"""

# Example ->>>>>> Check for a single condition
temperature = 35
# temperature = 19

if temperature > 30:
    print("It is a good day for walking")


# Example ->>>>>> Check for 2 conditions
if temperature > 25:
    print("Awesome!")
else:
    print("Cold!")


# Example ->>>>>> Check for multiple conditions
if temperature >= 35:
    print("Hot!")
elif temperature > 25:
    print("Awesome!")
elif temperature < 5:
    print("Cold!")
else:
    print("Wrond value!")
