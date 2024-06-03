# Dictionary Comprehensions

#! Example 1
coordinates = {}
for key in range(5):
    coordinates[key] = (key * 5) / 2

print(coordinates)

# the same here
coordinates = {key: (key * 5) / 2 for key in range(5)}
print(coordinates)


#! Example 2
old_price = {"milk": 1.02, "coffee": 2.5, "bread": 1.89}

dollar_to_pound = 0.76

new_price = {item: old_price[item]
             * dollar_to_pound for item in old_price}

# for item in old_price:
#     new_price[item] = old_price[item] * dollar_to_pound

print(new_price)

#! Example 2 modified
old_price = {"milk": 1.02, "coffee": 2.5, "bread": 1.89}

dollar_to_pound = 0.76
new_price = {item: value *
             dollar_to_pound for (item, value) in old_price.items()}
print(new_price)

#! Example 3
original_dict = {"Jack": 38, "Lincoln": 48,
                 "Theodore": 57, "John": 33, "Cecile": 21, "Tony": 18}
even_dict = {k: v for (k, v) in original_dict.items() if v % 2 == 0}
print(even_dict)

#! Another version of example 3
for item in original_dict:
    if original_dict[item] % 2 == 0:
        even_dict[item] = original_dict[item]

print(even_dict)
