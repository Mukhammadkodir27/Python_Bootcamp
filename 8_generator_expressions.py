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
