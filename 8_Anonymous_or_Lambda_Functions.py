# ---------- Anonymous or Lambda Functions ----------

# Iterators can be iterated only once

products = [
    ("Item1", 10),
    ("Item2", 12),
    ("Item3", 3),
    ("Item4", 5),
    ("Item5", 16),
    ("Item6", 4)
]

products.sort(key=lambda product: product[1])   # once we are done with this, it will go to garbage, so garbage collected, can't use second time
print(products)

print("")

products.sort(key=lambda items: items[0])
print(products)


my_list = [1, 5, 4, 6, 8, 11, 3, 12, 34, 55]

# this new list will take only even numbers
new_list = filter(lambda x: (x % 2 == 0), my_list)

for num in new_list:
    print(num)

# it won't assign a list to the new list as it can be used once only (iterator)
even_nums = list(new_list)
print(even_nums)


'''
products = [("Apple", 3), ("Banana", 2), ("Cherry", 5), ("Date", 1)]

# Sort products based on the second element of each tuple (item[1])
products.sort(key=lambda item: item[1])

print(products)
'''
