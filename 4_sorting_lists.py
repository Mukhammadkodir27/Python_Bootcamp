# ---------- Sorting Lists ----------

numbers = [1, 5, 32, 124, 70, 854, 2356, 6589, 62, 8, 19, 999, 321]

# Example ->>> sort()

numbers.sort() # ascending order
numbers.sort(reverse=True) # descending order
# print(numbers)

# Example ->>> sorted()
# it will not modify original list but return a new list

print(sorted(numbers))
print(sorted(numbers, reverse=True))


# Example sort complex data

products = [("Cup", 5),
            ("T-Shirt", 19),
            ("Hat", 29),
            ("Watch", 49),
            ("UV Lamp", 27),
            ("Mug", 7),
            ]

# products.sort()
# print(products)


def sort_products(product):
    return product[1]


products.sort(key=sort_products)
print(products)
