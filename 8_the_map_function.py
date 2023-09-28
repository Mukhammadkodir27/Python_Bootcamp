# ---------- The Map Function ----------

# map functions take 2 paramteres, first one is function and the second one is iterable 

# Iterable 
numbers = [1, 2, 3, 4, 5]

# Function 
def calculate_square(n):
  return n * n

results = map(calculate_square, numbers)
results_in_list = list(results)
print(results_in_list)

# or it could be done like this
print(tuple(results))


# when there are more than one iterable passed to map function using lambda keyword, then it will be executed in the amount of time regarding the smallest iterable
# imagine you have 2 iterables
# nums1 = [1, 2, 3, 4, 5]
# nums2 = [1, 2]
result2 = map(lambda n1, n2: n1 + n2, nums1, nums2) 
# this time map function will be executed 2 times only, as the second iterable named nums2 consists of 2 elements only.
