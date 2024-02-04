# Do not confuse list() method with List methods

numbers = [range(100)]
print(numbers)  # [0, 100]
print(len(numbers))  # 1 item

nums = list(range(100))
print(nums)  # [0, 1, 2, 3, 4, 5, 6, ... 99]
print(len(nums))  # 100 items

for n in nums:
    print(n)
# 0,
# 1,
# 2,
# ...
# 99

# we can also create a list of string because strings are also iterable

random_name = list("Izabella")
print(random_name)
print(len(random_name))

for n in random_name:
    print(n)

ran_name = ["Izabella"]
print(ran_name)
print(len(ran_name))

for n in ran_name:
    print(n)
