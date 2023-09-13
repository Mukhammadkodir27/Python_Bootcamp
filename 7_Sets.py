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


# ----- Modifying Lists -----

# Example ---> Creating a set
mixed_info = {"Python", "Dog"}

# Example ---> Indexing is not allowed
# print(mixed_info[0]) #TypeError

# Example ---> add()
mixed_info.add(31)
mixed_info.add("C++")
# print(mixed_info)


# Example ---> update()  to add multiple items at a time
mixed_info.update([12, "Jar", "Sand", 23])
print(mixed_info)

# Example ---> update()
# duplicates are removed as it is becoming a set
mixed_info.update(["Bird", "Island"], ("Cat", "Island"), {"Rabbit", "Island"})
print(mixed_info)


# ---------- Removing Set Items ----------

# Example ---> discard()
numbers = {1, 2, 3, 4, 5, 6}
print(numbers)
# cool thing about discard is that if item does not exist it won't give an error
numbers.discard(4)
print(numbers)

# Example ---> discard() -> item which does not exist
numbers.discard(11)
print(numbers)


# Example ---> remove()
numbers2 = {1, 2, 3, 4, 5, 6}
print(numbers2)

numbers2.remove(3)
print(numbers2)

# Example ---> remove() -> item which does not exist
# numbers.remove(11) # KeyError as item does not exist


# Example ---> pop()
# it removes arbitrary item as there is no indexing in set.
# it cannot delete the last item as there is no indexing

numbers2.pop()
print(numbers2)
numbers2.pop()
print(numbers2)
# numbers2.pop()
# print(numbers2)


# Example ---> clear()
numbers.clear()
print(numbers)  # it prints set() because it cannot print {}, it is for dict
numbers2.clear()
print(numbers2)  # this method clears the entire set
