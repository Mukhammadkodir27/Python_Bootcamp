# ---------- Function Types ----------

# 1 - Functions that perform a task          
# 2 - Functions that calculate and return a value

# Example 6
# This function returns a value
def facebook(name, status):
    return f"{name} is {status}"


user1_status = facebook("Tom", "offline")
user2_status = facebook("Tiffany", "online")

print(user1_status)
print(user2_status)

# Keyword Arguments


def multiply(number, by):
    return number * by

# print(multiply(20.1, 2.23))
# result = multiply(15, 4)
# print(result)
# instead of just simply writing(12, 23) in more complex functions, you can use keyword arguments, for functions with more than 4 or 7 arguments
# it is good to use them because you will not get confused which value goes to which argument


result = multiply(number=65, by=12)
print(result)
print(multiply(number=123, by=2))
# these are called keyword arguments
