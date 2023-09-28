# ---------- Zip Function ----------

# result = zip(iterator1, iterator2, iterator3) # the code will run according to the smallest item, if iterator2 has 3 elements, then it will be executed 3 times only

numbers_list = [1, 2, 3, 4, 5, 6]
names_list = ['Kadir', 'Adil', 'Fozil']

# no iterables are passed
result = zip()
# print(result)

# converting zip to a set
result_zip = set(result)
print(result_zip)

# passing 2 iterables to our zip
result = zip(names_list, numbers_list)
print(dict(result))

# it will run until the smallest iterable reaches the end

# passing 3 iterables to our zip

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
names = ["Kadir", "Adil", "Fozil", "Bin"]
numbers_tuple = ('ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX')

results3 = zip(numbers, names, numbers_tuple)
print(set(results3))
# print(tuple(results3))
# print(list(results3))

# kinda it adds all of them one by one like real 7zip
