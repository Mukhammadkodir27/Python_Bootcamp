# ---------- Modifying List Items Part 1 ----------

# append()
# insert(index, item_name/value)
# pop()
# pop(index)
# remove()

numbers = [1, 55, 64, 124, 654]
names = ['John', 'Mark', 'Emily', "Sandra"]
fruits = ['Apple', "Orange", "Banana"]

# more about list methods, we all know that everything in python is an object
# append() method
# to add items to the end of a list - use append() method

names.append("Sandrine")  # to add item to the end of the list
# print(names)

# Example ->>> insert() method
# .insert(index_number, "item_name")
fruits.insert(1, "Lemon")
# print(fruits) # Apple, Lemon, Orange, Banana
fruits.insert(0, "Peach")
# print(fruits) # Peach, Apple, Lemon, Orange, Banana

# Example ->>> pop() method
# removes item from the end of a list
numbers.pop()
# print(numbers) # last item is deleted

# Example ->>> pop() with index
numbers.pop(-1)  # removes the last item
numbers.pop(1)
names.pop(3)


# Example ->>> remove() method
# .remove("item_name")
fruits.remove("Banana")

# Example ->>> del statement
del numbers[0]
del fruits[1:3]

# ---------- Part 2 ----------

numbers = [1, 23, 64, 124, 654]
names = ['Hoit', 'David', 'Tom', "Sandra"]
fruits = ['Apple', "Orange", "Banana"]

# Example ->>> clear() method
# removes all objects/items in a list
print(fruits.clear())
# fruits.clear()

# Example ->>> reverse() method
names.reverse()
# print(names) # Sandra, Tom, David, Hoit

numbers.reverse()
# print(numbers)


# How to join list items together
# Example ->>> join()

print("".join(names))  # SandraTomDavidHoit
print(" ".join(names))  # Sandra Tom David Hoit
print(", ".join(names))  # Sandra, Tom, David, Hoit
