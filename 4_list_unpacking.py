# ---------- List Unpacking ----------

# Example ->>> assigning list items to different variables
nums = [23, 49, 85]
num1, num2, num3 = nums
# print(num1)
# print(num2)
# print(num3)

# Example ->>> assigning list items to another list is done using *var_name
numbers = [23, 49, 85, 1, 2, 3, 4, 5]
num1, num2, *other_nums = numbers
# print(num1)
# print(num2)
# print(other_nums)
num1, *other_nums, num2 = numbers

# Example
num1, num2, *other_nums, num3, num4 = numbers
# 23   49    85, 1, 2, 3   4,    5     23, 49, 85, 1, 2, 3, 4, 5

print(num1)
print(num2)
print(num3)
print(num4)
print(other_nums)
print(numbers)
