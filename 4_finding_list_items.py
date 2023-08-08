# ---------- Finding List Items Index ----------

fruits = ['Apple', "Orange", "Banana"]
# fruits = ['Apple', "Banana"] * 5 # also possible, multiplication of list[]
numbers = [1, 1, 1, 1, 1, 1] * 5

# Example ->>> index()
print(fruits.index("Orange"))
# print(fruits.index("Mango")) # Error if item does not exist
# to prevent errors here is the better way
if "Mango" in fruits:
    print(fruits.index("Mango"))


# Example ->>> count() method
print(fruits.count("Mango"))
# it is useful to check whether the item exists or not, if yes how many
print(fruits.count("Banana"))
print(numbers.count(1))
