# ---------- List Comprehension Part 1 ----------

# basic syntax of a List Comprehension
# [expression for item in list]

numbers = [23, 54, 67, 89, 15, 99]
fruits = ['Apple', "Orange", "Banana"]

# Example
numbers2 = [num for num in numbers]
# print(numbers) # [23, 54, 67, 89, 15, 99]


# Example
numbers2 = [num*2 for num in numbers]
# print(numbers2) # [46, 108, 134, 178, 30, 198]


# Example
numbers2 = [(num / 2) * 5 for num in numbers]
# print(numbers2)  # [57.5, 135.0, 167.5, 222.5, 37.5, 247.5]

# we can do a sort of complex arithmetic operations with LC


# Example - let's work with strings

fruits2 = [fruit.lower() for fruit in fruits]
# print(fruits2) # [apple, orange, banana]

fruits2 = [fruit.upper() for fruit in fruits]
# print(fruits2) # [APPLE, ORANGE, BANANA]


# Example
products = [("Cup", 5),
            ("T-Shirt", 19),
            ("Hat", 29),
            ("Watch", 49),
            ("UV Lamp", 27),
            ("Mug", 7),
            ]

items = [item for item in products]
# items = [item[1] for item in products]
items = [item[0] for item in products]
print(items)  # [Cup, T-Shirt, Hat, Watch, UV Lamp, Mug]
# as you can see it grabbed 0 index items from list of tuples

# or we can do even better

product_names = [item[0] for item in products]
product_prices = [item[1] for item in products]
# product_prices = [item[1] * 2 for item in products]
print(product_names)
print(product_prices)


# ---------- Part 2 ----------

products = [("Cup", 5),
            ("T-Shirt", 20),
            ("Hat", 29),
            ("Watch", 49),
            ("UV Lamp", 27),
            ("Mug", 7),
            ]

numbers = [21, 24, 56, 564, 102, 504, 79, 84]

# Example ->>> Single Condition

items = [item[1] for item in products if item[1] >= 20]
print(items)

# Example ->>> Two Conditions

modified_numbers = [num if num > 100 else num / 2 for num in numbers]
modified_numbers2 = [num if num < 100 else num / 2 for num in numbers]

print(modified_numbers)
print(modified_numbers2)

