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

products.sort(key=lambda product: product[1])
print(products)

print("")

products.sort(key=lambda items: items[0])
print(products)




''''
products = [("Apple", 3), ("Banana", 2), ("Cherry", 5), ("Date", 1)]

# Sort products based on the second element of each tuple (item[1])
products.sort(key=lambda item: item[1])

print(products)
'''
