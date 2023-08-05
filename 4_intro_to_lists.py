# ---------- Lists Introduction ----------

# Example ->>> simple lists
numbers = [1, 2, 3, 12, 64, 124, 654]
names = ["John", "Tom", "Mark", "Elon"]
# print(names)
# print(numbers)

# Example ->>> a list of lists
likes = [["tv", "pc", "laptop"], [
    "gaming", "watching", "fun"], ["pizze", "food"]]
# print(likes)


# Example ->>> a list of lists of lists
mixed = [[1, True], "Cat", "Dog", [["wind", "water"], ["earth", "fire"]]]
# print(mixed)

# Example ->>> a list of identical items
animal = ["cat"] * 10
# print(animal)

# Example ->>> list concatenation/merging
even_nums = [2, 4, 6, 8, 10]
odd_nums = [1, 3, 5, 7, 9]
cities = ["Tashkent", "New York", "London"]
booleans = [True, False]

mixed_data = even_nums + odd_nums + cities + booleans
print(mixed_data)

