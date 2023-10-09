# ---------- Exception Handling ----------

import sys

# try except

try:
    pass
except:
    pass


# Example

try:
    age = int(input("Enter your age: "))
except:
    print("Please, provide a valid value!")


# Example

try:
    age2 = int(input("Enter your age 2: "))
except ValueError:
    print("Please, provide a valid value!")
else:
    print("No Exceptions here")


# Example

try:
    age3 = int(input("Enter your age 3:"))
except ValueError as exp_error:
    print("Please, provide a valid value!")
    print(exp_error)
    print(type(exp_error))
else:
    print("No Exceptions here!")
