# ---------- Accessing List Items ----------

# Example
collection = [28, "M", 32, "H", "Parrot", "Sea Biscuit"]

collection[5] = "Sea Bird"
print(collection[5])

for i in range(6):
    print(collection[i])


print(collection[0:2])
print(collection[:5])
print(collection[0:])
print(collection[:])

# Example
# step by 2, every second item from the list will be printed
print(collection[::2])
print(collection[::3])  # step by 3, every third item from the list

# If you want to reverse the order of items, simply put -1 [::-1]
print(collection[::-1])
print(collection[2::2])  # starting point and step by
print(collection[2:5:2])  # starting point, ending point, step by
