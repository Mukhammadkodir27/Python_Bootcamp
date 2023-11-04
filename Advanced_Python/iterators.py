# ---------- Iterators ----------

# __iter__() & __next__()

numbers = [1, 2, 3, 4, 5]

first_element = iter(numbers)        # creating our iterator

# iterators return one element or value at a time and using special method __next__()

print(next(first_element)) #1
print(next(first_element)) #2
print(type(next(first_element)))  # even if we used type with __next__(), it counts as next element

# next() == __next__()


first_iterator = numbers.__iter__()

print(first_iterator.__next__())  #1
print(first_iterator.__next__())  #2
print(first_iterator.__next__())  #3


# --- iterating over using for loop
print("iterator above")
print("for loop below")

for number in numbers:
    print(number)
