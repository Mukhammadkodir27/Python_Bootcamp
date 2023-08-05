# ---------- The List Method ----------

# Do not confuse list() method with list methods
number = [1, 2, 3, 4]  # 1, 2, 3, 4
nums = [range(90)]  # [range(0, 90)]   # 1 item

numbers = list(range(100))  # [0, 1, 2, ... 97, 98, 99]   # 100 items
print(numbers)

# we can create a list of string because strings are iterable
random_name = list("Izabella")   # 'I', 'z', 'a', 'b', 'e', 'l', 'l', 'a'
print(random_name)
print(len(random_name))  # 8 items

ran_name = ["Izabella"]  # it could count it as one item
print(len(ran_name))     # 1 item
# names = list("Karim", 1, 2, 3, "Kadir") - WRONG!
