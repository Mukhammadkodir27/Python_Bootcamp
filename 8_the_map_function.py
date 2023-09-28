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

