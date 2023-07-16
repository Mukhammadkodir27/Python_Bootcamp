# ------------------ # String Methods # ------------------ #

# 1 - len()
address = "Lodz, Poland"
print(len(address))


# 2 - [] Notation
# from left to right start with 0 ... 9
# from right to left start with -1 ... -9
print(address[6])
print(address[0])
print(address[7])
print(address[-1])  # d last word from "Lodz. Poland"
print(address[-9])  # z -9 word from "Lodz, Poland"


# 3 - [] Notation
print(address[0:4])
print(address[-7:-1])
print(address[0:])
print(address[:9])
print(address[:])


#  4 - concatenation - means combining ...
country = "Poland"
city = "Lodz"
full_address = city + ", " + country
print(full_address)


# 5 - upper()
print(address.upper())  # LODZ, POLAND


# 6 - lower()
print(address.lower())  # lodz, poland


# 7 - title()  - capitalize the first letter of every word
print(full_address.title())


# 8 - strip()  -  remove spaces, empty spaces from beginning to the end
job = "            Programmer      "
print(job.strip())
print(job.lstrip())   # strip from left
print(job.rstrip())   # strip from right


# 9 - find()
