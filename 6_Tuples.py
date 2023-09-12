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


# ----- Tuple Packing & Unpacking -----
qw
