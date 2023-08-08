# ---------- Looping Over Lists ----------

# Example
# Lists are iterables, we can iterate over any iterable, or we can loop over any iterable
letters = ["a", "b", "c"]
strings = list("Mukhammadkodir")

for letter in letters:
    print(letter)

print(strings)

for i in range(len(letters)):
    print(letters[i])

# Example
for letter in enumerate(letters):
    print(letter)
# out put will be like this
# (0, 'a')
# (1, 'b')
# (2, 'c')
# it is paring the list items with their index numbers

# Example
print("=== Example ===")

for index, item in enumerate(letters):
    print(index, item)

# Example
# print('---')  Unpacking List Items
# items = (0, 'a')
# index, letter = items
# print(index)
# print(letter)

