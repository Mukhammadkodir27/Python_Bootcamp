# ---------- Introduction to Tuples ----------

# It is similar to Lists but ...
# we cannot change the elements of tuples once they are assigned

first_tuple = ()
print(first_tuple)
print(type(first_tuple))

num = (1, 2, 3, 4)
print(num)
print(type(num))

# it can have mixed items of mixed data types, in many amounts
mixed_tuple = (1, "Bear", True)
print(mixed_tuple)

# mixed data types
mixed = ({"Name": "John", "Age": 18, "Job": "Developer"}, [
         "Dev1", "Dev2", 1, 4], (1.2, 1.3, 2, 3), {"Europe", 19})
print(mixed)

print("")
print("")
print("")

# ----- Tuple Packing & Unpacking -----

# Example ---> Tuple Packing
to_do = "buy coffee", "read a book", "finish homework"  # it is a tuple
print(to_do)

# Example ---> Tuple Unpacking
to_do1, to_do2, to_do3 = to_do
print(to_do1)
print(to_do2)
print(to_do3)

# Example ---> Tuple with one element
name1 = ("Tommy")  # it is a string
print(name1)
print(type(name1))
name = ("Tommy",)  # it is a tuple as there is a comma after "Value"
print(name)
print(type(name))

print("")
print("")
print("")

# ----- Accessing Tuple Elements -----

# Example ---> Indexing []
mixed2 = (False, 3.14159, "Python", ["Web", "Mobile"], 45)
print(mixed2)
print(mixed2[0])
print(mixed2[1])

for i in mixed2:
    print(i)


# Example ---> Negative Indexing
print(mixed2[-1])   # 45 because it starts from right-hand side till left side
print(mixed2[-2])  # ["Web", "Mobile"]
print(mixed2[-5])  # False


# Example ---> Slicing
print(mixed2[0:2])
print(mixed2[2:4])
print(mixed2[:4])
print(mixed[3:])
print(mixed[:])
print(mixed[:-1])  # from -5, -4, -3, -2 till -1
print(mixed[:-3])  # from -5, -4 till -3


# ----- Changing Tuples -----

# Example ---> Chaning Tuple Elements (Lists)
numbers = (4, 2, 3, [5, 6, 7, 8])
# numbers[1] = 10 #TypeError

print(numbers)
numbers[3][2] = 111
print(numbers)
print(numbers[3])

# Example ---> Reassignment of a tuple
# we can reassign a tuple with different values
numbers = (222, 333, 111)
print(numbers)

# Example ---> repeating a tuple items
print(("Movie",) * 5)

# Example ---> tuple concatenation
letters = ("p", "y", "t", "h", "o", "n")

nums_and_letters = numbers + letters
print(nums_and_letters)


# we cannot delete individual items in tuple
# but we can delete a tuple entirely
del letters
del numbers

# print(letters) #NameError as letters (tuple) is not defined


# ----- Tuple Methods -----
# Example ---> count() method
colors = ("green", "blue", "violet", "lawngreen", "green")
print(colors.count("green"))
print(colors.count("black"))

# Example ---> index()
print(colors.index("blue"))
print(colors.index("green"))
