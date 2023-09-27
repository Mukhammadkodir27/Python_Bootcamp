# ---------- Filter Function ----------

# filter function takes 2 parameters, one is function that we create and the second one is an iterable. 
# or filter function could be as None but this to be continued...

# Iterable
letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

# Function 
def filter_vowels(letter):
    vowels = ["a", "e", "i", "o", "u"]

    if (letter in vowels):
        return True
    else: 
        return False
    

# now we have a function and iterable, time to use our filter method

filtered_vowels = filter(filter_vowels, letters)
print(filtered_vowels)
print(type(filtered_vowels)) # class filter (type)

print("The vowels are: ")

for vowel in filtered_vowels:
    print(vowel)
