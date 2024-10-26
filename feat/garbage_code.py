name = list("Elbek")    # [E,  l,  b,  e,  k]
for i in name:
    print(i)
print(name)             # [E, l, b, e, k]
name = ["Elbek"]        # ["Elbek"]
for i in name:
    print(i)            # Elbek

numbers = [1, 2, 3, 4, 5]
fruits = ["Apple", "Banana", "Mango"]

multiplication = [i*i for i in numbers]
print(multiplication)

nums = list(range(1, 15))
nums_multiplied = [n*n for n in nums]
print(nums_multiplied)

nums = list(range(1, 15))
nums_multiplied = []
for n in nums:
    nums_multiplied.append(n//2)

print(nums_multiplied)

fruits2 = [fruit.lower() for fruit in fruits]
fruits2 = [fruit.upper() for fruit in fruits]
