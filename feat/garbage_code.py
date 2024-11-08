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


# # # fromkeys()  - accept the sequences
# # letters = {'a', 'e', 'i', 'o', 'u'}
# # numbers = [1, 2]

# # vowels = dict.fromkeys(letters)  # none automatically
# # print(vowels)
# # vowels = dict.fromkeys(letters, numbers)
# # print(vowels)

# # anything = ['a', 'b', 'c']
# # anymany = [1, 2, 3]

# # randomDict = dict.fromkeys(anything, anymany)
# # print(randomDict)
# # print(type(vowels))
# # print(type(randomDict))

# random = {}
# print(type(random))

players = {
    "winger": "Kadir",
    "striker": "Adil",
    "defender": "Fozil",
    "winger_number": 7,
    "subs": "Bin, Maiwand, Gourab",
    11: "squad amount",
    "Best Player": "Kadir, 7, Uzbekistan",
    "Active Players": True,
    "Statistics": {"Win", "Win", "Lose", "Win"},
    "Scores": ["11:1", "0:3", "5:4"],
    "Cups": ("Sawo Gruz", "Nations Cup")
}

# # print({}.fromkeys(players))
# print({}.get("random_key"))

# print(players.items())
# print(players.keys())
# print(players.values())

# for item1 in players.values():
#     print(item1)
clubs = {
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5
}

# we are merging two dicts
players.update(clubs)
print(players.items())

players.update(dict(club="Real Madrid", opposite_team="Barcelona"))
print(players)


for i in players.items():
    print(i)

for i in players:
    # print(i, players[i])
    print(f"{i}: {players[i]}")

for i in players.keys():
    pass
