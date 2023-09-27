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
