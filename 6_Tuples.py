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
