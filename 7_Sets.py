# ---------- Introduction to Sets ----------
# sets are mutable
# we can perform mathematical set of operations
# sets are unordered
# it removes duplicates, so it is good to take unique numbers

# Example 1
first_set = {21, 32, 54, 665, 999}
# print(first_set)

scores = {1, 2, 3, 1, 1, 2, 1, 3, 1, 2}
unique_numbers = scores
print(unique_numbers)

# Example 2
mixed = {5.19, "Set", ("London", "Paris")}
# print(mixed)

# Example 3 ---> Creating a set from a tuple
colors = set(("blue", "red", "green", "blue"))  # it removes duplicates
print(colors)

# Example 4 ---> Creating a set from a list
colors2 = set(["red", "blue", "red", "yellow", "red"])
print(colors2)

# Example 5 ---> Creating a set from a dictionary
colors3 = set({
    "blue": 1,
    "red": 2,
    "green": 3
})
print(colors3)

# Example 6 ---> a set cannot have a mutable data type as an item
# colors4 = {"red", "blue", [1, 2, 3]}  # TypeError

# Example 7 ---> creating an empty set
names = {}  # empty dict
print(names)
print(type(names))  # it is a dict as it is denoting a {}

# how can we create an empty set?
numbers = set()
print(numbers)
print(type(numbers))

