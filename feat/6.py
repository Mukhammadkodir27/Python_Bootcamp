# Accessing list items

random_generated = ["Mukhammadkodir", 21, "Developer", 7, 17, 27]

print(random_generated[0])
print(random_generated[0:])
print(random_generated[:])
print(random_generated[:3])
print(random_generated[0:5:2])
print(random_generated[0::3])  # step by 3
print(random_generated[::4])  # step by 4

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
reversed_numbers = numbers[::-1]
print(reversed_numbers[2::2-1])
print(reversed_numbers)
