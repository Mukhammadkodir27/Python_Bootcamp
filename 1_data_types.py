# ------------- Data Types --------------

'''
--Data Type--              --Class--        --Value--
integers                   -> int           -> 45
floating point numbers     -> float         -> 4.5
booleans                   -> bool          -> True/False
strings                    -> str           -> "Hello My Dear"
list                       -> list          -> [1, 2, 3, 4]
dictionary                 -> dict          -> {"user_name", "awesome50", "user_id": 56}
tuple                      -> tuple         -> (10, 20, 30)
set                        -> set           -> {"cat", 99}
'''

# Integer
age = 38
print(age)
print(type(age))

# Floats
grade = 5.0
print(grade)
print(type(grade))

# Booleans
alarm = True
offline = False
print(alarm, offline)
print(type(alarm))
print(type(offline))

# Strings
name = "name"
print(name)
print(type(name))


# -------------- Data Types 2 --------------

# ----------- List ---------------
# Ordered sequence of items, mostly used data type, very flexible,
# every item in a list does not need to be of the same type
numbers = [1, 2, 3, 3.7, 5.4]
print(numbers)
print(type(numbers))

# there can be a list inside of a list
mixed = [1, 2, 3, True, "kadir", [1, 2, 3, 4], False]
print(mixed)
print(type(mixed))


# ------------ Dictionary ---------------
# Unordered, a collection of key value pairs
user_info = {"user_name": "awesome50", "user_id": 56}
print(user_info)
print(type(user_info))


# ------------ Tuple -------------
# Ordered
mixed_tuple = (1, 2, 3, True, "kadir", [1, 2, 3, 4], False)
print(mixed_tuple)
print(type(mixed_tuple))


# -------------- Set --------------
# Unordered, when you print, output will not be in the same order as it is written
mixed_set = {1, 2, 3.2, 5.4, True, "Python Programming", 101}
print(mixed_set)
print(type(mixed_set))
