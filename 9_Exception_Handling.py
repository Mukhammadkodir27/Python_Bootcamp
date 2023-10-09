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
