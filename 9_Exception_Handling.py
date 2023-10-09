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


# Example

random_list = ["a", 0, 2]

for entry in random_list:
    try:
        print("The entry is", entry)
        r = 1 / int(entry)
        break
    except:
        print("oops", sys.exc_info()[0], "occured!")

        print("Next Entry")
        print()

print()
print("The reciprocal of", entry, "is", r)


# Example

for a in random_list:
    try:
        print("The entry is", a)
        r = 1 / int(a)
        break
    except Exception as exp_error:
        print("oops", exp_error.__class__, "occured!")

        print("Next Entry")
        print()


print()
print("The reciprocal of", a, "is", r)



# ----------------------------------------------------------------------------------------------

# --------- Exception Handling 2 ----------

# Example
# try:
#     age = int(input("Age: "))
#     result = 10 / age
# except ValueError:
#     print("Please enter a valid value")
# else:
#     print("No Errors Here")


# Example ->>> ZeroDivisionError
# try:
#     age = int(input("Age: "))
#     result = 10 / age
# except ValueError:
#     print("Please enter a valid value")
# except ZeroDivisionError:
#     print("age cannot be zero!")
# else:
#     print("No Errors Here")

# Example ->>> creating a tuple of errors
# try:
#     age = int(input("Age: "))
#     result = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("Please enter a valid value")
# except ZeroDivisionError:
#     print("Age cannot be zero!")
# else:
#     print("No Errors Here")


# Example ->>> a tuple of errors
try:
    age = int(input("Age: "))
    result = 10 / age
except (ValueError, ZeroDivisionError):
    print("Please enter a valid value")
else:
    print("No Errors Here")

# --------------------------------------------------------------------------------------------------------------------------

# ---------- Exception Handling 3 ----------

# finally clause --->>> runs no matter there is exception or there is no exception
# it always runs


# Example --- try... except... else... finally...

# Example 1
# try:
#     note = open("someFile.txt")
#     age = int(input("Enter age: "))
#     result = 10 / age
#     note.close()  # this file wont be closed if there is exception in previous lines
# except (ValueError, ZeroDivisionError):
#     print("Please enter a valid value")
# else:
#     print("No Exceptions here")


# Solution 1
# try:
#     note = open("someFile.txt")
#     age = int(input("Enter age: "))
#     result = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("Please enter a valid value")
#     note.close()  # this file wont be closed if there is no exception
# else:
#     print("No Exceptions here")


# Solution 2
# try:
#     note = open("someFile.txt")
#     age = int(input("Enter age: "))
#     result = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("Please enter a valid value")
#     note.close()  # this file wont be closed if there is no exception
# else:
#     print("No Exceptions here")
#     note.close()  # we are making duplicates of the same code so not good way to solve the issue


# Solution 3 ->>> finally clause
try:
    note = open("someFile.txt")
    age = int(input("Enter age: "))
    result = 10 / age
except (ValueError, ZeroDivisionError):
    print("Please enter a valid value")
else:
    print("There are no exceptions")
finally:  # this will be executed no matter what (yes or no exceptions)
    note.close()


# ------------------------------------------------------------------------------------------------


# ---------- With Statement ----------

# the good thing about With Statement is that we can use FileNotFoundError to check the files opened
# if the files does exist or not, or if there are any issues with the file, we can check it via using With Statement for files.

# Also it automatically closes the opened file.
# we don't need to call the close method for opened file

try:
    with open("someFile.txt") as note, open("anotherFile.txt") as my_note:
        print("note opened")

    age = int(input("Age: "))
    result = 10 / age
except (ValueError, ZeroDivisionError):
    print("Please enter a valid value")
except FileNotFoundError:
    print("Check the file!")
else:
    print("No Exceptions Found!")


# Example
# try:
#     with open("someFile.txt") as note:
#         print("note opened")

#     age = int(input("Age: "))
#     result = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("Please enter a valid value")
# except FileNotFoundError:
#     print("Check the file!")
# else:
#     print("No Exceptions Found!")


# -------------------------------------------------------------------------------------------------


# ---------- Raising Exceptions ----------

def calculate_age(age):
    if age <= 0:
        raise ValueError("age cannot be zero or less")

    return 10 / age


try:
    # calculate_age(0)
    calculate_age(-5)
    # calculate_age(2)
except ValueError as error:
    print(error)
else:
    print("No Exceptions")

