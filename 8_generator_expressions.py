# ---------- Generator Expressions ----------
from sys import getsizeof
# when we are talking about big amount of numbers then it is good to use generator expressions than other data types like list
# List 
numbers_list = [x * 2 for x in range(10))
print("List Size: ", getsizeof(numbers_list)) # 800
# Generator Expressions
numbers_gen = (x * 2 for x in range(10)) 
print("GO Size: ", getsizeof(numbers_gen)) # 112

# when we talk about extremely large data, generator expressions are user-friendly. 
# if in range(100000) list reaches 812133 bytes of memory
# in (100000000) range also generator expressions remain same as 112. So less memory is used.


# List Comprehension
numbers_list = [x * 2 for x in range(10)]
numbers_list = [x * 2 for x in range(100)]
numbers_list = [x * 2 for x in range(1000)]
numbers_list = [x * 2 for x in range(10000)]

# Generator Expression Objects
# or
# Generator Objects
numbers_gen = (x * 2 for x in range(10))
numbers_gen = (x * 2 for x in range(100))
numbers_gen = (x * 2 for x in range(1000))
numbers_gen = (x * 2 for x in range(10000))

print(type(numbers_gen))
print(numbers_gen)

print("List Comprehension Expression size:", getsizeof(numbers_list)) # 85175 bytes
print("Generator Object size:", getsizeof(numbers_gen)) # 208 bytes
