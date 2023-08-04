# ---------- Non-keyword Arguments ----------

# Non-keyword Arguments are used whenever we don't know how many arguments will be given
# For example our function might accept only 2 parameters but we give 5 args when we call the function
# This is when we need Non-keyword Arguments

def sum(x, y):
    return x + y

# Example


def num(*numbers):
    return numbers


print(num(10, 21, 15, 24, 55))   # you are going to get a Tuple


def subtract(*nums):
    number = 100
    for x in nums:
        number = number - x
    return number

print(subtract(20, 30, 14, 5))
# when we are calling the function we can have as many args as we need, * is used before variable
